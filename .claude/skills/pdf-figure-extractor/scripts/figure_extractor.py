import os
import json
import base64
import re
import io
import sys
import time
import argparse
from pathlib import Path
from google import genai
from google.genai import types
from PIL import Image

# 尝试导入 fitz (pymupdf) 处理 PDF
try:
    import fitz
except ImportError:
    print("⚠️  未安装 pymupdf，将无法处理 PDF 文件。请运行: uv pip install pymupdf")

# ============================================================
# 命令行参数解析
# ============================================================
parser = argparse.ArgumentParser(description="PDF 教材插图智能提取工具")
parser.add_argument("--input", "-i", type=str, help="输入目录（PDF 页面或图片目录）")
parser.add_argument("--output", "-o", type=str, help="输出目录")
parser.add_argument("--pdf", action="store_true", help="使用 PDF 模式（默认）")
parser.add_argument("--png", action="store_true", help="使用 PNG/图片模式")
parser.add_argument("--chapter", "-c", type=int, help="快速选择章节（1-5），自动设置路径")
parser.add_argument("--force", action="store_true", help="强制重刷所有页面")
parser.add_argument("--crop-only", action="store_true", help="仅裁剪模式（不调用 API）")
args = parser.parse_args()

# ============================================================
# 配置区
# ============================================================
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# --- 模式选择 ---
if args.png:
    USE_PDF = False
elif args.pdf or not args.png:  # 默认 PDF 模式
    USE_PDF = True

# --- 路径设置 ---
# 如果通过 --chapter 指定，自动设置路径
if args.chapter:
    base = "notes/differential-geometry/do-carmo-curves-surfaces/figures"
    if USE_PDF:
        INPUT_DIR = f"{base}/chapter{args.chapter}/pages_pdf"
        OUTPUT_DIR = f"{base}/chapter{args.chapter}/output_pdf"
    else:
        INPUT_DIR = f"{base}/chapter{args.chapter}/pages_400dpi"
        OUTPUT_DIR = f"{base}/chapter{args.chapter}/output"
elif args.input and args.output:
    # 如果通过命令行指定
    INPUT_DIR = args.input
    OUTPUT_DIR = args.output
else:
    # 默认路径（需要手动修改）
    USE_PDF = True  # 修改这里切换模式
    if USE_PDF:
        INPUT_DIR = "notes/differential-geometry/do-carmo-curves-surfaces/figures/chapter2/pages_pdf"
        OUTPUT_DIR = "notes/differential-geometry/do-carmo-curves-surfaces/figures/chapter2/output_pdf"
    else:
        INPUT_DIR = "notes/differential-geometry/do-carmo-curves-surfaces/figures/chapter2/pages_400dpi"
        OUTPUT_DIR = "notes/differential-geometry/do-carmo-curves-surfaces/figures/chapter2/output"

RESULT_JSON = os.path.join(OUTPUT_DIR, "detection_results.json")

# 指定文件。为空则扫描全目录。
IMAGE_FILES = []

# ============================================================
# 提示词
# ============================================================
PROMPT = """
你是一个拥有像素级精准度的顶尖排版与图像提取专家。你的任务是分析这张数学教材扫描页，找出所有的数学插图（Figure），并输出完美的裁剪边界框（bounding box）。

你需要完美复刻“专业人工裁剪”的标准。请严格遵循以下【边界框截取几何美学标准】：

1. 【元素完整性】：这是最高优先级。确保坐标轴箭头、整条曲线、所有的字母标签（x, y, z, θ）都在框内。
2. 【禁止触边】：**如果你的边界线（bbox edge）接触到了任何线条（即使是线条的末端），你必须继续向外扩展该边界至少 0.05 的距离**。截出的图中，任何图形元素与图片边缘之间必须有明显的白边间隙，绝对不能看起来像是被切断了。
3. 【并排图的策略】：对于 Figure 1-1 和 Figure 1-2 这种左右并排的图，如果右图的曲线向左延伸得很远，不要犹豫，直接把它的 x1 设置到左侧区域内（允许和 Figure 1-1 的 x 范围产生显著重叠）。**宁愿提取出来的图包含另一张图的一小部分，也绝对不能截断本图的曲线。**
4. 【包围图注】：y2 必须完全包围 "Figure X-X" 及其描述文本，并在下方留出 0.03 的空白。
5. 【避开文本】：y1 应当在不截断图形顶部元素的前提下，尽可能靠近图形顶部，但不要包含上方的正文行。
6. 【视觉对称】：对于单张图，确保左右留白基本对称。

严格按以下 JSON 格式输出（只输出纯 JSON）：

{
  "figures": [
    {
      "id": "Figure 1-1",
      "description": "简短描述",
      "bbox": {
        "x1": 0.02,
        "y1": 0.08,
        "x2": 0.50,
        "y2": 0.38
      }
    }
  ]
}

如果没有插图，输出 {"figures": []}。
"""

# ============================================================
# 核心函数
# ============================================================

def init_client():
    if not GEMINI_API_KEY:
        print("❌ 错误: 未设置环境变量 GEMINI_API_KEY")
        exit(1)
    client = genai.Client(api_key=GEMINI_API_KEY)
    print("✅ Gemini 客户端初始化成功")
    return client


def detect_figures(client, file_path: str) -> tuple:
    """调用 Gemini 识别单张文件，包含自动重试机制。失败返回 None, 0"""
    print(f"\n🔍 正在识别: {file_path}")
    
    ext = os.path.splitext(file_path)[1].lower()
    mime_type = "application/pdf" if ext == ".pdf" else "image/png"
    
    with open(file_path, "rb") as f:
        file_bytes = f.read()

    max_retries = 3
    last_error = ""
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=[
                    types.Part.from_bytes(data=file_bytes, mime_type=mime_type),
                    types.Part.from_text(text=PROMPT)
                ],
                config=types.GenerateContentConfig(temperature=0.1)
            )
            
            usage = response.usage_metadata
            img_tokens = usage.total_token_count - usage.prompt_token_count - usage.candidates_token_count
            print(f"   🎫 Tokens: Text_In={usage.prompt_token_count}, Text_Out={usage.candidates_token_count}, File_Content={img_tokens}, Total={usage.total_token_count}")

            raw_text = response.text.strip()
            raw_text = re.sub(r"^```json\s*", "", raw_text)
            raw_text = re.sub(r"^```\s*", "", raw_text)
            raw_text = re.sub(r"\s*```$", "", raw_text)

            result = json.loads(raw_text)
            figures = result.get("figures", [])
            print(f"   → 检测到 {len(figures)} 张插图")
            return figures, usage.total_token_count

        except Exception as e:
            last_error = str(e)
            wait_time = (attempt + 1) * 10
            if attempt < max_retries - 1:
                print(f"⚠️  错误: {last_error}。正在重试({attempt+1}/{max_retries})，等待 {wait_time}s...")
                time.sleep(wait_time)
            else:
                print(f"❌ 最终识别失败: {last_error}")
                return None, 0


def crop_and_save(file_path: str, figures: list, output_dir: str) -> list:
    """根据 bbox 裁剪并保存每张插图。支持图片和 PDF (极高清渲染后裁剪)"""
    if not figures:
        return []

    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".pdf":
        doc = fitz.open(file_path)
        page = doc[0]
        # 🚀 提升 DPI 到 600，并开启抗锯齿，获得极致清晰度
        pix = page.get_pixmap(dpi=600, colorspace=fitz.csRGB)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        doc.close()
    else:
        try:
            img = Image.open(file_path)
        except Exception as e:
            print(f"❌ 无法打开图片 {file_path}: {e}")
            return []
        
    W, H = img.size
    saved = []

    for fig in figures:
        bbox = fig.get('bbox')
        if not bbox: continue
        
        x1 = max(0.0, bbox.get('x1', 0))
        y1 = max(0.0, bbox.get('y1', 0))
        x2 = min(1.0, bbox.get('x2', 1))
        y2 = min(1.0, bbox.get('y2', 1))

        # 转换为整数坐标
        box = (int(W * x1), int(H * y1), int(W * x2), int(H * y2))

        # 确保文件名安全
        safe_id = fig['id'].replace(" ", "_").replace("/", "-")
        out_name = f"{safe_id}.png"
        out_path = os.path.join(output_dir, out_name)

        # 裁剪并保存
        img.crop(box).save(out_path, dpi=(600, 600))
        saved.append(out_path)
        
        w_px = box[2] - box[0]
        h_px = box[3] - box[1]
        print(f"   💾 已保存(高清): {out_path}  ({w_px}x{h_px}px)")

    return saved


def run_pipeline():
    """主流程：识别 → 裁剪 → 保存结果"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    all_results = {}
    if os.path.exists(RESULT_JSON):
        try:
            with open(RESULT_JSON, "r", encoding="utf-8") as f:
                all_results = json.load(f)
            print(f"📦 已加载现有历史记录: {len(all_results)} 张页面")
        except Exception as e:
            print(f"⚠️  加载 {RESULT_JSON} 失败: {e}")

    crop_only = args.crop_only
    force_all = args.force
    
    if crop_only:
        print("✂️  [模式: 仅裁剪] 沿用现有坐标。")
    else:
        print(f"🤖 [模式: 智能识别] 输入源: {'PDF' if USE_PDF else 'PNG'}")
        client = init_client()

    p = Path(INPUT_DIR)
    valid_exts = [".png", ".jpg", ".jpeg", ".pdf"]
    target_files = sorted([f.name for f in p.glob("*") if f.suffix.lower() in valid_exts])
    if IMAGE_FILES:
        target_files = [f for f in IMAGE_FILES if f.strip()]
    
    print(f"📁 待处理列表: {len(target_files)} 个文件")

    total_tokens = 0
    actual_processed = 0

    for file_name in target_files:
        file_path = os.path.join(INPUT_DIR, file_name)
        if not os.path.exists(file_path):
            if IMAGE_FILES: # 仅在手动指定时提醒
                print(f"⚠️  跳过文件 (路径不存在): {file_path}")
            continue

        record = all_results.get(file_name)
        is_success = False
        cached_figures = []

        if isinstance(record, list):
            is_success = True
            cached_figures = record
        elif isinstance(record, dict) and record.get("status") == "success":
            is_success = True
            cached_figures = record.get("figures", [])
        
        if not force_all and not crop_only and is_success:
            continue

        try:
            if crop_only:
                if not is_success: continue
                print(f"\n✂️  重新裁剪: {file_name}")
                crop_and_save(file_path, cached_figures, OUTPUT_DIR)
            else:
                figures, tokens = detect_figures(client, file_path)
                
                if figures is not None:
                    total_tokens += tokens
                    crop_and_save(file_path, figures, OUTPUT_DIR)
                    all_results[file_name] = {
                        "status": "success",
                        "figures": figures,
                        "tokens": tokens,
                        "time": time.strftime("%Y-%m-%d %H:%M:%S")
                    }
                else:
                    all_results[file_name] = {
                        "status": "error",
                        "error_msg": "API failure after retries",
                        "time": time.strftime("%Y-%m-%d %H:%M:%S")
                    }

                with open(RESULT_JSON, "w", encoding="utf-8") as f:
                    json.dump(all_results, f, ensure_ascii=False, indent=2)
            
            actual_processed += 1

        except Exception as e:
            print(f"❌ 程序底层异常 ({file_name}): {e}")

    print(f"\n✅ 处理完成！本次实际操作了 {actual_processed} 个页面。")
    if not crop_only:
        print(f"📊 累计消耗 {total_tokens} tokens")


if __name__ == "__main__":
    run_pipeline()
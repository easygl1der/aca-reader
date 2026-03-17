import google.generativeai as genai
import PIL.Image
import os

# Using the provided env var or setting it if missing (assuming GEMINI_API_KEY is available)
if "GEMINI_API_KEY" in os.environ:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
else:
    print("Warning: GEMINI_API_KEY not found in environment.")

def get_bboxes(image_path):
    model = genai.GenerativeModel('gemini-2.5-flash')
    img = PIL.Image.open(image_path)
    
    prompt = """找出 Figure 1-33 的精确位置。

输出格式（每个 Figure 必须输出一行）：
Figure: 1-33
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX

规则：
- 坐标以图片整体宽高为基准，0.00 ~ 1.00
- 必须包含完整的图注文字 Figure 1-33
- 如果图注在图形下方，y2 要延伸到包含图注
- 四周留 0.02 边距
"""
    
    response = model.generate_content([img, prompt])
    print(response.text)

if __name__ == "__main__":
    get_bboxes("/Users/yueyh/.gemini/tmp/figure-extractor/temp_page.png")

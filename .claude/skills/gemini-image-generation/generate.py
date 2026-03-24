#!/usr/bin/env python3
"""
Gemini Image Generation Script
使用 Google Gemini API 生成图片
"""

import os
import sys
import json
import base64
import argparse
import urllib.request
import urllib.error

# 默认配置
DEFAULT_MODEL = "gemini-2.5-flash-image"
DEFAULT_OUTPUT = "gemini_output.png"
API_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"


def generate_image(prompt: str, api_key: str, model: str = DEFAULT_MODEL, output: str = DEFAULT_OUTPUT) -> bool:
    """生成图片"""
    url = f"{API_BASE_URL}/{model}:generateContent"

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]}
    }

    data = json.dumps(payload).encode('utf-8')

    req = urllib.request.Request(
        url,
        data=data,
        headers={
            'Content-Type': 'application/json',
            'x-goog-api-key': api_key
        },
        method='POST'
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode('utf-8'))

            # 提取图片数据
            if 'candidates' in result and len(result['candidates']) > 0:
                candidate = result['candidates'][0]
                if 'content' in candidate and 'parts' in candidate['content']:
                    for part in candidate['content']['parts']:
                        if 'inlineData' in part and 'data' in part['inlineData']:
                            image_data = part['inlineData']['data']

                            # 保存图片
                            with open(output, 'wb') as f:
                                f.write(base64.b64decode(image_data))

                            print(f"✅ 图片已保存到: {output}")
                            return True

            print("❌ 未找到图片数据")
            print(f"响应: {json.dumps(result, indent=2, ensure_ascii=False)[:500]}")
            return False

    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        print(f"❌ HTTP 错误 {e.code}:")
        try:
            error_json = json.loads(error_body)
            print(json.dumps(error_json, indent=2, ensure_ascii=False))
        except:
            print(error_body)
        return False
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description='Gemini 图片生成')
    parser.add_argument('prompt', help='图片描述文本')
    parser.add_argument('-m', '--model', default=DEFAULT_MODEL, help=f'使用的模型 (默认: {DEFAULT_MODEL})')
    parser.add_argument('-o', '--output', default=DEFAULT_OUTPUT, help=f'输出文件名 (默认: {DEFAULT_OUTPUT})')
    parser.add_argument('-k', '--api-key', default=None, help='API Key (默认: 环境变量 GEMINI_API_KEY)')
    parser.add_argument('-y', '--yes', action='store_true', help='直接确认，不询问')

    args = parser.parse_args()

    # 获取 API Key
    api_key = args.api_key or os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("❌ 请设置 GEMINI_API_KEY 环境变量或使用 -k 参数")
        sys.exit(1)

    # 验证 API Key 格式
    if not api_key.startswith('AIza'):
        print(f"⚠️  API Key 格式可能不正确 (应以 AIza 开头)")

    print(f"🤖 使用模型: {args.model}")
    print(f"📝 提示词: {args.prompt}")
    print(f"📁 输出文件: {args.output}")

    # 询问确认
    if not args.yes:
        confirm = input("\n❓ 确定要生成这张图片吗? (y/n): ")
        if confirm.lower() not in ['y', 'yes', '是', '确认']:
            print("❌ 已取消生成")
            sys.exit(0)

    print("⏳ 正在生成...")

    success = generate_image(args.prompt, api_key, args.model, args.output)
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()

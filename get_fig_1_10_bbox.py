import os
import json
import base64
import urllib.request
import ssl
import re

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

API_KEY = os.environ.get('GEMINI_API_KEY')
MODEL = 'gemini-flash-latest' # Using a stable model

def call_gemini(image_path, figure_id):
    with open(image_path, 'rb') as f:
        image_base64 = base64.b64encode(f.read()).decode('utf-8')

    url = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent'
    prompt = f'''找出 Figure {figure_id} 的精确位置。

输出格式（每个 Figure 必须输出一行）：
Figure: {figure_id}
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX

规则：
- 坐标以图片整体宽高为基准，0.00 ~ 1.00
- 必须包含完整的图注文字 Figure {figure_id}
- 如果图注在图形下方，y2 要延伸到包含图注
- 四周留 0.02 边距'''

    payload = {
        'contents': [{
            'parts': [
                {'text': prompt},
                {'inlineData': {'mimeType': 'image/png', 'data': image_base64}}
            ]
        }],
        'generationConfig': {'temperature': 0.1, 'maxOutputTokens': 1024}
    }

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={
        'Content-Type': 'application/json',
        'x-goog-api-key': API_KEY
    }, method='POST')

    try:
        with urllib.request.urlopen(req, timeout=120, context=ssl_context) as response:
            result = json.loads(response.read().decode('utf-8'))
            if 'candidates' in result:
                return result['candidates'][0]['content']['parts'][0].get('text', '')
    except Exception as e:
        print(f'Error: {e}')
    return None

if __name__ == "__main__":
    image_path = "/Users/yueyh/.gemini/tmp/figure-extractor/temp_page.png"
    figure_id = "1-10"
    result = call_gemini(image_path, figure_id)
    if result:
        print(result.strip())

import os
import json
import base64
import urllib.request
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

API_KEY = os.environ.get('GEMINI_API_KEY')
MODEL = 'gemini-flash-latest'
IMAGE_PATH = '/Users/yueyh/.gemini/tmp/figure-extractor/temp_page.png'

PROMPT = '''看这张教材原图，找出 Figure 2-3 的精确位置。

请仔细检查图注的位置。通常图注在图形下方。
确保 x1, y1, x2, y2 包含图形主体和下方的 Figure 2-3 文字。
坐标以图片整体宽高为基准，0.00 ~ 1.00。
四周留 0.02 边距。

输出格式（每个 Figure 必须输出一行）：
Figure: X-Y
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX'''

def call_gemini():
    with open(IMAGE_PATH, 'rb') as f:
        image_base64 = base64.b64encode(f.read()).decode('utf-8')

    url = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}'
    
    payload = {
        'contents': [{
            'parts': [
                {'text': PROMPT},
                {'inlineData': {'mimeType': 'image/png', 'data': image_base64}}
            ]
        }]
    }

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'}, method='POST')

    try:
        with urllib.request.urlopen(req, timeout=300, context=ssl_context) as response:
            result = json.loads(response.read().decode('utf-8'))
            print(result['candidates'][0]['content']['parts'][0]['text'])
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    call_gemini()

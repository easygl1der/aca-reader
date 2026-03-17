import os
import json
import base64
import urllib.request
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

API_KEY = os.environ.get('GEMINI_API_KEY')
# Use the best model available, e.g., gemini-1.5-pro-latest
MODEL = 'gemini-1.5-flash'
IMAGE_PATH = '/Users/yueyh/.gemini/tmp/figure-extractor/temp_page.png'

PROMPT = '''找出 Figure 2-5 的精确位置。

输出格式（每个 Figure 必须输出一行）：
Figure: X-Y
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX

规则：
- 坐标以图片整体宽高为基准，0.00 ~ 1.00
- 必须包含完整的图注文字 Figure X-Y
- 如果图注在图形下方，y2 要延伸到包含图注
- 四周留 0.02 边距'''

def call_gemini():
    if not API_KEY:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return

    try:
        with open(IMAGE_PATH, 'rb') as f:
            image_base64 = base64.b64encode(f.read()).decode('utf-8')
    except Exception as e:
        print(f"Error reading image: {e}")
        return

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
        # print error body if available
        if hasattr(e, 'read'):
            print(e.read().decode('utf-8'))

if __name__ == "__main__":
    call_gemini()
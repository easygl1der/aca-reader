import os
import json
import base64
import urllib.request
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

API_KEY = os.environ.get('GEMINI_API_KEY')
MODEL = 'gemini-pro-latest'

image_path = "/Users/yueyh/Projects/aca-workflow/notes/differential-geometry/do-carmo-curves-surfaces/figures/chapter1/pages_400dpi/page-059.png"
figure_id = "1-31"

PROMPT = f'''Look at this page and tell me what Figure numbers you see. 
If you see Figure {figure_id}, please provide its precise bounding box.

输出格式（必须精确）：
Figure: {figure_id}
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX

规则：
- 坐标以图片整体宽高为基准，0.00 ~ 1.00
- 必须包含完整的图注文字 Figure {figure_id}
- 如果图注在图形下方，y2 要延伸到包含图注
- 四周留 0.02 边距'''

with open(image_path, 'rb') as f:
    image_base64 = base64.b64encode(f.read()).decode('utf-8')

url = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}'
payload = {
    'contents': [{
        'parts': [
            {'text': PROMPT},
            {'inlineData': {'mimeType': 'image/png', 'data': image_base64}}
        ]
    }],
    'generationConfig': {'temperature': 0, 'maxOutputTokens': 1024}
}

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'}, method='POST')

try:
    with urllib.request.urlopen(req, timeout=120, context=ssl_context) as response:
        resp_data = response.read().decode('utf-8')
        result = json.loads(resp_data)
        if 'candidates' in result:
            text = result['candidates'][0]['content']['parts'][0].get('text', '')
            print(text)
        else:
            print(resp_data)
except Exception as e:
    print(f'Error: {e}')

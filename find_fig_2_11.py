import os
import json
import base64
import urllib.request
import ssl

def get_fig_bbox():
    IMAGE_PATH = '/Users/yueyh/.gemini/tmp/figure-extractor/temp_page.png'
    API_KEY = os.environ.get('GEMINI_API_KEY')
    MODEL = 'gemini-2.0-flash'
    
    if not os.path.exists(IMAGE_PATH):
        print(f"Error: {IMAGE_PATH} not found")
        return

    with open(IMAGE_PATH, 'rb') as f:
        image_base64 = base64.b64encode(f.read()).decode('utf-8')

    url = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}'
    
    prompt = '''找出 Figure 2-11 的精确位置。

输出格式（每个 Figure 必须输出一行）：
Figure: X-Y
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX

规则：
- 坐标以图片整体宽高为基准，0.00 ~ 1.00
- 必须包含完整的图注文字 Figure 2-11
- 如果图注在图形下方，y2 要延伸到包含图注
- 四周留 0.02 边距'''

    payload = {
        'contents': [{
            'parts': [
                {'text': prompt},
                {'inlineData': {'mimeType': 'image/png', 'data': image_base64}}
            ]
        }]
    }

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'}, method='POST')

    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    try:
        with urllib.request.urlopen(req, timeout=60, context=ssl_context) as response:
            result = json.loads(response.read().decode('utf-8'))
            if 'candidates' in result and result['candidates']:
                print(result['candidates'][0]['content']['parts'][0]['text'])
            else:
                print(f"No candidates found in response: {result}")
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    get_fig_bbox()

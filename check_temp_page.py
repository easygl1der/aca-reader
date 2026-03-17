from PIL import Image
import os
import json
import base64
import urllib.request
import ssl

def check_image():
    IMAGE_PATH = '/Users/yueyh/.gemini/tmp/figure-extractor/temp_page.png'
    if not os.path.exists(IMAGE_PATH):
        print(f"File not found: {IMAGE_PATH}")
        return

    API_KEY = os.environ.get('GEMINI_API_KEY')
    MODEL = 'gemini-2.0-flash'
    
    with open(IMAGE_PATH, 'rb') as f:
        image_base64 = base64.b64encode(f.read()).decode('utf-8')

    url = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}'
    
    payload = {
        'contents': [{
            'parts': [
                {'text': 'Describe this image and tell me if it contains "Figure 2-6". If not, tell me which Figure numbers are present.'},
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
        with urllib.request.urlopen(req, timeout=30, context=ssl_context) as response:
            result = json.loads(response.read().decode('utf-8'))
            print(result['candidates'][0]['content']['parts'][0]['text'])
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    check_image()

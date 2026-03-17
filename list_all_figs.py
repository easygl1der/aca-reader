import os
import json
import base64
import urllib.request
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

API_KEY = os.environ.get('GEMINI_API_KEY')
MODEL = 'gemini-2.0-flash-lite' # Try lite for broad scan? Or just flash.
# Actually let's use gemini-2.5-flash as it's the "smartest" one available here.
MODEL = 'gemini-2.5-flash'

image_path = "/Users/yueyh/.gemini/tmp/figure-extractor/temp_page.png"

PROMPT = '''Identify all figures on this page. For each figure, provide its number and a precise bounding box.
Include the figure itself and its caption.

Output format:
Figure: [Number], Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX
'''

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
    'generationConfig': {'temperature': 0}
}

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'}, method='POST')

try:
    with urllib.request.urlopen(req, timeout=120, context=ssl_context) as response:
        resp_data = response.read().decode('utf-8')
        result = json.loads(resp_data)
        if 'candidates' in result:
            text = result['candidates'][0]['content']['parts'][0].get('text', '')
            print(text.strip())
        else:
            print(resp_data)
except Exception as e:
    print(f'Error: {e}')

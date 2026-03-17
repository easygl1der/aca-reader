import os
import json
import urllib.request
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

API_KEY = os.environ.get('GEMINI_API_KEY')

url = f'https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}'

req = urllib.request.Request(url, method='GET')

try:
    with urllib.request.urlopen(req, timeout=120, context=ssl_context) as response:
        result = json.loads(response.read().decode('utf-8'))
        for model in result.get('models', []):
            print(model.get('name'))
except Exception as e:
    print(f'Error: {e}')

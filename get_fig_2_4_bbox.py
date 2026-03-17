import os
try:
    import google.generativeai as genai
    import PIL.Image
except ImportError:
    print("Please install google-generativeai and pillow")
    exit(1)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def get_bboxes(image_path):
    model = genai.GenerativeModel('gemini-2.5-flash')
    img = PIL.Image.open(image_path)
    
    prompt = """找出图片中的 Figure 2-4。
请提供其精确的 Bounding Box。
要求：
1. 坐标以图片整体宽高为基准，范围 0.00 ~ 1.00。
2. 必须包含完整的图注文字 'Figure 2-4'。
3. 如果图注在图形下方，y2 要延伸到包含图注。
4. 在图形和图注的四周留出 0.02 的边距。
5. 严格按照以下格式输出（每个 Figure 一行）：
Figure: X-Y
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX
"""
    
    response = model.generate_content([img, prompt])
    print(response.text)

if __name__ == "__main__":
    get_bboxes("/Users/yueyh/.gemini/tmp/figure-extractor/temp_page.png")
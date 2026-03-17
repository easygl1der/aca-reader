import google.generativeai as genai
import PIL.Image
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def get_bboxes(image_path):
    model = genai.GenerativeModel('gemini-2.5-flash')
    img = PIL.Image.open(image_path)
    
    prompt = """找出图片中的 Figure 1-30 和 Figure 1-31。
对于每个 Figure，请提供其精确的 Bounding Box。
要求：
1. 坐标以图片整体宽高为基准，范围 0.00 ~ 1.00。
2. 必须包含完整的图注文字 'Figure 1-30' 或 'Figure 1-31'。
3. 如果图注在图形下方，y2 要延伸到包含图注。
4. 在图形和图注的四周留出 0.02 的边距。
5. 严格按照以下格式输出（每个 Figure 一行）：
Figure: X-Y
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX
"""
    
    response = model.generate_content([img, prompt])
    print(response.text)

if __name__ == "__main__":
    get_bboxes("page_59.png")

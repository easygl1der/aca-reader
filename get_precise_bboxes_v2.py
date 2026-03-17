import google.generativeai as genai
import PIL.Image
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def get_bboxes(image_path):
    model = genai.GenerativeModel('gemini-2.5-flash')
    img = PIL.Image.open(image_path)
    
    prompt = """请仔细观察图片，给出 Figure 1-30 和 Figure 1-31 的精确 Bounding Box。
注意：
1. Figure 1-30 和 Figure 1-31 是并排的。Figure 1-30 在左边，Figure 1-31 在右边。
2. 边界框必须包含图形本身以及其对应的完整图注（例如 'Figure 1-30. ...'）。
3. 坐标范围 0.00 到 1.00。
4. 在图形和图注边缘外侧增加 0.02 的边距（Margin）。
5. 结果请严格按此格式：
Figure: 1-30
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX
Figure: 1-31
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX
"""
    
    response = model.generate_content([img, prompt])
    print(response.text)

if __name__ == "__main__":
    get_bboxes("page_59.png")

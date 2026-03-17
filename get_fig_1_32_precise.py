import google.generativeai as genai
import PIL.Image
import os
import sys

if "GEMINI_API_KEY" not in os.environ:
    print("Error: GEMINI_API_KEY not set in environment.")
    sys.exit(1)

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def get_bboxes(image_path):
    model = genai.GenerativeModel('gemini-2.5-flash')
    img = PIL.Image.open(image_path)
    
    prompt = """请仔细观察图片，给出 Figure 1-32 的精确 Bounding Box。
注意：
1. 边界框必须包含图形本身以及其对应的完整图注（例如 'Figure 1-32. ...'）。
2. 坐标范围 0.00 到 1.00。
3. 在图形和图注边缘外侧增加 0.02 的边距（Margin）。
4. 结果请严格按此格式：
Figure: 1-32
Bounding Box: x1=0.XX, y1=0.XX, x2=0.XX, y2=0.XX
"""
    
    response = model.generate_content([img, prompt])
    print(response.text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_bboxes(sys.argv[1])
    else:
        print("Please provide an image path.")

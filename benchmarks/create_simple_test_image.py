#!/usr/bin/env python3
"""
建立簡單的測試圖片
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_simple_test_image():
    """建立一張包含文字的簡單測試圖片"""
    
    # 建立白色背景的圖片
    width, height = 400, 100
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)
    
    # 設定文字
    text = "Hello World OCR Test"
    
    try:
        # 嘗試使用系統字型
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    except:
        try:
            # 備用字型
            font = ImageFont.truetype("arial.ttf", 24)
        except:
            # 使用預設字型
            font = ImageFont.load_default()
    
    # 計算文字位置 (置中)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # 在圖片上繪製文字
    draw.text((x, y), text, fill='black', font=font)
    
    # 儲存圖片
    image_path = "simple_test_image.png"
    image.save(image_path)
    
    print(f"測試圖片已建立: {image_path}")
    print(f"圖片內容: {text}")
    
    return image_path, text

if __name__ == "__main__":
    image_path, text_content = create_simple_test_image()
    
    print("\n現在你可以執行以下命令進行測試:")
    print(f"python run_ocr_single_file.py --image_file_path {image_path} --result_output_path result.json")
    print(f"\n預期結果應該是: {text_content}")

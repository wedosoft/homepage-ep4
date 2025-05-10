from PIL import Image
import os
from datetime import datetime

# 입력 폴더 경로 설정
input_folder = "images"  # 여기에 원본 이미지들이 들어 있음

# 출력 폴더에 고정된 이름 사용
output_folder = "optimized"

# 최적화 옵션
max_width = 1200  # 가로 크기 제한
quality = 80      # 0~100

# 타임스탬프 설정 (파일명에 추가)
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

def optimize_image(input_path, output_path, max_width, quality):
    with Image.open(input_path) as img:
        if img.width > max_width:
            ratio = max_width / img.width
            new_size = (max_width, int(img.height * ratio))
            img = img.resize(new_size, Image.LANCZOS)
        img.save(output_path, format="WebP", quality=quality, method=6)
        print(f"✅ 최적화 완료: {output_path}")
    os.remove(input_path)
    print(f"🗑 원본 삭제됨: {input_path}")

# 출력 폴더 생성
os.makedirs(output_folder, exist_ok=True)

# 입력 폴더 내 모든 이미지 파일 처리
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        input_path = os.path.join(input_folder, filename)
        base_name = os.path.splitext(filename)[0]
        output_filename = f"{base_name}-{timestamp}.webp"
        output_path = os.path.join(output_folder, output_filename)
        optimize_image(input_path, output_path, max_width, quality)
import os
import shutil

# 다운로드 폴더 경로
downloads_folder = r'C:\Users\student\Downloads'

# 각 확장자에 맞는 폴더 경로
images_folder = r'C:\Users\student\Downloads\images'
data_folder = r'C:\Users\student\Downloads\data'
docs_folder = r'C:\Users\student\Downloads\docs'
archive_folder = r'C:\Users\student\Downloads\archive'

# 폴더가 없으면 생성
os.makedirs(images_folder, exist_ok=True)
os.makedirs(data_folder, exist_ok=True)
os.makedirs(docs_folder, exist_ok=True)
os.makedirs(archive_folder, exist_ok=True)

# 다운로드 폴더 내 모든 파일 확인
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)
    
    # 파일일 경우에만 처리
    if os.path.isfile(file_path):
        # 확장자에 따른 파일 이동
        if filename.lower().endswith(('.jpg', '.jpeg')):
            shutil.move(file_path, os.path.join(images_folder, filename))
        elif filename.lower().endswith(('.csv', '.xlsx')):
            shutil.move(file_path, os.path.join(data_folder, filename))
        elif filename.lower().endswith(('.txt', '.doc', '.pdf')):
            shutil.move(file_path, os.path.join(docs_folder, filename))
        elif filename.lower().endswith('.zip'):
            shutil.move(file_path, os.path.join(archive_folder, filename))

print("파일 이동이 완료되었습니다.")

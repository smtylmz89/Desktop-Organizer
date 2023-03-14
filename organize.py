import os
import shutil

# Klasör yapısını oluştur
desktop = os.path.expanduser("~/Desktop")
folder_path = os.path.join(desktop, "categorized_folders")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Dosyaları klasörlere taşı
for filename in os.listdir(desktop):
    if filename != "organize.py" and not os.path.isdir(os.path.join(desktop, filename)):
        file_path = os.path.join(desktop, filename)
        file_extension = os.path.splitext(filename)[1][1:].lower()
        file_folder_path = os.path.join(folder_path, file_extension)
        if not os.path.exists(file_folder_path):
            os.makedirs(file_folder_path)
        shutil.move(file_path, os.path.join(file_folder_path, filename))

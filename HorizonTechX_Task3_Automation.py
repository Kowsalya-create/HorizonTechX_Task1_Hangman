import os
import shutil

source_folder = "source_images"
destination_folder = "jpg_images"

if not os.path.exists(source_folder):
    os.makedirs(source_folder)
    print("Created source_images folder. Add JPG files and run again.")
    raise SystemExit

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

files = os.listdir(source_folder)

for file in files:
    if file.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)
        print(file, "moved successfully.")

print("\nAll JPG files have been processed.")

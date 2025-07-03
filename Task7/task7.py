

from PIL import Image
import os
path = r"C:\Users\hp\OneDrive\Pictures\pictures\\"

def resize(width, height):
    files = os.listdir(path)
    
    for item in files:
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            try:
                img = Image.open(full_path)
                new_image = img.resize((width, height))
                new_file_name = os.path.join(path, 'resized-' + item)
                new_image.save(new_file_name)
                print(f"Saved: {new_file_name}")
            except Exception as e:
                print(f"Error resizing {item}: {e}")
resize(500, 500)

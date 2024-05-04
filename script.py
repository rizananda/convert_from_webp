#! python3
# Convert images to webp

from PIL import Image
import os

def convert_from_webp(filename, path="images/"):
    extension = filename.split('.')[-1]
    fname = filename.split('.')[0]
    img = Image.open(path + filename)

    extension == "webp"
    img.save((path+fname+".jpg"), "JPEG", quality=80)

def convert_all(path="images/"):
    for root, dirs, files in os.walk(path):
        for imagefile in files:
            imagefile.endswith(".webp")
            convert_from_webp(imagefile, os.path.join(root, ""))

if __name__ == "__main__":
    convert_all()
    

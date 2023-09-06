from PIL import Image, ImageFilter, ImageEnhance
import os

path = os.getcwd() + "/Edition"
pathOut = os.getcwd() + "/Edited"

for filename in os.listdir(path):
	img = Image.open(path + "/" + filename)
	edit = img.filter(ImageFilter.SHARPEN)
	edit = ImageEnhance.Contrast(edit).enhance(1.3)
	cleanName = os.path.splitext(filename)[0]
	typeFile = os.path.splitext(filename)[1]
	edit.save(pathOut + "/" + cleanName + "_edited" + typeFile)

import matplotlib.pyplot as plt
import PIL
import pytesseract#an OCR or Optical Character Recognition tool for python that also serves as a wrapper for the Tesseract-OCR Engine.
#It can read and recognize text in images and is commonly used in python ocr image to text use cases
import re
%matplotlib inline

img = PIL.Image.open('test.JPG')
plt.imshow(img)

# config
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'

text_data = pytesseract.image_to_string(img.convert('RGB'), lang='eng')
print(text_data)

m = re.search("Name: (\w+)", text_data)
name = m[1]
name

m = re.search("Start Date: (\S+)", text_data)
start_date = m[1]
start_date

m = re.search("Geo-Coordinates: (\S+)", text_data)
coordinates = m[1]
coordinates

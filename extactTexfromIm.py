import pytesseract
from PIL import Image

img = Image.open('Text.jpeg')

text = pytesseract.image_to_string(img)
print(text)
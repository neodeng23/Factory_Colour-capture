import pytesseract
from PIL import Image

img = Image.open('/Users/wts-sw/PycharmProjects/Factory_Colour-capture/111.png') #先创建image对象
text = pytesseract.image_to_string(img) #直接转化成string，更多参数可以查看文档
print(text)

import pytesseract
from PIL import Image

img = Image.open('/Users/wts-sw/Desktop/pic/1111.png') #先创建image对象
text = pytesseract.image_to_string(img, lang='eng', config='--psm 10') #直接转化成string，更多参数可以查看文档
print(text)

img2 = Image.open('/Users/wts-sw/Desktop/pic/2021-01-20-14-48-48.png.png') #先创建image对象
text2 = pytesseract.image_to_string(img2, lang='eng', config='--psm 10') #直接转化成string，更多参数可以查看文档
print(text2)

import cv2
import os
from get_color import *
from get_pos_config import *
import time, datetime
current_user = getpass.getuser()

pic_name = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".png"
os.system("screencapture /Users/" + current_user + "/Desktop/pic/" + pic_name)
time.sleep(1)
# 设定文件路径
img_path = "/Users/" + current_user + "/Desktop/pic/" + pic_name
# Read image
# img = cv2.imread(img_path)
x, y = get_win_pos()
x1, x2, y1, y2 = get_channel_config("A", x ,y)
print(x1, x2, y1, y2)

# cropImg = img[y1:y2, x1:x2]    # 裁剪【y1,y2：x1,x2】
#
# cropImg = convert_from_cv2_to_image(cropImg)
# image = cropImg.convert('RGB')
# image.show()

img = Image.open(img_path)

cropped = img.crop((x1, y1, x2, y2))  # (left, upper, right, lower)
cropped.show()
print(get_dominant_color(cropped))


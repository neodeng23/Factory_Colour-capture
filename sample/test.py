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
img = cv2.imread(img_path)

x1, x2, y1, y2 = get_channel_config("B")
print(x1, x2, y1, y2)

cropImg = img[y1:y2, x1:x2]    # 裁剪【y1,y2：x1,x2】

cropImg = convert_from_cv2_to_image(cropImg)
image = cropImg.convert('RGB')
image.show()
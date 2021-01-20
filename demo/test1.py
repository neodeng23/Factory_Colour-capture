import cv2
import os
from get_color import *
from get_pos_config import *
import time, datetime
current_user = getpass.getuser()

# pic_name = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".png"
# os.system("screencapture /Users/" + current_user + "/Desktop/pic/" + pic_name)
# time.sleep(1)
#
# img_path = "/Users/" + current_user + "/Desktop/pic/" + pic_name
#
# x, y = get_win_pos()
# x1, x2, y1, y2 = get_channel_config("A", x ,y)
# img = Image.open(img_path)


img_path = "/Users/" + current_user + "/Desktop/pic/" + "1111.png"

# cropped = img.crop((x1, y1, x2, y2))  # (left, upper, right, lower)
# cropped.show()
# print(get_dominant_color(cropped))
img = Image.open(img_path)
image = img.convert('RGB')
(r, g, b) = get_dominant_color(img)
color = recognize_color(r, g, b)
print(color)

import numpy as np
import pandas as pd
import cv2
import colorsys
from PIL import Image
import re
import pytesseract

index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('/Users/wts-sw/PycharmProjects/Factory_Colour-capture/src/colors.csv', names=index, header=None)


def convert_from_cv2_to_image(img: np.ndarray) -> Image:
    # return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    return Image.fromarray(img)


def convert_from_image_to_cv2(img: Image) -> np.ndarray:
    # return cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    return np.asarray(img)


def recognize_color(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if (d <= minimum):
            minimum = d
            cname = csv.loc[i, "color_name"]
    if cname in ["Tomato", "Bittersweet", "Salmon"]:  # 红色类
        cname = "Red"
    elif cname in ["Daffodil", "Light Khaki", "Isabelline", "Unmellow Yellow", "Yellow (Ryb)"]:  # 黄色类
        cname = "Yellow"
    elif cname in ["White", "White Smoke"]:
        cname = "White"
    elif cname in ["Medium Spring Green", "Bright Turquoise", "Medium Aquamarine", "Aquamarine"]:
        cname = "Green"
    else:
        cname = ""
    return cname


def get_dominant_color(image):
    max_score = 0.0001
    dominant_color = None
    for count, (r, g, b) in image.getcolors(image.size[0] * image.size[1]):
        # 转为HSV标准
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]
        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
        y = (y - 16.0) / (235 - 16)

        # # 忽略高亮色
        # if y > 0.9:
        #     continue
        score = (saturation + 0.1) * count

        if score > max_score:
            max_score = score
            dominant_color = (r, g, b)
    return dominant_color


def get_text(image):
    text = pytesseract.image_to_string(image, lang='eng', config='--psm 10')
    for i in ["ERROR", "PASS", "FAIL"]:
        reslist = re.findall(i, text)
        if len(reslist) != 0:
            text = i
    if text not in ["ERROR", "PASS", "FAIL"]:
            text = " "
    return text

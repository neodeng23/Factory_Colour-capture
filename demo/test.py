# _*_ coding:UTF-8 _*_
from PIL import ImageGrab
import numpy as np
from PIL import Image
import cv2


def convert_from_cv2_to_image(img: np.ndarray) -> Image:
    # return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    return Image.fromarray(img)


def convert_from_image_to_cv2(img: Image) -> np.ndarray:
    # return cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    return np.asarray(img)


# img = ImageGrab.grab()
# open_cv_image = convert_from_image_to_cv2(img)


im = ImageGrab.grab().convert('RGB')
im.save(r"/Users/wts-sw/PycharmProjects/Factory_Colour-capture/des.jpg", 'jpeg')
print("截屏完成")
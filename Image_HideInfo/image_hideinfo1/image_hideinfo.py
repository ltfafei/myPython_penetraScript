#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import cv2
import sys

'''
source_image = cv2.imread('waitang.jpg')
#设置图像的垂直尺寸、水平尺寸和通道数
h, w = source_image.shape[:2]
message = "Hello Shanghai, I'm come!"
x, y = (150, 250)
#设置字体RGB颜色
color = [100, 30, 18]
cv2.putText(source_image, message, (x, y), cv2.QT_FONT_BLACK, 3, color, thickness=5)
cv2.imwrite('result.jpg', source_image)
'''

def img_hideinfo():
    if (len(sys.argv) < 3):
        print("-----------------------------------------------")
        print(" ")
        print("Useg: python %s <path/source.png> <path/result.png>" % sys.argv[0])
        print("eg: python image_hideinfo.py c:/1.png c:/2.png")
        print(" ")
        print("-----------------------------------------------")
        return

    source_path = sys.argv[1]
    result_path = sys.argv[2]
    source_image = cv2.imread(source_path)
    h, w = source_image.shape[:2]
    message = "Flying"
    x, y = (350, 450)
    color = [100, 300, 18]
    color = [100, 300, 18]
    cv2.putText(source_image, message, (x, y), cv2.QT_FONT_BLACK, 3, color, thickness=5)
    cv2.imwrite(result_path, source_image)
    return

if (__name__ == '__main__'):
    img_hideinfo()
import cv2
import time
import numpy as np


img = cv2.imread("4target.png")
cv2.imshow("src", img)

def findLight():
    b, g, r = cv2.split(img)
    br = cv2.subtract(b, r)  # B - R
    brg = cv2.subtract(br, g)  # BR - G
    # 灰度处理,二值化
    ret, img2 = cv2.threshold(brg, 50, 255, cv2.THRESH_BINARY)
    # 寻找连通矩形
    img2, contours, hierarchy = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        # 获取最小包围矩形
        rect = cv2.minAreaRect(contours[n])
        n = n + 1
        # 中心坐标
        x, y = rect[0]
        cv2.circle(img, (int(x), int(y)), 1, (0, 0, 255), 5)
        # 长宽,总有 width>=height
        width, height = rect[1]
        # 角度:[-90,0)
        angle = rect[2]
        cv2.drawContours(img, contour, -1, (255, 255, 0), 3)
        #cv2.putText()
        print('width=', width, 'height=', height,
          'x=', x, 'y=', y, 'angle=', angle, '$$$=', str(width / height))

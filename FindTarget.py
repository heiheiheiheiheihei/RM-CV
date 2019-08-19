import time

import numpy as np

import cv2

img = cv2.imread("./TestImage/test.png")
cv2.imshow("src", img)
Light = []


def findLight():
    b, g, r = cv2.split(img)
    br = cv2.subtract(b, r)  # B - R
    brg = cv2.subtract(br, g)  # BR - G
    
    ret, img2 = cv2.threshold(brg, 50, 255, cv2.THRESH_BINARY) # 图像二值化
    
    img2, contours, hierarchy = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # 寻找连通矩形
    n = 0
    cv2.drawContours(img, contours, -1, (255, 255, 0), 3)
    cv2.imshow("src", img)
    for contour in contours:
        # 获取最小包围矩形
        rect = cv2.minAreaRect(contours[n])
        # 中心坐标
        x, y = rect[0]
        # cv2.circle(img, (int(x), int(y)), 1, (125, 125, 255), 5)
        # 长宽
        width, height = rect[1]
        # 角度:[-90,0)
        angle = rect[2]
        # cv2.drawContours(img, contour, -1, (255, 255, 0), 3)
        # cv2.putText()
        print('width=', width, 'height=', height, 'x=', x, 'y=',
              y, 'angle=', angle, '$$$=', str(width / height))
        if height > width:
            scale = height / width
        else:
            scale = width / height
            angle += 90
        if 10 > scale > 4.5:
            cv2.drawContours(img, contour, -1, (255, 255, 0), 3)
            cv2.circle(img, (int(x), int(y)), 1, (125, 125, 255), 5)
            Light.append(rect)
        n = n + 1
    #cv2.drawContours(img, Light, -1, (255, 255, 0), 3)
    cv2.imshow("result", img)


findLight()
cv2.waitKey(0)

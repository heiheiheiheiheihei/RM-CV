import cv2
import time
import numpy as np


cam = cv2.VideoCapture(0)
while(0):
    start_time = time.time()
    # 获取一帧
    ret, frame = cam.read()
    cv2.imshow('raw', frame)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    b, g, r = cv2.split(frame)
    br = cv2.subtract(b, r)  # B - R
    brg = cv2.subtract(br, g)  # BR - G
    #ret, mask = cv2.threshold(brg, 20, 255, cv2.THRESH_BINARY)

    end_time = time.time()
    #cv2.putText(mask, str(end_time - start_time), (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2)
    print(str(end_time - start_time))
    cv2.imshow('frame', brg)
    if cv2.waitKey(1) == ord('1'):
        break

while ():
    ret, img = cam.read()
    cv2.imshow("src", img)
    # 灰度处理,二值化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img2 = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

    # 寻找连通矩形
    img, contours, hierarchy = cv2.findContours(
        img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # 获取最小包围矩形
        rect = cv2.minAreaRect(contours[0])

        # 中心坐标
        x, y = rect[0]
        cv2.circle(img, (int(x), int(y)), 3, (0, 255, 0), 5)

        # 长宽,总有 width>=height
        width, height = rect[1]

        # 角度:[-90,0)
        angle = rect[2]

        cv2.drawContours(img, contour, -1, (255, 255, 0), 3)
        print('width=', width, 'height=', height,
              'x=', x, 'y=', y, 'angle=', angle)

    cv2.imshow("contour", img)
    if cv2.waitKey(1) == ord('1'):
        break


img = cv2.imread("4target.png")
cv2.imshow("src", img)
b, g, r = cv2.split(img)
br = cv2.subtract(b, r)  # B - R
brg = cv2.subtract(br, g)  # BR - G
# 灰度处理,二值化
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img2 = cv2.threshold(brg, 50, 255, cv2.THRESH_BINARY)

# 寻找连通矩形
img2, contours, hierarchy = cv2.findContours(
    img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("findcontour", img2)
n = 0
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
cv2.imshow("contour", img)
#cv2.drawContours(img,contours,-1,(0,0,255),3)
cv2.waitKey()
cv2.destroyAllWindows()

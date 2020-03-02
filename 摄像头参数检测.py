import cv2
import time
import math

mode = "BLUE"       # 填写敌方阵营的颜色，可以是 RED 和 BLUE
debug = False       # 一键开启调试模式

cam = cv2.VideoCapture(0)
ret, img = cam.read()
cv2.imshow('raw', img)

print("图像宽度：", cam.get(cv2.CAP_PROP_FRAME_WIDTH))
print("图像高度：", cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("帧率：", cam.get(cv2.CAP_PROP_FPS))
print("图像亮度：", cam.get(cv2.CAP_PROP_BRIGHTNESS))
print("图像对比度：", cam.get(cv2.CAP_PROP_CONTRAST))
print("图饱和度：", cam.get(cv2.CAP_PROP_SATURATION))
print("图像色调：", cam.get(cv2.CAP_PROP_HUE))
print("摄像头曝光：", cam.get(cv2.CAP_PROP_EXPOSURE))

while(1):
    if cv2.waitKey(1) == ord('1'):
        break

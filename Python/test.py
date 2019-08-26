import math
import time

import cv2

cam = cv2.VideoCapture(0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # 定义结构元素

sightX = 330
sightY = 245

while(True):
    timeStamp = time.time()
    # ret, img = cam.read()  # 获取一帧图像
    img = cv2.imread("./TestImage/fang.png")
    print("获取一帧图像:" + str(time.time() - timeStamp))
    blueImg, greenImg, redImg = cv2.split(img)  # 分离图像的RGB通道
    img2 = cv2.subtract(blueImg, redImg)  # B通道-R通道
    img2 = cv2.subtract(img2, greenImg)  # (B通道-R通道)-G通道
    print("只保留b通道:" + str(time.time() - timeStamp))
    ret, img2 = cv2.threshold(img2, 30, 255, cv2.THRESH_BINARY)  # 图像二值化处理
    print("二值化:" + str(time.time() - timeStamp))
    # img2 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)  # 开运算
    # img2 = cv2.dilate(img2, kernel）        #膨胀处理
    contours, hierarchy = cv2.findContours(
        img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 获取轮廓
    print("找轮廓:" + str(time.time() - timeStamp))
    # cv2.drawContours(img, contours, -1, (0, 0, 255), 2)  # 在原始图像上绘制轮廓以进行显示
    n = 0
    x = []
    y = []
    longSide = []
    shortSide = []
    angle = []  # 初始化变量
    for contour in contours:
        rect = cv2.minAreaRect(contours[n])  # 获取最小包围矩形
        xCache, yCache = rect[0]  # 获取矩形的中心坐标
        widthC, heigthC = rect[1]  # 获取矩形的长宽
        angleCache = rect[2]  # 获取矩形的角度 (-90, 0]

        if heigthC > widthC:
            if heigthC / widthC >= 2.1:  # 长宽比满足条件
                # if widthC < heigthC and heigthC / widthC >= 2.1:        #灯条是竖直放置，长宽比满足条件
                x.append(int(xCache))
                y.append(int(yCache))
                longSide.append(int(heigthC))
                # shortSide.append(widthC)
                angle.append(angleCache)
                n = n + 1  # 有效矩形计数
        else:
            if widthC / heigthC >= 2.1:  # 长宽比满足条件
                x.append(int(xCache))
                y.append(int(yCache))
                longSide.append(int(widthC))
                # shortSide.append(heigthC)
                angle.append(angleCache + 90)
                n = n + 1  # 有效矩形计数
    print("找灯条:" + str(time.time() - timeStamp))
    target = []  # 存储配对的两个灯条的编号 (L1, L2)
    locX = []
    locY = []  # 存储计算得到的中心点坐标
    dis = []  # 存储中心点与准星的距离
    pairNum = 0  # 初始化计数变量
    if n >= 2:  # 图像中找到两个以上的灯条
        for count in range(0, n):
            findCache = count + 1  # 初始化计数变量
            while findCache < n:  # 未超界，进行匹配运算
                calcCache = math.sqrt(
                    (x[findCache] - x[count]) ** 2 + (y[findCache] - y[count]) ** 2)  # 求中心点连线长
                calcCache = calcCache / \
                    (longSide[count] + longSide[findCache])  # 求快捷计算单位
                # print("·Scale:", calcCache)
                if abs(angle[count] - angle[findCache]) < 10 and (1.0 < calcCache < 1.4):  # 满足匹配条件
                    # if abs(angle[count] - angle[findCache]) < 10 and (0.8 < calcCache < 1.2 or 1.8 < calcCache < 5.2):  #满足匹配条件
                    target.append((count, findCache))
                    #loc.append((int((x[count] + x[findCache]) / 2), int((y[count] + y[findCache]) / 2)))
                    locX.append(int((x[count] + x[findCache]) / 2))
                    locY.append(int((y[count] + y[findCache]) / 2))
                    dis.append(
                        math.sqrt((locX[pairNum] - sightX) ** 2 + (locY[pairNum] - sightY) ** 2))
                    #cv2.circle(img, (locX[pairNum], locY[pairNum]), 3, (0, 0, 255), -1)
                    # 画两个圆来显示中心点的位置
                    #cv2.circle(img, (locX[pairNum], locY[pairNum]), 8, (0, 0, 255), 2)

                    pairNum = pairNum + 1  # 计数变量自增
                findCache = findCache + 1
    

        # ···在此处添加数字验证真假装甲板代码

        if pairNum != 0:
            # 寻找离准星最近的装甲板
            disCalcCache = dis[0]
            targetNum = 0  # 存储距离准星最进的装甲板编号
            for count in range(0, pairNum):
                if dis[count] < disCalcCache:
                    targetNum = count
                    disCalcCache = dis[count]
        print(disCalcCache)
    timeStamp = time.time() - timeStamp
    print("总耗时" + str(timeStamp))
    if cv2.waitKey(1) == ord('1'):
        break

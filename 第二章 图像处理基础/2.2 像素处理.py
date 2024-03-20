'''
2.2 像素处理
图像是个二维数组，行列 mage[0,0]
'''
import cv2
import numpy as np


img = np.zeros((64,64))
print(img)
img[32,5]=255
cv2.imshow("one",img)
cv2.waitKey()

# 例2.2 读一个灰度图像，并对其像素进行访问修改
def read_write():
    img = cv2.imread("./temp/save.png",cv2.IMREAD_GRAYSCALE)
    for i in range(0,50) :
        for j in range(100,500):
            img[i,j]=255
    cv2.imshow("temp1",img)
    cv2.waitKey()
# read_write()

# 例2.4 使用Numpy生成一个三维数组，用来观察三个通道值的变化
def create_color_square():
    square = np.zeros((300,300,3))
    c = 0
    for i in range(0,300):
        c = c+1 if (i+1)%100 == 0 and c<2 else c
        for j in range(0,300):
            square[i,j,c]=255
    cv2.imshow("color",square)
    cv2.waitKey()
# create_color_square()    
    

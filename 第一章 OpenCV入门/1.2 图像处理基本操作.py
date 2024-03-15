import cv2


kitty_pic = "C:\\Users\\Ad'min\\Pictures\\ico\\kitty.png"
''' 1.2.1 读取图像 '''
pic = cv2.imread(kitty_pic,cv2.IMREAD_UNCHANGED)
# 输出图像部分像素值
print( pic)


'''1.2.2 显示图像 '''
winname = "kitty"
# 1.创建窗口
cv2.namedWindow(winname)
# 2.显示窗口
cv2.imshow(winname,pic)
# 3.等待按键
# 返回按键的ASCII码 ，入参是等待时间单位毫秒 ， <= 表示无限，默认0
key = cv2.waitKey()
# ord() 函数获取ASCII码
def waitKey_test():
    pic = cv2.imread(kitty_pic)
    cv2.imshow("demo",pic)
    if key == ord('a'):
        cv2.imshow("demo_1",pic)
    key = cv2.waitKey()
# 4.销毁窗口
cv2.destroyWindow(winname)
# 5.销毁所有窗口
cv2.destroyAllWindows() 

# 1.2.3 保存图像
def savePic():
    grayscalePic = cv2.imread(kitty_pic,cv2.IMREAD_GRAYSCALE)
    isSave = cv2.imwrite("./temp/save.png",grayscalePic)

savePic()
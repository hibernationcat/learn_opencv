import numpy as np
import cv2 

'''2.3 使用numpy.array访问像素
item(行，列) itemset(索引值，新值) 修改和设置
'''


# 例 2.7 
def test2_7():
    img = np.random.randint(10,99,size = [5,5])
    print(img)
    print(img.item(3,4))
    img.itemset((3,4),111)
    img.itemset((0,0),0)
    print(img)
# test2_7()

# 例 2.9
def test2_9():
    img = cv2.imread("./temp/save.png",cv2.IMREAD_GRAYSCALE)
    x,y = img.shape
    for i in range(0,int(x/2)):
        for j in range(0,int(y/2)): 
            img.itemset((i,j),0)
    cv2.imshow("打码",img)
    key = cv2.waitKey()
    if key == ord('s'):
        cv2.destroyAllWindows()
test2_9()
             

import cv2
img = cv2.imread('sc2.jpg',cv2.IMREAD_COLOR)#读入彩色图片
cv2.imshow('image1',img)
k = cv2.waitKey(0) #键盘绑定函数, 0，那它将会无限期的等待键盘输入
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()#可以轻易删除任何我们建立的窗口,cv2.destroyWindow()，在括号内输入你想删除的窗口名。
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('sc21.png',img)
    cv2.destroyAllWindows()
cv2.namedWindow('image2',cv2.WINDOW_NORMAL)#窗口大小可调
cv2.imshow('image2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('sc22.png', img)
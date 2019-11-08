
import numpy as np
import cv2
cap = cv2.VideoCapture(0)

# 保存视频，首先需要创建一个VideoWriter对象，它的参数依次为视频文件名，视频编码格式，帧率，大小，是否彩色。
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('op1.avi',fourcc, 20.0, (640,480))#FourCC 就是一个 4 字节码，用来确定视频的编码格式。

while(cap.isOpened()):
    ret, frame = cap.read()  # # 从摄像头读取一帧，ret是表明成功与否
    if ret==True:
       # frame = cv2.flip(frame,0)   #处理得到的帧，这里将其翻转
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)  # 对捕捉到的视频帧进行处理
        # write the flipped frame
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
#waitKey(1) 中的数字代表等待按键输入之前的无效时间，单位为毫秒，在这个时间段内按键 ‘q’ 不会被记录，
# 在这之后按键才会被记录，并在下一次进入if语段时起作用。也即经过无效时间以后，
# 检测在上一次显示图像的时间段内按键 ‘q’ 有没有被按下，若无则跳出if语句段，捕获并显示下一帧图像。
#若此参数置零，则代表在捕获并显示了一帧图像之后，程序将停留在if语句段中一直等待 ‘q’ 被键入。
#在opencv中有超过150种颜色空间转换方法（震惊-_-）
#但是经常用的只有BGR-灰度图和BGR-HSV

#使用函数cv2.cvtColor(input_image ，flag)，flag是转换类型

#BGR和灰度图的转换使用 cv2.COLOR_BGR2GRAY
#BGR和HSV的转换使用 cv2.COLOR_BGR2HSV
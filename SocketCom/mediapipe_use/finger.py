import cv2
import time
import os
import math
import socket
import hand_module as handModule

# data
'''
class Data:
    def __init__(self): 
        self.x = 0
        self.y = 0
'''

# socket
address = ('127.0.0.1', 5555)  # 服务端地址和端口
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# detect
weight = 640
height = 480
cap = cv2.VideoCapture(0)
#cap.set(3,weight)
#cap.set(4,height)


detect = handModule.HandDetect(static_image_mode=False,
                max_num_hands=1,
                min_detection_confidence=0.55,
                min_tracking_confidence=0.7)

while True:
    flag,img = cap.read()
    img = cv2.flip(img,1)

    detect.initImage(img)
    img = detect.findHandsPoint()
    lm_list = detect.findPosition(img,draw=False)

    if len(lm_list[0])!=0:
        cv2.circle(img,(lm_list[0][0][1],lm_list[0][0][2]),5,(0,255,255), cv2.FILLED)
        
        cv2.circle(img,(lm_list[0][4][1],lm_list[0][4][2]),5,(255,255,0), cv2.FILLED)
        cv2.circle(img,(lm_list[0][8][1],lm_list[0][8][2]),5,(255,255,0), cv2.FILLED)
        cv2.circle(img,(lm_list[0][12][1],lm_list[0][12][2]),5,(255,255,0), cv2.FILLED)
        cv2.circle(img,(lm_list[0][16][1],lm_list[0][16][2]),5,(255,255,0), cv2.FILLED)
        cv2.circle(img,(lm_list[0][20][1],lm_list[0][20][2]),5,(255,255,0), cv2.FILLED)
     

    if len(lm_list[0])!=0:
        # distance between 0-5
        p1x = lm_list[0][0][1]
        p1y = lm_list[0][0][2]
        p2x = lm_list[0][5][1]
        p2y = lm_list[0][5][2]
        standardDistance = math.sqrt((p2x-p1x)*(p2x-p1x)+(p2y-p1y)*(p2y-p1y))
        # distance between 4-8 to control
        p3x = lm_list[0][4][1]
        p3y = lm_list[0][4][2]
        p4x = lm_list[0][8][1]
        p4y = lm_list[0][8][2]
        controlDistance = math.sqrt((p4x-p3x)*(p4x-p3x)+(p4y-p3y)*(p4y-p3y))
        # print(controlDistance/standardDistance)
        
    if len(lm_list[0])!=0:
        data = []
        data.append(str(lm_list[0][0][1]/10))
        data.append(str((height-lm_list[0][0][2])/10))
        #print(data)
        data_str = ' '.join(data)
        print(data_str)
        s.sendto(data_str.encode(), address)
            
    
    cv2.imshow('1',img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        data = "###"
        s.sendto(data.encode(), address)
        break
    
cv2.destroyAllWindows()
cap.release()
s.close()





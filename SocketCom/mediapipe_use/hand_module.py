import cv2
import mediapipe as mp
import time


class HandDetect():
    def __init__(self,
                static_image_mode=False,
                max_num_hands=2,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.65):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
                            static_image_mode,
                            max_num_hands,
                            min_detection_confidence,
                            min_tracking_confidence)
        self.mp_draw = mp.solutions.drawing_utils
        self.palm_point = []

    def initImage(self,img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # maybe high cost
        self.img = img
        self.results = self.hands.process(img_rgb)  # process frame

    def findHandsPoint(self):
        # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # self.results = self.hands.process(img_rgb)  # process frame
        if self.results.multi_hand_landmarks:
            # print(results.multi_hand_landmarks) 
            for hand_point in self.results.multi_hand_landmarks:
                for id,point in enumerate(hand_point.landmark):
                    # id:0-20
                    # point:x y z(ratio of image)
                    # print(id,point)
                    height,weight,channel = self.img.shape
                    centerx,centery = int(point.x * weight),int(point.y * height)

                    # point position of image (pixel)
                    # print(id,centerx,centery)
                    
                    if id ==0 or id == 1  or id == 5 or  id == 17:
                        self.palm_point.append((centerx,centery))
                    
                    # draw palm
                    if id == 20:
                        palm_centerx = 0
                        palm_centery = 0
                        for i in range(0,len(self.palm_point)):
                            palm_centerx += self.palm_point[i][0]
                            palm_centery += self.palm_point[i][1]
                        palm_centerx //= len(self.palm_point)
                        palm_centery //= len(self.palm_point)
                        self.palm_point = []

                        cv2.circle(self.img,(palm_centerx,palm_centery),10,(255,0,0), cv2.FILLED)

                # draw the feature point and edge
                self.mp_draw.draw_landmarks(self.img,hand_point,self.mp_hands.HAND_CONNECTIONS)
        return self.img

    def findSingleFinger(self,img,finger_number=0):
        # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # self.results = self.hands.process(img_rgb)  # process frame
        finger_list = []
        if self.results.multi_hand_landmarks:
            # print(results.multi_hand_landmarks) 
            for hand_point in self.results.multi_hand_landmarks:
                for id,point in enumerate(hand_point.landmark):
                    # id:0-20
                    # point:x y z(ratio of image)
                    # print(id,point)
                    height,weight,channel = img.shape
                    centerx,centery = int(point.x * weight),int(point.y * height)

                    # point position of image (pixel)
                    # print(id,centerx,centery)
                    
                    if id == finger_number:
                        cv2.circle(img,(centerx,centery),5,(255,255,0), cv2.FILLED)
                        finger_list.append((centerx,centery))
                # draw the feature point and edge
                # self.mp_draw.draw_landmarks(img,hand_point,self.mp_hands.HAND_CONNECTIONS)
        return finger_list
        
    def findPosition(self, img, handNo=0, draw=True):
        xList = []
        yList = []
        bbox = []
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                # print(id, cx, cy)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        if (xList and yList):
            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = xmin, ymin, xmax, ymax

            if draw:
                cv2.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20),
                (0, 255, 0), 2)

        return self.lmList, bbox



def main():
    weight = 1920
    height = 1080
    cap = cv2.VideoCapture(0)
    cap.set(3,weight)
    cap.set(4,height)
    handDetect = HandDetect(static_image_mode=False,
                max_num_hands=2,
                min_detection_confidence=0.55,
                min_tracking_confidence=0.7)

    while True:
        flag, img = cap.read()
        handDetect.initImage(img);
        img = handDetect.findHandsPoint()
        finger_list = handDetect.findSingleFinger(img,10);
        img = cv2.flip(img,1)
        
        # 检测到的所有手点，一只手=21点,each point {x,y,z}
        # print(results.multi_hand_landmarks) 
        
        
        cv2.imshow('1',img)  # 依然用cv的bgr
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
    
    cv2.destroyAllWindows()
    cap.release()



if __name__ == "__main__":
    main()

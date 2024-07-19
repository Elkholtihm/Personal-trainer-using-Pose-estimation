import cv2
import mediapipe as mp
import time
import math

class PoseDetector():

    def __init__(self, mode = False, complexity = 1, smothLm = True, segmentation = False, 
                 smoothSeg = True, DetecConf = 0.5, TrackConf = 0.5):

        self.mode = mode
        self.complexity = complexity
        self.smothLm = smothLm
        self.segmentation = segmentation
        self.smoothSeg = smoothSeg
        self.DetecConf = DetecConf
        self.TrackConf = TrackConf

        # create an instance of the class for pose
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode ,self.complexity, self.smothLm, self.segmentation, 
                                     self.smoothSeg, self.DetecConf, self.TrackConf)

        # initialize tool for drawing landmarks
        self.mpDraw = mp.solutions.drawing_utils

    def FindPose(self, img, drawn_cercle = False):
        # convert frame to the supported color 
        igmRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # process frame to exctract landmarks
        results = self.pose.process(igmRGB)
        
        self.lmlist = []
        if results.pose_landmarks:
            self.mpDraw.draw_landmarks(img, results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmlist.append([id, cx, cy])
                if drawn_cercle:
                    cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
        return img, self.lmlist
    
    def FindAngle(self, img, p1, p2, p3, draw = True):
        x1, y1 = self.lmlist[p1][1:]
        x2, y2 = self.lmlist[p2][1:]
        x3, y3 = self.lmlist[p3][1:]

        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 2)
            cv2.line(img, (x1, y1), (x3, y3), (255, 255, 0), 2)
            # p1
            cv2.circle(img, (x1, y1), 10, (255, 0, 255), 2)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), 2)
            # p2
            cv2.circle(img, (x2, y2), 10, (255, 0, 255), 2)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), 2)
            # p3
            cv2.circle(img, (x3, y3), 10, (255, 0, 255), 2)
            cv2.circle(img, (x3, y3), 15, (255, 0, 255), 2)

        # angle
        angle = math.degrees(math.atan2(y3 - y1, x3 - x1) - math.atan2(y2 - y1, x2 - x1))
        return angle

def main():
    # capturing via the webcam
    cap = cv2.VideoCapture(0)  

    # define an instance of the class 
    detector = PoseDetector()

    # initialize current time and previous time used to calculating the number of frames per second
    cTime = 0
    pTime = 0

    while True:
        # read frame and verify if its correctly read
        success, img = cap.read()

        img, lmlist = detector.FindPose(img, drawn_cercle = True)

        print(lmlist)


        # calculating number of frames per second
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 0), 2)

        # display image contaning with landmark drawn on it
        cv2.imshow('Image', img)
        cv2.waitKey(1)



     


if __name__ == "__main__": 
    main()
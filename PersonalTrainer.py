import PoseDetectionModule as pdm
import time
import cv2
import numpy as np



video_path = r'test2.mp4'

# capturing via the webcam
cap = cv2.VideoCapture(video_path)  

# define an instance of the class 
detector = pdm.PoseDetector()

# initialize current time and previous time used for calculating the number of frames per second
cTime = 0
pTime = 0

def frame_generateur(vid_path):
    cap = cv2.VideoCapture(vid_path)

    max_angle = [0, 0, 0, 0] # [angle_left_hand, angle_right_hand, angle_right_leg, angle_left_leg]
    min_angle = [360, 360, 360, 360] # [angle_left_hand, angle_right_hand, angle_right_leg, angle_left_leg]
    lms = [[13, 11, 15], [14, 12, 16], [26, 24, 28], [25, 23, 27]] # [angle_left_hand, angle_right_hand, angle_right_leg, angle_left_leg]

    while cap.isOpened(): # while vid open
        success, img = cap.read()
        if not success:
            break

        img, lmlist = detector.FindPose(img)

        # get the maximum angle
        if len(lmlist) != 0:
            for lm, i in zip(lms, [0, 1, 2, 3]):
                angle = detector.FindAngle(img, lm[0], lm[1], lm[2])
                if angle < 0:
                    angle += 360
                if max_angle[i] < angle:
                    max_angle[i] = angle
                if min_angle[i] > angle:
                    min_angle[i] = angle
    cap.release()    
    return max_angle, min_angle
        




max_angle, min_angle = frame_generateur(vid_path=video_path)
print(max_angle, min_angle)
counter = 0
while cap.isOpened():
    # read frame and verify if its correctly read
    success, img = cap.read()
    if not success:
        break
    
    # detect position and get landmarks
    img, lmlist = detector.FindPose(img)

    # get angle and display it
    lms = [[13, 11, 15], [14, 12, 16], [26, 24, 28], [25, 23, 27]] 
    if len(lmlist) != 0:
        for lm in lms:
            if lm == lms[0]:
                angle = detector.FindAngle(img, lm[0], lm[1], lm[2])
                if angle < 0:
                    angle += 360
                cv2.putText(img, f'{int(angle)}', (lmlist[lm[0]][1] + 50, lmlist[lm[0]][2] - 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)

        # we work only on hands (the same thing for the other)
        bar_level = np.interp(angle, [min_angle[0] + 10, max_angle[0] - 10], [100, 340])
        counter_level = np.interp(angle, [min_angle[0], max_angle[0]], [100, 340])
        if counter_level in [100, 340]:
            counter += 1
        
        # display bar and counter 
        cv2.rectangle(img, (600, 100), (630, 340), (255, 0, 255), 1)
        cv2.rectangle(img, (600, int(bar_level)), (630, 340), (255, 0, 255), cv2.FILLED)
        cv2.rectangle(img, (590, 60), (630, 90), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, f'{counter}', (605, 80), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)

    # calculating number of frames per second
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'fps : {int(fps)}', (10, 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)

    # display image contaning with landmark drawn on it
    cv2.imshow('Image', img)
    cv2.waitKey(1)
cap.release() 
import cv2
import mediapipe as mp
import time


# capturing via the webcam
cap = cv2.VideoCapture('test.mp4')

# create an instance of the class for pose
mpPose = mp.solutions.pose
pose = mpPose.Pose()

# initialize tool for drawing landmarks
mpDraw = mp.solutions.drawing_utils


# initialize current time and previous time used to calculating the number of frames per second
cTime = 0
pTime = 0

while True:
    # read frame and verify if its correctly read
    success, img = cap.read()

    # convert frame to the supported color 
    igmRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # process frame to exctract landmarks
    results = pose.process(igmRGB)
    print(results)

    # drawn a circle around each landmark
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)


    # calculating number of frames per second
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 0), 2)

    # display image contaning with landmark drawn on it
    cv2.imshow('Image', img)
    cv2.waitKey(1)

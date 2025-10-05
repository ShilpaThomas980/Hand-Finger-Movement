# Creating points for hands

import cv2
import mediapipe as mp

# select the solution I want to use
handSolution = mp.solutions.hands
hands = handSolution.Hands()

# Opening Camera (0 for default camera)
videoCap = cv2.VideoCapture(0)
# Reading Image
success, img = videoCap.read()

# Showing Image on seperate window (only if read was successfull)
if success:
    # recognize hands from out image
    recHands = hands.process(img)
    if recHands.multi_hand_landmarks:
        for hand in recHands.multi_hand_landmarks:
            # draw the dots on each our image for visual help
            for datapoint_id, point in enumerate(hand.landmark):
                h, w, c = img.shape
                x, y = int(point.x * w), int(point.y * h)
                cv2.circle(img, (x, y), 10, (255, 0, 255),cv2.FILLED)
    cv2.imshow("CamOutput", img)
    cv2.waitKey(1)
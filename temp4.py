# Computer's Volume (sound) control
# Using distance between thumb and index finger

import cv2
import mediapipe as mp
import time
from subprocess import call
import numpy as np
import math

# Opening Camera (0 for default camera)
videoCap = cv2.VideoCapture(0)

# FPS variables
lastFrameTime = 0 # prev_time
frame = 0
max_diff = 20
min_diff = 200

# MediaPipe setup
handSolution = mp.solutions.hands
hands = handSolution.Hands()
mp_draw = mp.solutions.drawing_utils

# Volume Control Variables
INDEX_FINGER_IDX = 8
THUMB_IDX = 4
VOLUME_UPDATE_INTERVAL = 15

while True:
    frame += 1

    # Reading Image
    success, img = videoCap.read()
    if not success:
        continue

    # Flip the image horizontally for a mirror effect (optional)
    img = cv2.flip(img, 1)
    # convert BGR to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

    # recognize hands from out image
    recHands = hands.process(img_rgb)

    # Draw dots if hands are detected
    if recHands.multi_hand_landmarks:
        for hand in recHands.multi_hand_landmarks:
            # draw the dots on each our image for visual help
            for datapoint_id, point in enumerate(hand.landmark):
                h, w, c = img.shape
                x, y = int(point.x * w), int(point.y * h)
                cv2.circle(img, (x, y), 5, (255, 0, 255),cv2.FILLED)

        # Volume control
        if frame % VOLUME_UPDATE_INTERVAL == 0:
            thumb_y = hand.landmark[THUMB_IDX].y
            index_y = hand.landmark[INDEX_FINGER_IDX].y
            distance = thumb_y * h - index_y * h

            # Calibrate min and max difference
            min_diff = np.minimum(distance + 50, min_diff)
            max_diff = np.maximum(distance, max_diff)

            # change volume
            call(["osascript -e 'set volume output volume {}'".format(
                    np.clip(
                        (distance/(max_diff - min_diff)*100), 0, 100))]
                ,shell=True)

            frame = 0

    # Calculate FPS
    thisFrameTime = time.time() # curr_time
    fps = 1 / (thisFrameTime - lastFrameTime)
    lastFrameTime = thisFrameTime

    # Display FPS on image
    cv2.putText(img, f'FPS:{int(fps)}', (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("CamOutput", img)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoCap.release()
cv2.destroyAllWindows()
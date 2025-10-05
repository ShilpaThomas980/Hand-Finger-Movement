# Creating points for hands - moving hands with pink dots


import cv2
import mediapipe as mp

# select the solution I want to use
handSolution = mp.solutions.hands
hands = handSolution.Hands()
mp_draw = mp.solutions.drawing_utils

# Opening Camera (0 for default camera)
videoCap = cv2.VideoCapture(0)

while True:
    # Reading Image
    success, img = videoCap.read()
    if not success:
        continue

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

    # Show the frame
    cv2.imshow("CamOutput", img)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoCap.release()
cv2.destroyAllWindows()
# This is a sample Python script.
# Computer's Volume (sound) control
# Using distance between thumb and index finger

import cv2
import mediapipe as mp
from volume import control_volume
from fps import calculate_fps
from accuracy import calculate_accuracy
from hand_detection import detect_and_draw_hands
from shape_manager import ShapeManager

# Opening Camera (0 for default camera)
videoCap = cv2.VideoCapture(0)
if not videoCap.isOpened():
    print("❌ Could not open webcam")
    exit()

# Variables for accuracy
finger_positions = []

# ----- Setup Managers ---------
shape_manager = ShapeManager()

while True:
    # Reading Image
    success, img = videoCap.read()
    if not success:
        continue

    # Flip the image for a mirror effect (optional)
    img = cv2.flip(img, 1)

    # Calculate FPS
    calculate_fps(img)

    # Hand Detection + drawing
    recHands = detect_and_draw_hands(img, finger_positions)

    # Volume control (only if hand detected)
    if recHands.multi_hand_landmarks:
        for hand in recHands.multi_hand_landmarks:
            control_volume(hand, img, 0)

    # Shape display and accuracy handling
    shape_manager.update(img, finger_positions)

    

    # # Draw target path
    # for tx, ty in target_path_points:
    #     cv2.circle(img, (tx, ty), 2, (0, 255, 255), -1)
    #
    # # Calculate the accuracy in real-time
    # accuracy_score = calculate_accuracy(finger_positions, target_path_points)
    # cv2.putText(img, f'Accuracy:{int(accuracy_score)}', (10, 120),
    #             cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show the frame
    cv2.imshow("CamOutput", img)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoCap.release()
cv2.destroyAllWindows()


import cv2
import mediapipe as mp

# MediaPipe setup
handSolution = mp.solutions.hands
hands = handSolution.Hands(
    model_complexity=0,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)
mp_draw = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles


def detect_and_draw_hands(img, finger_positions):
    """
    Detects hands and draws landmarks with Mediapipe's styled colors.
    Also updates finger_positions list with index fingertip coords.
    """
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    recHands = hands.process(img_rgb)

    if recHands.multi_hand_landmarks:
        for hand in recHands.multi_hand_landmarks:
            # Draw landmarks with nice colors (default Mediapipe styling)
            mp_draw.draw_landmarks(
                image=img,
                landmark_list=hand,
                connections=mp.solutions.hands.HAND_CONNECTIONS,
                landmark_drawing_spec=mp_styles.get_default_hand_landmarks_style(),
                connection_drawing_spec=mp_styles.get_default_hand_connections_style(),
            )

            # Save index fingertip (landmark 8) to finger_positions
            h, w, c = img.shape
            idx_finger = hand.landmark[8]
            x, y = int(idx_finger.x * w), int(idx_finger.y * h)
            finger_positions.append((x, y))

    return recHands

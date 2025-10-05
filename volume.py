import math
import cv2
import numpy as np
from subprocess import call

# Volume Control Variables
INDEX_FINGER_IDX = 8
THUMB_IDX = 4
VOLUME_UPDATE_INTERVAL = 15

frame_counter = 0
current_volume = 0 # store the last calculated volume
max_diff = 20
min_diff = 200

def control_volume(hand, img, frame):
    """
    controls system volume based on thumb-index distance
    and draws volume on screen.
    Returns updated frame_counter, min_diff, max_diff
    """
    global min_diff, max_diff, frame_counter, current_volume
    frame_counter += 1

    # Volume control
    h, w, _ = img.shape

    thumb_x, thumb_y = int(hand.landmark[THUMB_IDX].x * w), int(hand.landmark[THUMB_IDX].y * h)
    index_x, index_y = int(hand.landmark[INDEX_FINGER_IDX].x * w), int(hand.landmark[INDEX_FINGER_IDX].y * h)

    # Calculate Euclidean Distance
    distance = math.hypot(index_x - thumb_x, index_y - thumb_y)

    # Calibrate min and max diff
    min_diff = min(distance, min_diff)
    max_diff = max(distance, max_diff)

    # Map distance -> 0-100 volume
    if frame % VOLUME_UPDATE_INTERVAL == 0 and max_diff > min_diff:
        current_volume = np.clip((distance - min_diff) /
                         (max_diff - min_diff) * 100, 0, 100)

        # ---- Windows System Volume using nircmd -----
        # nircmd.exe must be installed & put in same folder
        call(f"nircmd.exe setsysvolume {int(current_volume * 655.35)}", shell=True)

    # show volume on screen
    cv2.putText(img, f'Vol:{int(current_volume)}', (10, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)


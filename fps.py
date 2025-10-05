import cv2
import time

# FPS variables
lastFrameTime = 0 # prev_time

def calculate_fps(img):
    """
    This Find frame per second.
    Return the fps on screen.
    """
    global lastFrameTime
    # Calculate FPS
    thisFrameTime = time.time()  # curr_time
    fps = 1 / (thisFrameTime - lastFrameTime + 1e-6) # avoid division by 0
    lastFrameTime = thisFrameTime
    cv2.putText(img, f'FPS:{int(fps)}', (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    return lastFrameTime
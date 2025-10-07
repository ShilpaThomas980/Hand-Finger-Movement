import cv2
import time
from accuracy import calculate_accuracy

class AccuracyBox:
    def __init__(self):
        self.show_box = False
        self.start_time = 0
        self.accuracy = 0
        self.countdown = 3

    def start(self, finger_positions, target_path_points):
        """
        Call this when the 8-second shape display ends.
        Calculates mean accuracy and starts the 3-second display.
        """
        self.accuracy = calculate_accuracy(finger_positions, target_path_points)
        self.show_box = True
        self.start_time = time.time()

    def update(self, img):
        """
        Draw the small box with accuracy and countdown.
        Returns True if still showing, False if finished 3-second display.
        """
        if not self.show_box:
            return False

        elapsed = time.time() - self.start_time  # Correct elapsed time
        if elapsed > self.countdown:
            self.show_box = False
            return False

        height, width, _ = img.shape

        # Box coordinates
        box_w, box_h = 320, 120
        box_x, box_y = width//2 - box_w//2, height//2 - box_h//2

        # Draw filled rectangle with transperancy
        overlay = img.copy()
        cv2.rectangle(overlay, (box_x, box_y), (box_x+box_w, box_y+box_h),
                      (40, 40, 40), -1)
        alpha = 0.75
        cv2.addWeighted(overlay, alpha, img, 1-alpha, 0, img)

        # Accuracy text
        cv2.putText(img, f"Accuracy: {int(self.accuracy)}%",
                    (box_x + 30, box_y + 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Countdown for next shape (bottom - right corner of the box)
        countdown_value = int(self.countdown - elapsed) + 1
        cv2.putText(img, f"Next shape in: {countdown_value}",
                    (box_x + box_w - 230, box_y + box_h - 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        return True
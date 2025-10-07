# ---- SHAPE MANAGER .PY CODE

import cv2
import time
import shapes
from accuracy import calculate_accuracy

# -------------- Shape Manager Class ---------------
class ShapeManager:
    def __init__(self):
        # List of shape functions
        self.shape_functions = [
            shapes.circle,
            shapes.line,
            shapes.triangle,
            shapes.square
        ]

        self.shape_index = 0
        self.target_path_points = self.shape_functions[self.shape_index]()
        self.last_switch_time = time.time()
        self.show_shape = False
        self.countdown_start = time.time()

    def update(self, img, finger_positions):
        """
        Handles shape switching, countdown, and drawing.
        Returns None
        """
        current_time = time.time()
        elapsed = current_time - self.last_switch_time
        height, width, _ = img.shape

        # ----------- Countdown Phase ---------------
        if not self.show_shape:
            countdown_elapsed = current_time - self.countdown_start
            countdown_value = 3 - int(countdown_elapsed)
            if countdown_value > 0:
                cv2.putText(img, str(countdown_value),
                            (width // 2 - 40, height // 2),
                            cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 5)
            else:
                # Countdown finished -> show shape
                self.show_shape = True
                self.last_switch_time = time.time()

        # ------------ Shape Display Phase -----------
        elif elapsed <= 8:
            # Draw target Shape
            for tx, ty in self.target_path_points:
                cv2.circle(img, (tx, ty), 2, (0, 255, 255), -1)

            # Calculate accuracy
            accuracy_score = calculate_accuracy(finger_positions, self.target_path_points)
            cv2.putText(img, f'Accuracy:{int(accuracy_score)}', (10, 120),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # --------- Switch to Next Shape ------------
        else:
            self.shape_index = (self.shape_index + 1) % len(self.shape_functions)
            self.target_path_points = self.shape_functions[self.shape_index]()
            self.show_shape = False
            self.countdown_start = time.time()
            finger_positions.clear()  # reset tracking





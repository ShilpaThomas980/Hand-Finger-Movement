# ---------- Open webcam
import cv2
cap = cv2.VideoCapture(0)
while True:
    success, frame = cap.read()
    if not success:
        break
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


# ------------- Flip the frame into mirror effect
import cv2

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break
    # flip
    flipped = cv2.flip(frame, 1)

    cv2.imshow("Mirror Effect", flipped)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


# ------------- Grayscale Image
import cv2

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Grayscale Frame", gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# -------------- A Red circle in center

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    h, w, _ = frame.shape
    center = (w // 2, h // 2)

    cv2.circle(frame, center, 50, (0, 0, 255), 3)

    cv2.imshow("Red Circle Center", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# ------------ Random Rectangle
import random
import cv2
cap = cv2.VideoCapture(0)
while True:
    success, frame = cap.read()
    if not success:
        break

    h, w, _ = frame.shape
    x1, y1 = random.randint(0, w-100), random.randint(0, h-100)
    x2, y2 = x1 + 100, y1 + 100

    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

    cv2.imshow("Random Rectangle", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

# --------------

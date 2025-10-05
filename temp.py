# First try, what will it show me? - Reading an Image
import cv2

# opening camera (0 for our default camera)
videoCap = cv2.VideoCapture(0)
# reading image
success, img = videoCap.read()
# showing image on seperate window (only if read was successfull)
if success:
    cv2.imshow("CamOutput", img)
    cv2.waitKey(1)
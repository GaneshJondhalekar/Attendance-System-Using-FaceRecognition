import cv2
camera=cv2.VideoCapture(0)
while True:
            i, image =camera.read()
            cv2.imshow("Camera", image)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

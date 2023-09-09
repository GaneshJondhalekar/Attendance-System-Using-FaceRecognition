import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def Add_photo_sample(self,roll=0):
            self.camera=cv2.VideoCapture("http://192.168.43.87:8080/video")
            #self.camera = cv2.VideoCapture("Shala__2_Full_marathi_Movie___2016___शाळा_2.mp4")
            count = 0
            while True:
                i, self.image = self.camera.read()

                # --------------------------------------------------
                self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
                self.faces = face_cascade.detectMultiScale(self.gray, 1.5, 2)
                for (x, y, w, h) in self.faces:
                    # To draw a rectangle in a face
                    cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 255, 0), 2)
                cv2.imshow("Camera", self.image)
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    break

                if count >= 10:
                    break
                count += 1
                cv2.imwrite("dataset/student." + str(roll) +"."+str(count) +".jpg", self.gray)

            self.camera.release()
            cv2.destroyAllWindows()
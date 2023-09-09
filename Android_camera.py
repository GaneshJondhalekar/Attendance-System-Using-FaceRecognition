
import cv2
import time
from PIL import Image
import face_recognition
import numpy as np
import os
from tkinter import messagebox
import psycopg2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class Camera:

    def Add_photo_sample(self,roll=0):
            self.camera=cv2.VideoCapture("http://192.168.43.254:8080/video")
            font = cv2.FONT_HERSHEY_SIMPLEX
            count=5
            while True:
                i, self.image = self.camera.read()

                # --------------------------------------------------
                self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
                self.faces = face_cascade.detectMultiScale(self.gray, 1.5, 2)
                for (x, y, w, h) in self.faces:
                    # To draw a rectangle in a face
                    cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 255, 0), 2)
                check=False
                cv2.imshow("Camera", self.image)
                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    break

                if key==ord('c'):
                    cv2.imwrite("dataset/student." + str(roll) +".jpg", self.image)
                    check=True
                    break

            self.camera.release()
            cv2.destroyAllWindows()
            self.img = face_recognition.load_image_file("dataset/student.{}.jpg".format(roll))
            self.encoding = face_recognition.face_encodings(self.img)[0]
            if check:
                dbname = 'ganesh'
                dbuser = 'postgres'
                dbserver = 'localhost'
                dbport = '5432'
                dbpass = '1234'

                conn = psycopg2.connect(user=dbuser, password=dbpass, host=dbserver, database=dbname)
                cursor = conn.cursor()
                e = list(self.encoding)

                roll=int(roll)
                query = '''insert into Student(id,encoding) values(%s,%s);'''
                cursor.execute(query, (roll,e))
                messagebox.showinfo("Success", "Sample added successfully")
                conn.commit()
                cursor.close()
                conn.close()




    def Trainer(self):

        # Path for face image database
        path = 'dataset'
        detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        recognizer =cv2.face.LBPHFaceRecognizer_create()

        # function to get the images and label data
        def getImagesAndLabels(path):
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
            faceSamples = []
            ids = []
            for imagePath in imagePaths:
                PIL_img = Image.open(imagePath).convert('L')  # grayscale
                img_numpy = np.array(PIL_img, 'uint8')
                id = int(os.path.split(imagePath)[-1].split(".")[-3])
                print(id)
                faces = detector.detectMultiScale(img_numpy)
                for (x, y, w, h) in faces:
                    faceSamples.append(img_numpy[y:y + h, x:x + w])
                    ids.append(id)
            return faceSamples, ids

        print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
        faces, ids = getImagesAndLabels(path)
        print(ids,faces)


        recognizer.train(faces, np.array(ids))
        # Save the model into trainer/trainer.yml
        recognizer.write('trainer/trainer.yml')
        # Print the numer of faces trained and end program
        print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))

    def recognizer(self):
        import cv2
        import numpy as np
        import os
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer/trainer.yml')
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath)
        font = cv2.FONT_HERSHEY_SIMPLEX
        # iniciate id counter
        id = 0
        # names related to ids: example ==> Marcelo: id=1,  etc
        names = ['Desai', 'Amar', 'Ajit', 'Ganesh', 'Sourabh', 'Omkar']
        # Initialize and start realtime video capture
        cam = cv2.VideoCapture("http://192.168.43.254:8080/video")
        cam.set(3, 640)  # set video widht
        cam.set(4, 480)  # set video height
        # Define min window size to be recognized as a face
        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)
        while True:
            ret, img = cam.read()
            #img = cv2.flip(img, -1)  # Flip vertically
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),
            )
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

                # If confidence is less them 100 ==> "0" : perfect match
                if (confidence < 100):
                    print(id)
                    id = names[id]
                    confidence = "  {0}%".format(round(100 - confidence))
                else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))

                cv2.putText(
                    img,
                    str(id),
                    (x + 5, y - 5),
                    font,
                    1,
                    (255, 255, 255),
                    2
                )
                cv2.putText(
                    img,
                    str(confidence),
                    (x + 5, y + h - 5),
                    font,
                    1,
                    (255, 255, 0),
                    1
                )

            cv2.imshow('camera', img)
            k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
            if k == 27:
                break
        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()


#c=Camera()
#c.Add_photo_sample(9999)
#c.Trainer()
#c.recognizer()

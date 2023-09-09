import face_recognition
from PIL import Image
import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
import psycopg2
from tkinter import messagebox

class Matching:
    def Detection(self):
        self.camera = cv2.VideoCapture("http://192.168.43.254:8080/video")
        self.camera.set(3, 640)  # set Width
        self.camera.set(4, 480)  # set Height
        while True:
            i, self.image = self.camera.read()

            self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.faces = face_cascade.detectMultiScale(
                self.gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(20, 20)
            )
            for (x, y, w, h) in self.faces:
                # To draw a rectangle in a face
                cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 0, 0), 5)
                roi_gray = self.gray[y:y + h, x:x + w]
                roi_color = self.image[y:y + h, x:x + w]
            cv2.imshow("Camera", self.image)
            key = cv2.waitKey(1) & 0xFF
            check=False
            if key == ord("q"):
                break

            if key == ord('c'):
                cv2.imwrite("dataset/Attendance/students.jpg", self.image)
                self.Attendance()

        self.camera.release()
        cv2.destroyAllWindows()

        #---------------------------------------------------------------------------------------------------------------
    def Attendance(self):
        print("hii")
        dbname = 'ganesh'
        dbuser = 'postgres'
        dbserver = 'localhost'
        dbport = '5432'
        dbpass = '1234'

        conn = psycopg2.connect(user=dbuser, password=dbpass, host=dbserver, database=dbname)
        cursor = conn.cursor()

        # Adding image
        image = face_recognition.load_image_file("dataset/Attendance/students.jpg")

        # Capture faces and it locations
        e = face_recognition.face_locations(image)
        j = 0
        count = 0
        for i in e:
            j += 1
            top, right, bottom, left = i
            image1 = image[top:bottom, left:right]
            img = Image.fromarray(image1)  # create image using array interface
            img.save("s{}.jpg".format(j))
            images = face_recognition.load_image_file("s{}.jpg".format(j))
            e1 = face_recognition.face_encodings(images)[0]

            fetch = '''select * from Student;'''
            cursor.execute(fetch)
            e2 = cursor.fetchall()

            for e2 in e2:
                e3 = int(e2[0])
                e4= np.array(e2[1])
                check = face_recognition.compare_faces([e1], e4)
                if True in check:
                    count+=1
                    cursor.execute("iNSERT INTO attendence(id,attendence) VALUES(%s,%s);", (e3, True))
                    continue
       # messagebox.showinfo("Attemndance","Present student {}".format(count))


        conn.commit()
        cursor.close()
        conn.close()

m=Matching()
m.Detection()

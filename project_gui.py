from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from time import sleep
from Android_camera import *
from tkinter import messagebox


class Registration:
    def Student(self):
        c=Camera()
        self.reg_window = Tk()
        self.reg_window.geometry('600x600')
        self.reg_window.title("Student Registration")
        self.canvas=Canvas(self.reg_window,width=500,height=500,bg='white')
        self.canvas.pack()
        self.student_label=Label(self.reg_window,text='Student Registration')
        self.student_label.place(x=225,y=10)
        self.student_name = Label(self.reg_window, text='Student Name : ')
        self.Rollno = Label(self.reg_window, text='Roll No : ')
        self.student_name.place(x=60, y=60)
        self.Rollno.place(x=60, y=90)
        self.username = Entry(self.reg_window)
        self.roll = Entry(self.reg_window)
        self.username.place(x=180, y=60)
        self.roll.place(x=180, y=90)
        self.variable = StringVar(self.reg_window)
        self.dpt=Label(self.reg_window,text='Department :')
        self.dpt.place(x=60,y=120)
        self.variable.set("CSE")
        self.department=OptionMenu(self.reg_window, self.variable, "CSE", "Mechanical", "Civil","Electronics")
        self.department.place(x=180,y=120)
        self.phone = Label(self.reg_window, text='Phone No :')
        self.phone.place(x=60, y=160)
        self.phone_no = Entry(self.reg_window)
        self.phone_no.place(x=180, y=160)
        self.gmail = Label(self.reg_window, text='Gmail :')
        self.gmail.place(x=60, y=190)
        self.mail = Entry(self.reg_window)
        self.mail.place(x=180, y=190)
        self.submit=Button(self.reg_window,text='Submit',command=self.SubmitS)
        self.submit.place(x=250,y=250)
        self.photo_sample=Button(self.reg_window,text='Add photo Sample',command=lambda :c.Add_photo_sample(self.roll.get()))
        self.photo_sample.place(x=250,y=350)
        self.reg_window.mainloop()

    def Teacher(self):
        self.reg_window = Tk()
        self.reg_window.geometry('600x600')
        self.reg_window.title("Teacher Registration")
        self.canvas=Canvas(self.reg_window,width=500,height=500,bg='white')
        self.canvas.pack()
        self.teacher_label=Label(self.reg_window,text='Teacher Registration')
        self.teacher_label.place(x=225,y=10)
        self.teacher_name = Label(self.reg_window, text='Teacher Name : ')
        self.id = Label(self.reg_window, text='ID : ')
        self.teacher_name.place(x=60, y=60)
        self.id.place(x=60, y=90)
        self.username = Entry(self.reg_window)
        self.ID = Entry(self.reg_window)
        self.username.place(x=180, y=60)
        self.ID.place(x=180, y=90)
        self.variable = StringVar(self.reg_window)
        self.dpt=Label(self.reg_window,text='Department :')
        self.dpt.place(x=60,y=120)
        self.variable.set("CSE")
        self.department=OptionMenu(self.reg_window, self.variable, "CSE", "Mechanical", "Civil","Electronics")
        self.department.place(x=180,y=120)
        self.phone = Label(self.reg_window, text='Phone No :')
        self.phone.place(x=60, y=160)
        self.phone_no = Entry(self.reg_window)
        self.phone_no.place(x=180, y=160)
        self.gmail = Label(self.reg_window, text='Gmail :')
        self.gmail.place(x=60, y=190)
        self.mail = Entry(self.reg_window)
        self.mail.place(x=180, y=190)
        self.password=Label(self.reg_window,text="Password")
        self.password.place(x=60, y=220)
        self.password1 = Entry(self.reg_window, show='*')
        self.password1.place(x=180, y=220)
        self.submit=Button(self.reg_window,text='Submit',command=self.SubmitT)
        self.submit.place(x=250,y=250)
        self.reg_window.mainloop()
    def SubmitS(self):
        import psycopg2

        dbname = 'ztpeoaeg'
        dbuser = 'ztpeoaeg'
        dbserver = 'rajje.db.elephantsql.com'
        dbport = '5432'
        dbpass = '6CJMqjVNVzdHoOwADIE0MgaBVutwQTLl'

        conn = psycopg2.connect(database=dbname, user=dbuser, password=dbpass, host=dbserver, port=dbport)

        cursor = conn.cursor()

        value1 = self.roll.get()
        value2 = self.variable.get()
        value3 =self.username.get()
        value4 = self.mail.get()
        value5 = self.phone_no.get()

        sql = """INSERT INTO registration(ID,DEPT,NAME,EMAIL,PHONE)
                     VALUES(%s,%s,%s,%s,%s)"""

        cursor.execute(sql, (value1, value2, value3, value4, value5))
        conn.commit()
        conn.close()

    def SubmitT(self):
        import psycopg2

        dbname = 'ztpeoaeg'
        dbuser = 'ztpeoaeg'
        dbserver = 'rajje.db.elephantsql.com'
        dbport = '5432'
        dbpass = '6CJMqjVNVzdHoOwADIE0MgaBVutwQTLl'

        conn = psycopg2.connect(database=dbname, user=dbuser, password=dbpass, host=dbserver, port=dbport)

        cursor = conn.cursor()

        value1 = self.ID.get()
        value2 = self.variable.get()
        value3 =self.username.get()
        value4 = self.mail.get()
        value5 = self.phone_no.get()
        value6= self.password1.get()

        sql = """INSERT INTO TeacherRegistration(ID,DEPT,NAME,EMAIL,PHONE,PASSWORD)
                     VALUES(%s,%s,%s,%s,%s,%s)"""

        cursor.execute(sql, (value1, value2, value3, value4, value5,value6))
        conn.commit()
        conn.close()





class Gui:
    def __init__(self,root_window):
        root_window.geometry("1500x800")
        root_window.title("Face Recognition")
        self.canvas1 = Canvas(root_window, width=1500, height=820)
        self.canvas1.pack()
        self.image = ImageTk.PhotoImage(Image.open("hd_water_drop.jpg"))
        self.canvas1.create_image(350, 0, anchor=NW, image=self.image)
        self.start_button = Button(root_window, text="Start", width=10, height=3, bg="green", command=self.run_progressbar)
        self.start_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.progressbar = ttk.Progressbar(root_window, orient=HORIZONTAL, length=1400,mode='determinate')
        self.progressbar.place(x=50,y=600)



        #self.root_window.after(1200,self.OpenApp())

    def progress(self,currentValue):
        self.progressbar["value"] = currentValue

    def OpenApp(self):
            c=Camera()
            r=Registration()
            self.progressbar.destroy()
            self.start_button.destroy()
            self.background = ImageTk.PhotoImage(Image.open("facial_recognitio.jpg"))
            self.canvas1.create_image(0,0, anchor=NW, image=self.background)
            self.image = ImageTk.PhotoImage(Image.open("images.jpeg"))
            self.button1=Button(root_window,text="",image=self.image,width=400,height=360,command=r.Student)
            self.button1.place(x=20,y=20)
            self.image1 = ImageTk.PhotoImage(Image.open("images 1.jpeg"))
            self.button2 = Button(root_window, text="", image=self.image1,width=400,height=370)
            self.button2.place(x=460, y=20)
            self.button3 = Button(root_window, text="", image=self.image, width=400, height=370)
            self.button3.place(x=900, y=20)
            self.button4 = Button(root_window, text="", image=self.image1, width=400, height=370,command=r.Teacher)
            self.button4.place(x=20, y=420)
            self.image5 = ImageTk.PhotoImage(Image.open("images.png"))
            self.button5 = Button(root_window, text="", image=self.image5, width=400, height=370,command=c.recognizer)
            self.button5.place(x=460, y=420)
            self.button6 = Button(root_window, text="", image=self.image1, width=400, height=370,command=root_window.destroy)
            self.button6.place(x=900, y=420)

    def Login(self):
        self.progressbar.destroy()
        self.start_button.destroy()
        self.canvas1.destroy()
        self.canvas1=Canvas(root_window,width=600,height=400,bg="white")
        self.canvas1.place(x=450,y=200)
        self.username = Label(root_window, text='Username: ')  # More labels
        self.password = Label(root_window, text='Password: ')  # ^
        self.username.place(x=500,y=300)
        self.password.place(x=500,y=380)
        self.username1 = Entry(root_window)  # The entry input
        self.password1 = Entry(root_window, show='*')
        self.username1.place(x=700,y=300)
        self.password1.place(x=700,y=350)
        self.login = Button(root_window, text="Login",command=self.authentication)
        self.login.place(x=580, y=420)


    def run_progressbar(self):
        self.progressbar['maximum']=100
        for i in range(101):
            sleep(0.001)
            self.progressbar['value']=i
            self.progressbar.update()
        self.Login()

    def authentication(self):
        username = self.username1.get()
        password = self.password1.get()
        email=''
        pas=''
        check=False
        import psycopg2
        dbname = 'ztpeoaeg'
        dbuser = 'ztpeoaeg'
        dbserver = 'rajje.db.elephantsql.com'
        dbport = '5432'
        dbpass = '6CJMqjVNVzdHoOwADIE0MgaBVutwQTLl'

        conn = psycopg2.connect(database=dbname, user=dbuser, password=dbpass, host=dbserver, port=dbport)

        cursor = conn.cursor()
        sql = """SELECT * FROM TeacherRegistration """
        cursor.execute(sql)
        records = cursor.fetchall()
        for records in records:
            email = records[3]
            pas =records[5]
            if username == email and password == pas:
                check=True
                self.OpenApp()
                break

        if check==False:
            messagebox.showerror("Error","Invalid Username or password")



        conn.commit()
        conn.close()

root_window=Tk()
start=Gui(root_window)
root_window.mainloop()





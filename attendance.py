import tkinter as tk
from tkinter import *
import os
import pyttsx3
from PIL import ImageTk, Image
import takeImage
import trainImage
import automaticAttedance
import show_attendance

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = "TrainingImageLabel/Trainner.yml"
trainimage_path = "TrainingImage"
if not os.path.exists(trainimage_path):
    os.makedirs(trainimage_path)

studentdetail_path = "StudentDetails/studentdetails.csv"
attendance_path = "Attendance"

# Initialize main window
window = tk.Tk()
window.title("Face recognizer")
window.geometry("1280x720")
window.configure(background="black")

# Error screen handling
def del_sc1():
    global sc1
    sc1.destroy()

def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")  # Ensure the .ico file is available in the working directory
    sc1.title("Warning!!")
    sc1.configure(background="black")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="white",
        bg="black",
        font=("times", 20, "bold"),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="white",
        bg="black",
        width=9,
        height=1,
        activebackground="Red",
        font=("times", 20, "bold"),
    ).place(x=100, y=50)

def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True

# Load and display logo
logo = Image.open("UI_Image/0001.png")
logo = logo.resize((50, 47), Image.Resampling.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)

# Main window UI elements
titl = tk.Label(window, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="black")
l1.place(x=600, y=10)

titl = tk.Label(window, text="IGDTUW!!", bg="black", fg="green", font=("arial", 27))
titl.place(x=700, y=12)

a = tk.Label(
    window,
    text="Face Recognition Based\nAttendance Management System",
    bg="black",
    fg="white",
    bd=10,
    font=("arial", 35),
)
a.pack()

# Display images
ri = Image.open("UI_Image/register.png")
r = ImageTk.PhotoImage(ri)
label1 = tk.Label(window, image=r)
label1.image = r
label1.place(x=100, y=270)

ai = Image.open("UI_Image/attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = tk.Label(window, image=a)
label2.image = a
label2.place(x=980, y=270)

vi = Image.open("UI_Image/verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = tk.Label(window, image=v)
label3.image = v
label3.place(x=600, y=270)

def TakeImageUI():
    ImageUI = tk.Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="black")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
    titl.pack(fill=X)

    titl = tk.Label(ImageUI, text="Register Your Face", bg="black", fg="green", font=("arial", 30))
    titl.place(x=270, y=12)

    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="black",
        fg="white",
        bd=10,
        font=("arial", 24),
    )
    a.place(x=280, y=75)

    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=10,
        height=2,
        bg="black",
        fg="white",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="black",
        fg="white",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="black",
        fg="white",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="black",
        fg="white",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="black",
        fg="white",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl3.place(x=120, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="black",
        fg="white",
        relief=RIDGE,
        font=("times", 12, "bold"),
    )
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=10,
        font=("times new roman", 18),
        bg="black",
        fg="white",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("times new roman", 18),
        bg="black",
        fg="white",
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=350)

# Main window buttons
r = tk.Button(
    window,
    text="Register a new student",
    command=TakeImageUI,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="black",
    height=2,
    width=17,
)
r.place(x=100, y=520)

def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)

r = tk.Button(
    window,
    text="Take Attendance",
    command=automatic_attedance,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="black",
    height=2,
    width=17,
)
r.place(x=600, y=520)

def view_attendance():
    show_attendance.subjectchoose(text_to_speech)

r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="black",
    height=2,
    width=17,
)
r.place(x=1000, y=520)

r = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=window.quit,  # Changed to window.quit to properly close the main window
    font=("times new roman", 16),
    bg="black",
    fg="black",
    height=2,
    width=17,
)
r.place(x=600, y=660)

window.mainloop()

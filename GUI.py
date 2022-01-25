from tkinter import ttk, filedialog
from tkinter import *
from backend import MakeImageAnalysisGreatAgain
from PIL import Image, ImageTk
import cv2

piv = 0
result = []


def is_float(value):
    try:
        float(value)
        return True
    except:
        return False


def getInputBoxValue():
    global width
    temp = tInput.get()
    if is_float(temp) and float(temp) > 0:
        width = float(temp)


def buttonEnterValue():
    getInputBoxValue()
    global result
    try:
        if file_path != "" and width != 0:
            result = MakeImageAnalysisGreatAgain(file_path, width)
    except:
        return


def nextElement():
    global piv
    if result:
        imageRGB = cv2.cvtColor(result[piv], cv2.COLOR_BGR2RGB)
        img = Image.fromarray(imageRGB)
        if piv < len(result) - 1:
            piv = piv + 1
        else:
            piv = 0
        img = img.resize((1500, 750), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        changeImage(img)


def changeImage(img):
    picture.create_image(1500, 0, anchor=NE, image=img)
    mainloop()


def loadPicture():
    global piv
    global file_path
    piv = 0
    file_path = filedialog.askopenfilename()
    try:
        if file_path != "" and width != 0:
            MakeImageAnalysisGreatAgain(file_path, width)
        img = Image.open(file_path)
        img = img.resize((1500, 750), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        changeImage(img)
    except:
        img = Image.open("images/img.png")
        img = img.resize((1500, 750), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        changeImage(img)


width = 0
file_path = ""
root = Tk()

root.geometry('1800x800')
root.configure(background='#F0F8FF')
root.title('IMAGE ANALYSIS PROJECT')

Button(root, text='Enter width of the left object', bg='#F0F8FF', font=("Times New Roman", 12, 'normal'),
       command=buttonEnterValue).place(x=20,
                                       y=336)
Button(root, text='Next', bg='#F0F8FF', font=("Times New Roman", 12, 'normal'), command=nextElement).place(x=90, y=400)
tInput = Entry(root)
tInput.place(x=57, y=276)

picture = Canvas(root, height=750, width=1500)
picture.place(x=273, y=16)
Button(root, text='Upload Photo', bg='#F0F8FF', font=("Times New Roman", 12, 'normal'), command=loadPicture).place(x=62, y=38)

root.mainloop()

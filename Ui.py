from Tkinter import *
from Run import *
from tkFileDialog import *
import tkMessageBox
import cv2
from PIL import Image,ImageTk
import os

def imageOpen():
    fileName = askopenfilename()
    if(fileName!=""):
        
        text = imgToText(fileName)

        image = cv2.imread(fileName)
        # cv2.imshow(("Image",image))
        tkMessageBox.showinfo("Number Plate", text)



class App:
    def __init__(self, master):
        title = "Number-plate Recognition"
        msgtitle = Message(master, text=title)
        msgtitle.config(font=('helvetica', 17, 'bold'), width=200)
        canvas_width = 400
        canvas_height = 200
        w = Canvas(master,
                   width=canvas_width,
                   height=canvas_height)
        msgtitle.pack()
        w.pack()
        self.encrypt = Button(master,
                              text="Select Image", fg="black",
                              command = imageOpen, width=25, height=5)
        self.encrypt.pack(side=TOP)


root = Tk()
app = App(root)
root.mainloop()

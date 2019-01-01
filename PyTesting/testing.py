import tkinter as tk
import tkinter.messagebox as mBox
from PIL import Image, ImageTk

top = tk.Tk()

C = tk.Canvas(top, bg="white", height=562, width=746)
BG_image = Image.open("PyTesting/raw pics/mDW.png")
background_image = ImageTk.PhotoImage(BG_image)
background_label = tk.Label(top, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

def helloCallBack():
    mBox.showinfo("Hello foo", "Hej Ellen")

B = tk.Button(top, text="fub", command = helloCallBack)
B.place(relx=.5, rely=.5)
B.pack()


top.mainloop()
# help("modules")

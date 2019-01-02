import tkinter as tk
import tkinter.messagebox as mBox
from PIL import Image, ImageTk

top = tk.Tk()

C = tk.Canvas(top, bg="white", height=562, width=746)
BG_image = Image.open("PyTesting/raw pics/mDW.png")
background_image = ImageTk.PhotoImage(BG_image)
background_label = tk.Label(top, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def helloCallBack():
    mBox.showinfo("Hello foo", "Hej Ellen")

B = tk.Button(top, text="fub", activebackgound="black" command = helloCallBack)
top.wm_attributes('-transparentcolor', top['bg'])
B_window = C.create_window(100, 100, window=B)


# B.place(x=5, y=5000)
# B.pack()
C.pack()

top.mainloop()
# help("modules")

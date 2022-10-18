import tkinter as tk
from turtle import title

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#1

    canv = tk.Canvas(root, width=1500, height=900, bg="black")#2
    canv.pack()
    

    tori = tk.PhotoImage(file="fig/9.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag = "tori")


    root.mainloop()

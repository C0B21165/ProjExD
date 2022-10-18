import tkinter as tk
import maze_maker as mm#8

def key_down(event):#5
    global key
    key = event.keysym

def key_up(event):#6
    global key
    key = ""

def main_proc():#7
    global cx, cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")#1

    canv = tk.Canvas(root, width=1500, height=900, bg="black")#2
    canv.pack()


    maze_lst = mm.make_maze(15,9)#9
    print(maze_lst)
    mm.show_maze(canv, maze_lst)#10
    

    tori = tk.PhotoImage(file="fig/fig/9.png")#3
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag = "tori")

    key = ""#4

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    
    main_proc()

    root.mainloop()

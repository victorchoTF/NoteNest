from tkinter import *

root = Tk()
root.title("Draw")
root.geometry("1100x600")

stroke_color = StringVar()
stroke_color.set("black")

stroke_size = IntVar()
stroke_size.set(1)

frame1 = Frame(root , height=100 , width=1100)
frame1.grid(row=0 , column=0, sticky=NW)

tools_frame = Frame(frame1, width=100, height=100)
tools_frame.grid(row=0, column=0)


def use_pencil():
    stroke_color.set("black")
    

def user_eraser():
    stroke_color.set("white")
    canvas["cursor"] = DOTBOX

pencil_button = Button(tools_frame, text="Pencil", width=10, command=use_pencil)
pencil_button.grid(row=0, column=0)

eraser_button = Button(tools_frame, text="Eraser", width=10, command=user_eraser)
eraser_button.grid(row=1, column=0)

tool_label = Label(tools_frame, text="Tools", width=10)
tool_label.grid(row=2, column=0)

frame2 = Frame(root , height=500 , width=1100 , bg="yellow")
frame2.grid(row=1 , column=0)

canvas = Canvas(frame2 , height=500 , width=1100 , bg="white")
canvas.grid(row=0 , column=0)

size_frame = Frame(frame1, width=100, height=100)
size_frame.grid(row=0, column=1)

default_button = Button(size_frame, text="Default", width=10, command=use_pencil)
default_button.grid(row=0, column=0)

options = [1, 2, 4, 5]

size_list = OptionMenu(size_frame, stroke_size, *options)
size_list.grid(row=1, column=0)

size_label = Label(size_frame, text="Size", width=10)
size_label.grid(row=2, column=0)

prevPoint = [0, 0]
currentPoint = [0, 0]

def paint(event):
    global prevPoint
    global currentPoint
    x = event.x
    y = event.y
    currentPoint = [x, y]

    if prevPoint != [0, 0]:
        canvas.create_line(prevPoint[0], prevPoint[1], currentPoint[0], currentPoint[1], fill=stroke_color.get(), width=stroke_size.get())
    
    prevPoint = currentPoint

    if event.type == "5":
        prevPoint = [0, 0]

canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)

root.mainloop()
from tkinter import *

root = Tk()
root.title("Draw")
root.geometry("1100x600")

frame1 = Frame(root , height=100 , width=1100 , bg="red")
frame1.grid(row=0 , column=0, sticky=NW)

tools_frame = Frame(frame1, width=100, height=100)
tools_frame.grid(row=0, column=0)


pencil_button = Button(tools_frame, text="Pencil", width=10, command=lambda: stroke_color.set("black"))
pencil_button.grid(row=0, column=0)

eraser_button = Button(tools_frame, text="Eraser", width=10, command=lambda: stroke_color.set("white"))
eraser_button.grid(row=1, column=0)

tool_label = Label(tools_frame, text="Tools", width=10)
tool_label.grid(row=2, column=0)

frame2 = Frame(root , height=500 , width=1100 , bg="yellow")
frame2.grid(row=1 , column=0)

canvas = Canvas(frame2 , height=500 , width=1100 , bg="white")
canvas.grid(row=0 , column=0)

stroke_color = StringVar()
stroke_color.set("black")



prevPoint = [0, 0]
currentPoint = [0, 0]

def paint(event):
    global prevPoint
    global currentPoint
    x = event.x
    y = event.y
    currentPoint = [x, y]

    if prevPoint != [0, 0]:
        canvas.create_line(prevPoint[0], prevPoint[1], currentPoint[0], currentPoint[1], fill=stroke_color.get())
    
    prevPoint = currentPoint

    if event.type == "5":
        prevPoint = [0, 0]

canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)

root.mainloop()
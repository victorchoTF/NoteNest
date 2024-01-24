from tkinter import *

root = Tk()
root.title("Draw")
root.geometry("1100x600")

frame1 = Frame(root , height=100 , width=1100 , bg="red")
frame1.grid(row=0 , column=0)

frame2 = Frame(root , height=500 , width=1100 , bg="yellow")
frame2.grid(row=1 , column=0)

canvas = Canvas(frame2 , height=500 , width=1100 , bg="white")
canvas.grid(row=0 , column=0)

canvas.create_oval(100 , 100 , 120 , 120 , fill="black")
def paint(event):
    x = event.x
    y = event.y
    canvas.create_oval(x , y , x +20 , y + 20 , fill="black")

canvas.bind("<B1-Motion>", paint)

root.mainloop()
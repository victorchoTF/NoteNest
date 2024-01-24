from tkinter import *
from Root import Root

root = Root(1100, 600, "Draw")
frame = Frame(root.root, height=100, width=1100, bg="red")
root.create_frame(frame)

root.run()

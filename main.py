import tkinter as tk
from components.add_cell import AddCell

root = tk.Tk()
frame = tk.Frame(root)

width = root.winfo_screenwidth() 
height = root.winfo_screenheight()

root.geometry(f"{width}x{height}")

add_cell = AddCell(frame)
add_cell.pack(side="bottom")

frame.pack()
root.mainloop()

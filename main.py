import tkinter as tk
from components.add_cell import AddCell

root = tk.Tk()

width = root.winfo_screenwidth() 
height = root.winfo_screenheight()

root.geometry(f"{width}x{height}")

add_cell = AddCell(root)
add_cell.pack(side="bottom")

root.mainloop()

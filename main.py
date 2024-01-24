import tkinter as tk
from text_cell import TextCell

root = tk.Tk()

text_cell = TextCell(root)
text_cell.pack()

text_cell_2 = TextCell(root)
text_cell_2.pack()

root.mainloop()

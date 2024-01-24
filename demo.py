from tkinter import Tk
from text_cell import TextCell

root = Tk()
root.title("Expanding Text")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}+0+0")

text = TextCell(root)
text.pack(padx=10, pady=10)

root.mainloop()

from tkinter import *

class Root:
    def __init__(self, width, height, title) -> None:
        # Initialise main window
        self.root = Tk()

        # Set parameters
        self.width = width
        self.height = height
        self.title = title

        # Enter title, set width and height
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.title(f"{self.title}")

    def create_frame(self,frame):
        self.frame = frame
        self.frame.grid(row=0, column=0)
        
    def run(self):
        self.root.mainloop()


        
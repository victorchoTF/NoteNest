from typing import List
import tkinter as tk
from components.text_cell import TextCell

class AddCell(tk.Frame):
    CELL_TYPES = (
        "Text",
        "Draw",
        "Image"
    )

    def __init__(self, parent: tk.Tk or tk.Frame) -> None: 
        super().__init__(parent)

        self.buttons: List[tk.Button] = []
        
        self.create_buttons()

        self.pack_buttons()
    
    def create_buttons(self) -> None:
        FUNCTIONS = (
            self.create_text_cell,
            lambda: print("Draw"),
            lambda: print("Image")
        )
        
        for cell_type, function in zip(AddCell.CELL_TYPES, FUNCTIONS):
            button = tk.Button(self, text=cell_type, command=function)
            self.buttons.append(button)

    def pack_buttons(self) -> None:
        for button in self.buttons:
            button.pack(side="left")

    def create_text_cell(self) -> None:
        TextCell(self.master)
        
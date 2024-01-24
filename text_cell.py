from typing import Tuple
import tkinter as tk

class TextCell(tk.Text):
    def __init__(self, parent: tk.Tk or tk.Frame, height: int = 1, width: float = 40, font: Tuple[str, int] = ('Helvetica', 12)) -> None:
        super().__init__(parent, wrap=tk.WORD, height=height, width=width, font=font)
        
        self.bind_events()

    
    def bind_events(self) -> None:
        self.bind("<Return>", self.enter_event)
        self.bind("<BackSpace>", self.backspace_event)

    def enter_event(self, _) -> None:
        self.config(height=self.cget("height") + 1)

    def backspace_event(self, _):
        cursor_index = self.index(tk.INSERT)
        cursor_line = int(cursor_index.split(".")[0])

        if cursor_index != f"{cursor_line}.0":
            return
        
        if cursor_line == 1:
            return
        
        self.config(height=self.cget("height") - 1)

    def line_has_content(self, line_number):
        line_start = f"{line_number}.0"
        line_end = f"{line_number + 1}.0"
        line_text = self.get(line_start, line_end).strip()
        return bool(line_text)
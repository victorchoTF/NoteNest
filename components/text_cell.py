from typing import Tuple
from markdown import markdown
from tkhtmlview import HTMLLabel
import tkinter as tk

class TextCell(tk.Frame):
    """Versatile text input and display component for rich text editing with Markdown and HTML support."""

    def __init__(self, parent: tk.Tk or tk.Frame, number_of_lines: int = 1, width: float = 80, font: Tuple[str, int] = ('Helvetica', 15)) -> None:
        """Initializes a TextCell instance with the specified parent, initial number of lines, width, and font."""
        
        super().__init__(parent)

        self.width = width
        self.font = font
        
        self.text_widget = tk.Text(self, wrap=tk.WORD, height=number_of_lines, width=width, font=self.font)
        self.html_label = HTMLLabel(self, html="")

        self.is_compiled = False

        self.bind_events()
        
        self.text_widget.pack()
        
        self.pack()

    @property
    def text(self) -> str:
        """Returns the entire text content of the text_widget."""

        return self.text_widget.get("1.0", tk.END)
    
    @property
    def filtered_text(self) -> str:
        """Returns the text content with empty lines removed."""

        return '\n'.join(line for line in self.text.splitlines() if line.strip())

    @property
    def number_of_lines(self) -> int:
        """Returns the current number of lines in the text_widget."""

        return self.text.count('\n')
    
    @property
    def html_label_height(self) -> int:
        """Calculates the height needed to display HTML content based on Markdown formatting."""

        height = self.number_of_lines
        for line in self.filtered_text.splitlines():
            hashtag_count = line.count("#")

            height += 6 - hashtag_count if hashtag_count else 1
        
        return height

    def bind_events(self) -> None:
        """Binds events to corresponding methods for handling user interactions."""

        self.text_widget.bind("<Return>", self.enter_event)
        self.text_widget.bind("<BackSpace>", self.backspace_event)
        self.text_widget.bind("<Control-h>", self.backspace_event)
        self.text_widget.bind("<KeyRelease>", self.update_html_event)
        self.text_widget.bind("<Shift-Return>", self.shift_enter_event)
        self.html_label.bind("<Button-1>", self.html_label_click_event)

    def enter_event(self, _: tk.Event) -> None:
        """Adjusts the height of the text widget on pressing the Enter key."""

        current_height = self.number_of_lines + 1
        self.text_widget.config(height=current_height)

    def backspace_event(self, _: tk.Event) -> None:
        """Adjusts the height of the text widget on pressing Backspace or Control-h."""

        cursor_index = self.text_widget.index(tk.INSERT)
        cursor_line = int(cursor_index.split(".")[0])

        if cursor_index != f"{cursor_line}.0":
            return
        
        if cursor_line == 1:
            return
        
        current_height = self.number_of_lines - 1
        self.text_widget.config(height=current_height)

    def update_html_event(self, _: tk.Event) -> None:
        """Updates the HTML label content based on Markdown formatting."""

        if self.is_compiled:
            return

        markdown_text_with_spaces = self.text.replace('\n', '  \n')

        html_content = markdown(markdown_text_with_spaces)
        decoded_html = TextCell.decode_html_entities(html_content)
        self.html_label.set_html(decoded_html)
        self.fit_html_label_content()

    def shift_enter_event(self, _: tk.Event) -> None:
        """Switches to HTML display mode on pressing Shift-Enter."""

        self.text_widget.mark_set(tk.INSERT, tk.END)

        self.master.focus_set()

        self.text_widget.pack_forget()
        self.html_label.pack()
        self.is_compiled = True

    def html_label_click_event(self, _: tk.Event) -> None:
        """Switches back to text mode on clicking the HTML label."""

        self.html_label.pack_forget()
        self.text_widget.pack()
        self.is_compiled = False

        self.polish_text()

    def polish_text(self) -> None:
        """Trims trailing newline characters and adjusts the text widget."""

        text_content = self.text.rstrip("\n")
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert(tk.END, text_content)
        self.text_widget.config(height=self.number_of_lines)
        self.text_widget.mark_set(tk.INSERT, tk.END)

    def fit_html_label_content(self) -> None:
        """Fits the HTML label content within specified width and calculated height."""

        self.html_label.configure(width=self.width, height=self.html_label_height)


    @staticmethod
    def decode_html_entities(html_content) -> str:
        """Decodes HTML entities in the given content."""

        return html_content.encode("utf-8").decode("unicode_escape")

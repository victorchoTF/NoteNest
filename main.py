from tkinter import Tk, END, Button, StringVar
from tkhtmlview import HTMLLabel
from text_cell import TextCell
from markdown import markdown

def decode_html_entities(html_content):
    return html_content.encode("utf-8").decode("unicode_escape")

def update_html():
    markdown_text = text.get("1.0", END)
    html_content = markdown(markdown_text)
    decoded_html = decode_html_entities(html_content)
    html_label.set_html(decoded_html)

root = Tk()
root.title("Expanding Text")

text = TextCell(root)
text.pack(padx=10, pady=10)

Button(root, text="Click", command=update_html).pack()

html_label = HTMLLabel(root)
html_label.pack()

root.mainloop()

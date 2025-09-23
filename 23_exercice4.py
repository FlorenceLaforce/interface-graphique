import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("detecteur de touche")
        self.geometry("400x400")
        row = ttk.Frame(self)
        row.pack(padx=5, pady=5)
        for t in ( "A", "B", "C", "D", "E", "F" ):
            ttk.Button(row, text= f"Bouton {t}").pack(side="left", padx = 6)
        self.bind_class("TButton", "<Enter>", self.on_hover)

    def on_hover(self, e):
        self.title(f"Survol: {e.widget.cget("text")}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = "detecteur de touche"
        self.geometry = "400x400"
        self.crer_widget()

    def crer_widget(self):
        self.champ = tk.Entry(self)
        self.champ.pack(padx=10, pady=5)
        self.champ.bind("<KeyRelease>", self.touche_appuyee)

    def touche_appuyee(self, event):
        messagebox.showinfo("Touche appuyee", repr(event.char))

if __name__ == "__main__":
    app = Application()
    app.mainloop()

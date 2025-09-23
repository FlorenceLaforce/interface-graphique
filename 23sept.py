import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = "Graphique"
        self.geometry = "200x200"
        self.lbl = tk.Label(self,text ="Hola", fg="plum", bg="white")
        self.lbl.pack(padx=5, pady=5)
        tk.Button(self, text = "mettre à jour", command= self.maj).pack(padx=5, pady=5)

    def maj(self):
        self.lbl.config(text="Bonjour")
        print("Texte actuel =", self.lbl.cget("text"))

if __name__ == "__main__":
    app = Application()
    app.mainloop()
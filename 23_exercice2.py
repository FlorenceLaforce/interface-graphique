import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Entry method example")
        self.e = tk.Entry(self, width=60)
        self.e.pack(padx=10, pady=5)
        self.e.insert(0, "Texte par défaut")
        bar = tk.Frame(self) ; bar.pack(pady = 6)
        btn_lire = tk.Button(bar, text = "lire", command = self.lire)
        btn_lire.pack(side = "left", padx = 4)
        btn_effacer = tk.Button(bar,text = "Effacer", command = self.eff)
        btn_effacer.pack(side = "left", padx = 4)
        btn_inserer = tk.Button(bar, text = "inserer au début", command = self.debut)
        btn_inserer.pack(side = "left", padx = 4)

    def lire(self):
        print("Entry =", self.e.get())

    def eff(self):
        self.e.delete(0, "end")

    def debut(self):
        self.e.insert(0, "BAGUETTE")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
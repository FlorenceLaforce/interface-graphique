import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("interface simple")
        self.geometry("400x500")
        self.crer_widget()

    def crer_widget(self):
        #partie
        self.label = tk.Label(self, text="Nombre 1:")
        self.label.pack(padx=5, pady=5)
        self.champ = tk.Entry(self)
        self.champ.pack(padx=10, pady=5)
        #partie 2
        self.label2 = tk.Label(self, text="Nombre 2:")
        self.label2.pack(padx=5, pady=5)
        self.champ2 = tk.Entry(self)
        self.champ2.pack(padx=10, pady=5)

        btn_calculer = tk.Button(text = "Calculer", command=self.calculer)
        btn_calculer.pack(padx=10, pady=5)

    def calculer(self):
        try:
            n1 = float(self.champ.get())
            n2 = float(self.champ2.get())
            resultat = n1 + n2
            messagebox.showinfo("Resultat", f"{resultat}")
        except ValueError:
            messagebox.showerror("Error", "CE N'EST PAS UN FOUTU CHIFFRE CRISS D'AARON")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
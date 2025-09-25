import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("interface simple")
        self.geometry("400x200")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        frm1 = tk.Frame(self)
        frm1.grid(row=0, column=0, sticky="nsew", padx=10, pady=40)
        frm1.columnconfigure(1, weight=1)

        tk.Label(frm1, text="Couriel :").grid(row=0, column=0, sticky="e")
        email = tk.Entry(frm1)
        email.grid(row=0, column=1, sticky="we")

        tk.Label(frm1, text="Mot de passe :").grid(row=1, column=0, sticky="e")
        mdp = tk.Entry(frm1, show="*")
        mdp.grid(row=1, column=1, sticky="we")

        btn = tk.Button(frm1, text = "Valider")
        btn.grid(row=0, column=2, rowspan=2, sticky="e")

if __name__ == "__main__":
    app = Application()
    app.mainloop()


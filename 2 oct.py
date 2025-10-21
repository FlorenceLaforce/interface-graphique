import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulaire")
        self.geometry("800x600")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.creer_widgets()


    def creer_widgets(self):
        frm = tk.Frame(self, bg="mistyrose")
        frm.grid(row=0, column=0, sticky="nsew")
        frm.columnconfigure(0, weight=1)
        frm.columnconfigure(1, weight=60)
        frm.columnconfigure(2, weight=1)
        frm.columnconfigure(3, weight=1)
        frm.columnconfigure(4, weight=1)

        frm.rowconfigure(2, weight=1)

        frm2 = tk.Frame(self, bg="lightcoral")
        frm2.grid(row=3, column=0, sticky="nsew")

        nom = tk.Label(frm, text="Nom")
        nom.grid(row=0, column=0, sticky="w", padx=20, pady=10)

        email = tk.Label(frm, text = "Email")
        email.grid(row = 0, column = 1, sticky = "w", padx=10, pady=10)

        age = tk.Label(frm, text = "Age")
        age.grid(row=0, column = 2, sticky = "w", padx=10, pady=10)

        self.entrer_nom = tk.Entry(frm, width = 20)
        self.entrer_nom.grid(row = 1, column = 0, sticky = "ew", padx=20, pady=10)

        self.entrer_email = tk.Entry(frm, width = 30)
        self.entrer_email.grid(row = 1, column = 1, sticky = "ew", padx=10, pady=10)

        self.entrer_age = tk.Entry(frm, width = 10)
        self.entrer_age.grid(row = 1, column = 2, sticky = "ew", padx=10, pady=10)

        btn_ajouter = tk.Button(frm, text="Ajouter", command=self.ajouter_donnees)
        btn_ajouter.grid(row = 1, column = 3, padx=10, pady=10)

        btn_sup = tk.Button(frm, text="Supprimer sélection",command=self.supprimer_selection)
        btn_sup.grid(row = 1, column = 4, padx=10, pady=10)

        self.tableau =ttk.Treeview(frm, columns=("nom", "email", "age"), show="headings")
        self.tableau.heading("nom", text="Nom")
        self.tableau.heading("email", text="Email")
        self.tableau.heading("age", text="Age")
        self.tableau.column("nom", width=80)
        self.tableau.column("email", width=200)
        self.tableau.column("age", width=50)
        self.tableau.grid(row=2, column=0,columnspan=5, sticky="nsew", padx=20, pady=(40,80))


    def ajouter_donnees(self):
        nom = self.entrer_nom.get().strip()
        email = self.entrer_email.get().strip()
        age = self.entrer_age.get().strip()

        if nom and email and age:
            self.tableau.insert("", "end", values=(nom, email, age))
            # Vider les champs après l'ajout
            self.entrer_nom.delete(0, tk.END)
            self.entrer_email.delete(0, tk.END)
            self.entrer_age.delete(0, tk.END)

    def supprimer_selection(self):
        selected_item = self.tableau.selection()
        for item in selected_item:
            self.tableau.delete(item)
        else:
            messagebox.showwarning("Avertissement", "Aucun element selectionné")


    def exporterJson(self):
        if not self.rows:
            messagebox.showinfo("Exporter", "Le fichier n'existe pas")
            return
        path = filedialogue


if __name__ == "__main__":
    app = interface()
    app.mainloop()
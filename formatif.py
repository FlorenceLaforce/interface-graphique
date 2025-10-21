import tkinter as tk
from tkinter import ttk, messagebox
import random


class Produit:
    def __init__(self, nom, quantite, prix):
        self.nom = nom
        self.quantite = quantite
        self.prix = prix

    @property
    def nom(self):
        return self.nom
    @nom.setter
    def nom(self, nom):
        if not isinstance(nom, str):
            raise TypeError("nom must be a string")
        self.nom = nom

    @property
    def quantite(self):
        return self.quantite

    @quantite.setter
    def quantite(self, quantite):
        if not isinstance(quantite, int):
            raise TypeError("quantite must be a integer")
        self.quantite = quantite

    @property
    def prix(self):
        return self.prix

    @prix.setter
    def prix(self, prix):
        if not isinstance(prix, int):
            raise TypeError("prix must be a integer")
        self.prix = prix


class interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulateur de compte --- Florence Laforce")
        self.geometry("600x500")

        self.creer_widgets()

    def creer_widgets(self):

        self.columnconfigure(0, weight=1)

        self.frm = tk.Frame(self)
        self.frm.grid(row=0, column=0, sticky="nsew")
        self.frm.columnconfigure(0, weight=1)

        self.header = tk.LabelFrame(self.frm, text="Ajouter un produit")
        self.header.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.middle = tk.LabelFrame(self.frm, text="Gestion de produits")
        self.middle.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        for i in range(2):
            self.middle.rowconfigure(i, weight=1)
        for i in range(4):
            self.middle.columnconfigure(i, weight=1)

        self.bottom = tk.Frame(self.frm)
        self.bottom.grid(row=2, column=0, sticky="nsew", padx=8, pady=5)

        self.lbl_prod = tk.Label(self.header, text="Produit:")
        self.lbl_prod.grid(row=0, column=0, sticky="e", padx=8, pady=(8,3))

        self.lbl_quantite = tk.Label(self.header, text="Quantite:")
        self.lbl_quantite.grid(row=1, column=0, sticky="e", padx=8, pady=3)

        self.lbl_prix = tk.Label(self.header, text="Prix:")
        self.lbl_prix.grid(row=2, column=0, sticky="e", padx=5, pady=(3,8))

        self.entry_prod = tk.Entry(self.header, width=66)
        self.entry_prod.grid(row=0, column=1, sticky="nsew", padx=5, pady=(8,3))

        self.entry_quantite = tk.Entry(self.header, width=66)
        self.entry_quantite.grid(row=1, column=1, sticky="nsew", padx=5, pady=3)

        self.entry_prix = tk.Entry(self.header, width=66)
        self.entry_prix.grid(row=2, column=1, sticky="nsew", padx=5, pady=(3,8))

        self.bouton = tk.Button(self.header, text="Ajouter Produit", command=self.ajouter_produits)
        self.bouton.grid(row=1, column=2, sticky="nsew", padx=5, pady=3)

        self.btn_sup = tk.Button(self.middle, text="Supprimer Produit")
        self.btn_sup.grid(row=0, column=0, columnspan=2, padx=5, pady=(10,5))

        self.btn_modif = tk.Button(self.middle, text="Modifier Produit")
        self.btn_modif.grid(row=0, column=2, columnspan=2, padx=5, pady=(10,5))

        self.btn_sauv_csv = tk.Button(self.middle, text="Sauvegarder CSV ")
        self.btn_sauv_csv.grid(row=1, column=0, padx=5, pady=(5,10))

        self.btn_sauv_JSON = tk.Button(self.middle, text="Sauvegarder JSON ")
        self.btn_sauv_JSON.grid(row=1, column=1, padx=5, pady=(5,10))

        self.btn_import_csv = tk.Button(self.middle, text="Importer CSV ")
        self.btn_import_csv.grid(row=1, column=2, padx=5, pady=(5,10))

        self.btn_import_JSON = tk.Button(self.middle, text="Importer JSON ")
        self.btn_import_JSON.grid(row=1, column=3, padx=5, pady=(5,10))

        self.tableau = ttk.Treeview(self.bottom, columns=("Produit", "Quantite", "Prix"), show="headings", selectmode="extended")
        self.tableau.heading("Produit", text="Produit")
        self.tableau.heading("Quantite", text="Quantite")
        self.tableau.heading("Prix", text="Prix")

        self.tableau.grid(row=0, column=0, sticky="nsew")

    def ajouter_produits(self):
        nom = self.entry_prod.get()
        quantite = self.entry_quantite.get()
        prix = self.entry_prix.get()
        try:
            produit = Produit(nom, quantite, prix)
            self.tableau.insert("", values = (Produit.nom, Produit.quantite, Produit.prix))
            self.entry_prod.delete(0,"end")
            self.entry_quantite.delete(0,"end")
            self.entry_prix.delete(0,"end")
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))

    def supprimer_produits(self):
        selected = self.tableau.selection()
        if not selected:
            messagebox.showwarning("selection requise", "veuillez selectionner un produit")
            return
        for item in selected:
            self.tableau.delete(item)


    def modifier(self):
        data = self.tableau.selection()[0]
        i = self.tableau.item(data)["values"]
        self.tableau.delete(data)
        self.entry_prix.delete(0, "end")
        self.entry_quantite.delete(0, "end")
        self.entry_prod.delete(0, "end")
        self.entry_prix.insert(0, i[0])
        self.entry_quantite.insert(0, i[1])
        self.entry_prod.insert(0, i[2])









if __name__ == "__main__":
    app = interface()
    app.mainloop()
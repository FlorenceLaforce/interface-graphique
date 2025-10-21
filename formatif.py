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

        frm = tk.Frame(self)
        frm.grid(row=0, column=0, sticky="nsew")

        header = tk.LabelFrame(frm, text="Ajouter un produit")
        header.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        middle = tk.LabelFrame(frm, text="Gestion de produits")
        middle.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        for i in range(2):
            middle.rowconfigure(i, weight=1)
        for i in range(4):
            middle.columnconfigure(i, weight=1)

        bottom = tk.Frame(frm)
        bottom.grid(row=2, column=0, sticky="nsew", padx=8, pady=5)

        lbl_prod = tk.Label(header, text="Produit:")
        lbl_prod.grid(row=0, column=0, sticky="e", padx=8, pady=(8,3))

        lbl_quantite = tk.Label(header, text="Quantite:")
        lbl_quantite.grid(row=1, column=0, sticky="e", padx=8, pady=3)

        lbl_prix = tk.Label(header, text="Prix:")
        lbl_prix.grid(row=2, column=0, sticky="e", padx=5, pady=(3,8))

        entry_prod = tk.Entry(header, width=66)
        entry_prod.grid(row=0, column=1, sticky="nsew", padx=5, pady=(8,3))

        entry_quantite = tk.Entry(header, width=66)
        entry_quantite.grid(row=1, column=1, sticky="nsew", padx=5, pady=3)

        entry_prix = tk.Entry(header, width=66)
        entry_prix.grid(row=2, column=1, sticky="nsew", padx=5, pady=(3,8))

        bouton = tk.Button(header, text="Ajouter Produit")
        bouton.grid(row=1, column=2, sticky="nsew", padx=5, pady=3)

        btn_sup = tk.Button(middle, text="Supprimer Produit")
        btn_sup.grid(row=0, column=0, columnspan=2, padx=5, pady=(10,5))

        btn_modif = tk.Button(middle, text="Modifier Produit")
        btn_modif.grid(row=0, column=2, columnspan=2, padx=5, pady=(10,5))

        btn_sauv_csv = tk.Button(middle, text="Sauvegarder CSV ")
        btn_sauv_csv.grid(row=1, column=0, padx=5, pady=(5,10))

        btn_sauv_JSON = tk.Button(middle, text="Sauvegarder JSON ")
        btn_sauv_JSON.grid(row=1, column=1, padx=5, pady=(5,10))

        btn_import_csv = tk.Button(middle, text="Importer CSV ")
        btn_import_csv.grid(row=1, column=2, padx=5, pady=(5,10))

        btn_import_JSON = tk.Button(middle, text="Importer JSON ")
        btn_import_JSON.grid(row=1, column=3, padx=5, pady=(5,10))

        tableau = ttk.Treeview(bottom, columns=("Produit", "Quantite", "Prix"), show="headings", selectmode="extended")
        tableau.heading("Produit", text="Produit")
        tableau.heading("Quantite", text="Quantite")
        tableau.heading("Prix", text="Prix")

        tableau.grid(row=0, column=0, sticky="nsew")





if __name__ == "__main__":
    app = interface()
    app.mainloop()
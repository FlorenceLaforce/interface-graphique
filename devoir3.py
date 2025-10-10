import tkinter as tk
from tkinter import ttk, messagebox
import random


class interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulateur de compte --- Florence Laforce")
        self.geometry("600x250")

        self.comptes = {}

        self.affichage_random = tk.StringVar()
        self.affichage_random.set("")

        self.affichage_solde =tk.StringVar()
        self.affichage_solde.set("")

        self.creer_widgets()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def creer_widgets(self):
        frm1 = tk.Frame(self)
        frm1.grid(row=0, column=0, sticky="nsew")
        frm1.columnconfigure(0, weight=1)
        frm1.rowconfigure(0, weight=1)
        frm1.rowconfigure(1, weight=1)

        lbl_frm = tk.LabelFrame(frm1, text = "Données du compte")
        lbl_frm.grid(row=0, column=0, sticky="nsew",padx=10, pady=10)
        #lbl_frm.rowconfigure(0, weight=1)
        #lbl_frm.rowconfigure(1, weight=0)
        #lbl_frm.columnconfigure(0, weight=1)
        #lbl_frm.columnconfigure(1, weight=0)

        lbl_frm_montants = tk.LabelFrame(frm1, text = "Montant")
        lbl_frm_montants.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        frm2 = tk.Frame(frm1)
        frm2.grid(row=1, column=0,columnspan=2, pady = 10)
        #frm2.columnconfigure(0, weight=0)
        #frm2.columnconfigure(1, weight=1)
        #frm2.columnconfigure(2, weight=0)
        #frm2.columnconfigure(3, weight=1)
        #frm2.columnconfigure(4, weight=0)
        #frm2.columnconfigure(5, weight=1)
        #frm2.columnconfigure(6, weight=0)

        lbl1 = tk.Label(lbl_frm, text = "Numéro :")
        lbl1.grid(row=0, column=0, sticky="e", padx=10, pady=5)

        lbl2 = tk.Label(lbl_frm, text = "Détenteur :")
        lbl2.grid(row=1, column=0, sticky="e", padx=10, pady=5)

        lbl3 = tk.Label(lbl_frm, text = "Solde :")
        lbl3.grid(row=2, column=0, sticky="e", padx=10, pady=5)

        self.entry_num = tk.Entry(lbl_frm, width = 20)
        self.entry_num.grid(row=0, column=1, sticky="w", pady = 5)

        self.variable_gelee = tk.BooleanVar(value = False)
        btn_chk = tk.Checkbutton(lbl_frm, text = "Gelé",variable=self.variable_gelee, command=self.basculer_gelee)
        btn_chk.grid(row=0, column=2, sticky="nsew", padx=10)

        self.entry_detenteur = tk.Entry(lbl_frm, width = 30)
        self.entry_detenteur.grid(row=1, column=1, columnspan=2, sticky="w", pady=5)

        self.entry_solde = tk.Entry(lbl_frm, textvariable= self.affichage_solde, width=20,  state="readonly",bg="white")
        self.entry_solde.grid(row=2, column=1, columnspan=2, sticky="w", pady=5)
        #entry_solde = tk.Entry(lbl_frm, width = 20)
        #entry_solde.grid(row=2, column=1, columnspan=2, sticky="w", pady=5)

        entry_montant = tk.Label(lbl_frm_montants, textvariable=self.affichage_random, width = 10, bg = "white")
        entry_montant.grid(row=0, column=0, sticky="w", pady=5, padx=10)

        self.btn_random = tk.Button(lbl_frm_montants, text = "Random", width=10, command=self.random)
        self.btn_random.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.civ = tk.StringVar(value="M")
        btn_radio = tk.Radiobutton(lbl_frm_montants, text = "1 à 10", variable = self.civ, value = "M")
        btn_radio.grid(row=0, column=1, sticky="w",padx=10)
        btn_radio = tk.Radiobutton(lbl_frm_montants, text="10 à 100", variable=self.civ, value="L")
        btn_radio.grid(row=1, column=1, sticky="w", padx=10)
        btn_radio = tk.Radiobutton(lbl_frm_montants, text="100 à 1000", variable=self.civ, value="C")
        btn_radio.grid(row=2, column=1, sticky="w", padx=10)

        self.btn_depo = tk.Button(frm2, text = "Déposer", width=10)
        self.btn_depo.grid(row=0, column=0, padx=(10,40), pady=5)

        self.btn_retirer = tk.Button(frm2, text = "Retirer", width = 10)
        self.btn_retirer.grid(row=0, column=1, padx=40, pady=5)

        self.btn_vider = tk.Button(frm2, text="Vider", width=10)
        self.btn_vider.grid(row=0, column=2, padx=40, pady=5)

        self.btn_reset = tk.Button(frm2, text = "Reset", width=10)
        self.btn_reset.grid(row=0, column=3, padx=(40,10), pady=5)

        self.gelables = [
            self.entry_num,
            self.entry_detenteur,
            self.btn_random,
        ]

        for child in lbl_frm_montants.winfo_children():
            if isinstance(child, tk.Radiobutton):
                self.gelables.append(child)
        self.gelables.extend([self.btn_depo, self.btn_retirer, self.btn_vider, self.btn_reset])

    def valider_numero(self, numero: str) -> bool:
        numero = numero.strip()
        return numero.isdigit() and len(numero) == 5

    def valider_detenteur(self, det: str) -> bool:
        det = det.strip()
        lettres = [c for c in det if c.isalpha()]
        return len(lettres) >= 5


    def obtenir_paire(self):
        num = self.entry_num.get().strip()
        det = self.entry_detenteur.get().strip()
        return num, det

    def mettre_a_jour_solde_affichage(self, num, det):
        if (num, det) in self.comptes:
            solde = self.comptes[(num, det)]
            # afficher avec 2 décimales
            self.affichage_solde.set(f"{solde:.2f}")
        else:
            self.affichage_solde.set("")

    def random(self):
        sel = self.civ.get()
        if sel == "M":
            val = random.randint(1, 10)
        elif sel == "L":
            val = random.randint(10, 100)
        elif sel == "C":
            val = random.randint(100, 1000)
        else:
            # fallback
            val = random.randint(1, 10)
        # mettre à jour l'entry (label) du montant
        self.affichage_random.set(str(val))

    def basculer_gelee(self):
        gelee = self.variable_gelee.get()
        state = "disabled" if gelee else "normal"
        for w in self.gelables:
            try:
                w.configure(state=state)
            except tk.TclError:
                try:
                    w.configure(state=state)
                except Exception:
                    pass



if __name__ == "__main__":
    app = interface()
    app.mainloop()
import tkinter as tk
from tkinter import ttk


class interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulateur de compte --- Florence Laforce")
        self.geometry("800x600")
        self.creer_widgets()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def creer_widgets(self):
        frm1 = tk.Frame(self, bg="aqua")
        frm1.grid(row=0, column=0, sticky="nsew")
        frm1.columnconfigure(0, weight=1)
        frm1.rowconfigure(0, weight=1)
        frm1.rowconfigure(1, weight=1)

        lbl_frm = tk.LabelFrame(frm1, text = "Données du compte", bg = "purple")
        lbl_frm.grid(row=0, column=0, sticky="nsew",padx=10, pady=10)
        lbl_frm.rowconfigure(0, weight=1)
        lbl_frm.rowconfigure(1, weight=0)
        lbl_frm.columnconfigure(0, weight=1)
        lbl_frm.columnconfigure(1, weight=0)

        lbl_frm_montants = tk.LabelFrame(frm1, text = "Montant")
        lbl_frm_montants.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        frm2 = tk.Frame(frm1, bg="pink")
        frm2.grid(row=1, column=0,columnspan=2, sticky="nsew")
        frm2.columnconfigure(0, weight=0)
        frm2.columnconfigure(1, weight=1)
        frm2.columnconfigure(2, weight=0)
        frm2.columnconfigure(3, weight=1)
        frm2.columnconfigure(4, weight=0)
        frm2.columnconfigure(5, weight=1)
        frm2.columnconfigure(6, weight=0)


        lbl1 = tk.Label(lbl_frm, text = "Numéro :")
        lbl1.grid(row=0, column=0, sticky="nsew")

        lbl2 = tk.Label(lbl_frm, text = "Détenteur :")
        lbl2.grid(row=1, column=0, sticky="nsew")

        lbl3 = tk.Label(lbl_frm, text = "Solde :")
        lbl3.grid(row=2, column=0, sticky="nsew")

        entry_num = tk.Entry(lbl_frm, width = 10)
        entry_num.grid(row=0, column=1, sticky="nsew")

        btn_chk = tk.Checkbutton(lbl_frm, text = "Gelé")
        btn_chk.grid(row=0, column=2, sticky="nsew")

        entry_detenteur = tk.Entry(lbl_frm, width = 10)
        entry_detenteur.grid(row=1, column=1, columnspan=2, sticky="nsew")

        entry_solde = tk.Entry(lbl_frm, width = 10)
        entry_solde.grid(row=2, column=1, columnspan=2, sticky="nsew")

        entry_montant = tk.Entry(lbl_frm_montants, width = 10)
        entry_montant.grid(row=0, column=0, sticky="nsew")

        btn_random = tk.Button(lbl_frm_montants, text = "Random")
        btn_random.grid(row=1, column=0, sticky="nsew")

        civ = tk.StringVar(value="M")
        btn_radio = tk.Radiobutton(lbl_frm_montants, text = "1 à 10", variable = civ, value = "M")
        btn_radio.grid(row=0, column=1, sticky="nsew")
        btn_radio = tk.Radiobutton(lbl_frm_montants, text="10 à 100", variable=civ, value="L")
        btn_radio.grid(row=1, column=1, sticky="nsew")
        btn_radio = tk.Radiobutton(lbl_frm_montants, text="100 à 1000", variable=civ, value="C")
        btn_radio.grid(row=2, column=1, sticky="nsew")

        btn_depo = tk.Button(frm2, text = "Déposer")
        btn_depo.grid(row=0, column=0, sticky="nsew")

        btn_retirer = tk.Button(frm2, text = "Retirer")
        btn_retirer.grid(row=0, column=2, sticky="nsew")

        btn_vider = tk.Button(frm2, text="Vider")
        btn_vider.grid(row=0, column=4, sticky="nsew")

        btn_reset = tk.Button(frm2, text = "Reset")
        btn_reset.grid(row=0, column=6, sticky="nsew")



if __name__ == "__main__":
    app = interface()
    app.mainloop()
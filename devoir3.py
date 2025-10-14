import tkinter as tk
from tkinter import ttk, messagebox
import random


class interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulateur de compte --- Florence Laforce")
        self.geometry("600x250")

        self.comptes = {} # creer un dict afin de stocker les compte (pas ajour)

        self.affichage_random = tk.StringVar() #afffiche montant random comme une string
        self.affichage_random.set("") #creer chaine vide

        self.affichage_solde =tk.StringVar()  #afffiche solde comme une string
        self.affichage_solde.set("") #creer chaine vide

        self.creer_widgets() # appel methode creer_widget
        self.columnconfigure(0, weight=1) #configuration de la grille (column_
        self.rowconfigure(0, weight=1) #configuration de la grille (row)

    def creer_widgets(self):

        #creation et configuration du frame 1
        frm1 = tk.Frame(self)
        frm1.grid(row=0, column=0, sticky="nsew")
        frm1.columnconfigure(0, weight=1)
        frm1.rowconfigure(0, weight=1)
        frm1.rowconfigure(1, weight=1)

        # lbl frame donnée du compte
        lbl_frm = tk.LabelFrame(frm1, text = "Données du compte")
        lbl_frm.grid(row=0, column=0, sticky="nsew",padx=10, pady=10)
        #lbl_frm.rowconfigure(0, weight=1)
        #lbl_frm.rowconfigure(1, weight=0)
        #lbl_frm.columnconfigure(0, weight=1)
        #lbl_frm.columnconfigure(1, weight=0)

        # lbl frame montant
        lbl_frm_montants = tk.LabelFrame(frm1, text = "Montant")
        lbl_frm_montants.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # frame principal 2 (en dessou du premier)
        frm2 = tk.Frame(frm1)
        frm2.grid(row=1, column=0,columnspan=2, pady = 10)
        #frm2.columnconfigure(0, weight=0)
        #frm2.columnconfigure(1, weight=1)
        #frm2.columnconfigure(2, weight=0)
        #frm2.columnconfigure(3, weight=1)
        #frm2.columnconfigure(4, weight=0)
        #frm2.columnconfigure(5, weight=1)
        #frm2.columnconfigure(6, weight=0)

        # label numero
        lbl1 = tk.Label(lbl_frm, text = "Numéro :")
        lbl1.grid(row=0, column=0, sticky="e", padx=10, pady=5)

        #label detenteur
        lbl2 = tk.Label(lbl_frm, text = "Détenteur :")
        lbl2.grid(row=1, column=0, sticky="e", padx=10, pady=5)

        #label solde
        lbl3 = tk.Label(lbl_frm, text = "Solde :")
        lbl3.grid(row=2, column=0, sticky="e", padx=10, pady=5)

        #entry numero
        self.entry_num = tk.Entry(lbl_frm, width = 20)
        self.entry_num.grid(row=0, column=1, sticky="w", pady = 5)

        #check button
        self.variable_gelee = tk.BooleanVar(value = False) # met l'état geler
        btn_chk = tk.Checkbutton(lbl_frm, text = "Gelé",variable=self.variable_gelee, command=self.basculer_gelee)
        btn_chk.grid(row=0, column=2, sticky="nsew", padx=10)

        #entry dtenteur
        self.entry_detenteur = tk.Entry(lbl_frm, width = 30)
        self.entry_detenteur.grid(row=1, column=1, columnspan=2, sticky="w", pady=5)

        #entry solde
        self.entry_solde = tk.Entry(lbl_frm, textvariable= self.affichage_solde, width=20,  state="readonly",bg="white")
        # champ affichant le solde en lecture seule, textvariable à self.affichage_solde
        self.entry_solde.grid(row=2, column=1, columnspan=2, sticky="w", pady=5)
        #entry_solde = tk.Entry(lbl_frm, width = 20)
        #entry_solde.grid(row=2, column=1, columnspan=2, sticky="w", pady=5)

        # label montant random (non-modifiable),lié à self.affichage_random
        entry_montant = tk.Label(lbl_frm_montants, textvariable=self.affichage_random, width = 10, bg = "white")
        entry_montant.grid(row=0, column=0, sticky="w", pady=5, padx=10)
        self.entry_montant = entry_montant

        # bouton random
        self.btn_random = tk.Button(lbl_frm_montants, text = "Random", width=10, command=self.random) # lié avec def random
        self.btn_random.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        # radio button (choix de montant random)
        self.civ = tk.StringVar(value="M") # variable qui contient les choix radio (M,L,C)
        btn_radio = tk.Radiobutton(lbl_frm_montants, text = "1 à 10", variable = self.civ, value = "M")
        btn_radio.grid(row=0, column=1, sticky="w",padx=10)
        btn_radio = tk.Radiobutton(lbl_frm_montants, text="10 à 100", variable=self.civ, value="L")
        btn_radio.grid(row=1, column=1, sticky="w", padx=10)
        btn_radio = tk.Radiobutton(lbl_frm_montants, text="100 à 1000", variable=self.civ, value="C")
        btn_radio.grid(row=2, column=1, sticky="w", padx=10)

        #bouton depo lié a self.deposer
        self.btn_depo = tk.Button(frm2, text = "Déposer", width=10, command=self.deposer)
        self.btn_depo.grid(row=0, column=0, padx=(10,40), pady=5)

        #bouton retirer lié a self.retirer
        self.btn_retirer = tk.Button(frm2, text = "Retirer", width = 10, command=self.retirer)
        self.btn_retirer.grid(row=0, column=1, padx=40, pady=5)

        #bouton vider lié a self.vider
        self.btn_vider = tk.Button(frm2, text="Vider", width=10, command=self.vider)
        self.btn_vider.grid(row=0, column=2, padx=40, pady=5)

        #bouton reset lié a self.reset
        self.btn_reset = tk.Button(frm2, text = "Reset", width=10, command=self.reset)
        self.btn_reset.grid(row=0, column=3, padx=(40,10), pady=5)

        #liste de variable qui vont etre geler
        self.gelables = [
            self.entry_num,
            self.entry_detenteur,
            self.btn_random,
            self.entry_montant,
        ]

        #ajoute bouton radio dans gelable
        for i in lbl_frm_montants.winfo_children():
            if isinstance(i, tk.Radiobutton):
                self.gelables.append(i)
        #ajouter bouton (depo, retirer,vider, reset) dans gelable
        self.gelables.extend([self.btn_depo, self.btn_retirer, self.btn_vider, self.btn_reset])

    #verifie numero (si == 5 chiffre) return True or fasle
    def valider_numero(self, numero: str) -> bool:
        numero = numero.strip()
        return numero.isdigit() and len(numero) == 5

    #verifie si au moins 5 lettres
    def valider_detenteur(self, det: str) -> bool:
        det = det.strip()
        lettres = [c for c in det if c.isalpha()]
        return len(lettres) >= 5

    #on recupere valeur numero et la valeur detenteur et on return un "couple" (num, det)
    def obtenir_paire(self):
        num = self.entry_num.get().strip()
        det = self.entry_detenteur.get().strip()
        return num, det


    def mettre_a_jour_solde_affichage(self, num, det):
        if (num, det) in self.comptes: # si compte existe
            solde = self.comptes[(num, det)] #prend solde
            # afficher avec 2 décimales
            self.affichage_solde.set(f"{solde:.2f}")
        else:
            self.affichage_solde.set("")# sinon on vide l'affichage du solde

    #def random montant
    def random(self):
        sel = self.civ.get() #prend selection: M,L,C
        #prend num dependament de la lettre
        if sel == "M":
            val = random.randint(1, 10)
        elif sel == "L":
            val = random.randint(10, 100)
        elif sel == "C":
            val = random.randint(100, 1000)
        else:
            val = random.randint(1, 10)
        self.affichage_random.set(str(val)) #met a jour la string affichage_random

    def deposer(self):
        num, det = self.obtenir_paire() #recupere champs
        if not self.valider_numero(num): #valide num
            messagebox.showerror("Erreur", "Numéro invalide : doit contenir exactement 5 chiffres.")
            return
        if not self.valider_detenteur(det): #valide detenteur
            messagebox.showerror("Erreur", "Détenteur invalide : doit contenir au moins 5 lettres.")
            return
        montant_txt = self.affichage_random.get().strip() #prend montant de affichage_random
        if montant_txt == "":
            messagebox.showerror("Erreur", "Aucun montant. Appuyez sur Random ou entrez un montant via Random.")
            return
        try:
            montant = float(montant_txt)# convertit en float
            if montant <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Erreur", "Montant invalide.")
            return

        cle = (num, det) #elements du compte
        if cle in self.comptes:
            self.comptes[cle] += montant #ajout au solde existant
        else:
            self.comptes[cle] = montant #cree un nouveau compte avec ce solde


        self.mettre_a_jour_solde_affichage(num, det) #met a jour affichage solde
        messagebox.showinfo("Succès", f"Dépôt effectué : {montant:.2f}.\nSolde actuel : {self.comptes[cle]:.2f}")

    def retirer(self):
        #meme chose que def deposer
        num, det = self.obtenir_paire()

        if not self.valider_numero(num):
            messagebox.showerror("Erreur", "Numéro invalide : doit contenir exactement 5 chiffres.")
            return
        if not self.valider_detenteur(det):
            messagebox.showerror("Erreur", "Détenteur invalide : doit contenir au moins 5 lettres.")
            return

        montant_txt = self.affichage_random.get().strip()
        if montant_txt == "":
            messagebox.showerror("Erreur", "Aucun montant. Appuyez sur Random pour générer un montant.")
            return
        try:
            montant = float(montant_txt)
            if montant <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Erreur", "Montant invalide.")
            return

        cle = (num, det)
        if cle not in self.comptes: #si compte introuvable
            messagebox.showerror("Erreur", "Compte introuvable.")
            return

        if self.comptes[cle] < montant: #si solde insufisant
            messagebox.showerror("Erreur", "Solde insuffisant.")
            return

        self.comptes[cle] -= montant #soustrait montant
        self.mettre_a_jour_solde_affichage(num, det)
        messagebox.showinfo("Succès", f"Retrait effectué : {montant:.2f}.\nSolde actuel : {self.comptes[cle]:.2f}")

    def vider(self):
        num, det = self.obtenir_paire()
        if not self.valider_numero(num) or not self.valider_detenteur(det):
            messagebox.showerror("Erreur", "Validez Numéro et Détenteur avant de vider.")
            return
        cle = (num, det)
        if cle not in self.comptes:
            messagebox.showerror("Erreur", "Compte introuvable.")
            return
        self.comptes[cle] = 0.0 #remet solde a 0
        self.mettre_a_jour_solde_affichage(num, det)
        messagebox.showinfo("Succès", "Solde remis à 0.00")

    def reset(self):

        self.entry_num.delete(0, tk.END) #vide numero
        self.entry_detenteur.delete(0, tk.END) #vide detenteur
        self.affichage_solde.set("") #vide affichage_solde
        self.affichage_random.set("") #vide affichage_random
        self.civ.set("M")
        self.variable_gelee.set(False) #decoche la checkbox
        self.basculer_gelee() #applique etat non geler

    def basculer_gelee(self):
        gelee = self.variable_gelee.get() #True si cocher
        etat = "disabled" if gelee else "normal" # si geler = disabled sinon normal
        for w in self.gelables:
            if "state" in w.keys(): #verifie si le widget a l'option state
                w.configure(state=etat) #applique l'etat, donc soit normal ou disabled



if __name__ == "__main__":
    app = interface()
    app.mainloop()
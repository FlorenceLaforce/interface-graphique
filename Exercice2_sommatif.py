import tkinter as tk


class Calculatrice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("450x400")

        self.affichage = tk.StringVar()
        self.affichage.set("")

        self.creer_widgets()


    def creer_widgets(self):

        #
        frame2 = tk.Frame(bg="green") #frame pour ecran calculatrice
        frame2.pack(side="top", fill="both", padx =10, pady = 10, expand = True, anchor = "n")
        ecran = tk.Label(frame2, textvariable=self.affichage, width=10, height=5, border = 10, bg="pink", font = ("Arial", 12))
        ecran.pack(side="top", fill="both", expand=True)

        frame3 = tk.Frame(bg="blue") # 1er ligne bouton
        frame3.pack(side="top", fill="both", expand = True, anchor = "n")
        #boutons
        boutonC = tk.Button(frame3, text="C", width=15, height=2, fg="black", bg="lightcoral", border=2, command = self.zero)
        boutonC.pack(side="left", fill = "both", expand=True, anchor="w")
        bouton_diviser =tk.Button(frame3, text="/", width=15, height=2, fg="black", bg="lightcoral", border=2, command = lambda: self.ajouter_symbole("/"))
        bouton_diviser.pack(side="left", fill = "both", expand=True, anchor="w")
        bouton_etoile = tk.Button(frame3, text="*", width=15, height=2, fg="black", bg="lightcoral", border=2, command=lambda: self.ajouter_symbole("*"))
        bouton_etoile.pack(side="left", fill="both", expand=True, anchor="w")

        frame4 = tk.Frame(bg="orange") #2e ligne bouton
        frame4.pack(side="top", fill="both", expand = True)
        #boutons
        bouton7 = tk.Button(frame4, text="7", width=15, height=2, fg="black", bg="pink", border=2, command=lambda: self.ajouter_symbole("7"))
        bouton7.pack(side="left", fill="both", expand=True, anchor="w")
        bouton8 = tk.Button(frame4, text="8", width=15, height=2, fg="black", bg="pink", border=2, command=lambda: self.ajouter_symbole("8"))
        bouton8.pack(side="left", fill="both", expand=True, anchor="w")
        bouton9 = tk.Button(frame4, text="9", width=15, height=2, fg="black", bg="pink", border=2, command=lambda: self.ajouter_symbole("9"))
        bouton9.pack(side="left", fill="both", expand=True, anchor="w")
        bouton_moins = tk.Button(frame4, text="-", width=15, height=2, fg="black", bg="plum", border=2, command=lambda: self.ajouter_symbole("-"))
        bouton_moins.pack(side="left", fill="both", expand=True, anchor="w")

        frame5 = tk.Frame(bg="red")# 3e ligne bouton
        frame5.pack(side="top", fill="both", expand = True)
        #bouton
        bouton4 = tk.Button(frame5, text="4", width=15, height=2, fg="black", bg="pink", border=2,command=lambda: self.ajouter_symbole("4"))
        bouton4.pack(side="left", fill="both", expand=True, anchor="w")
        bouton5 = tk.Button(frame5, text="5", width=15, height=2, fg="black", bg="pink", border=2, command=lambda: self.ajouter_symbole("5"))
        bouton5.pack(side="left", fill="both", expand=True, anchor="w")
        bouton6 = tk.Button(frame5, text="6", width=15, height=2, fg="black", bg="pink", border=2, command=lambda: self.ajouter_symbole("6"))
        bouton6.pack(side="left", fill="both", expand=True, anchor="w")
        bouton_plus = tk.Button(frame5, text="+", width=15, height=2, fg="black", bg="plum", border=2, command=lambda: self.ajouter_symbole("+"))
        bouton_plus.pack(side="left", fill="both", expand=True, anchor="w")

        frame6 = tk.Frame(bg="green") # 4e ligne de bouton
        frame6.pack(side="top", fill="both", expand = True)
        #boutons
        bouton1 = tk.Button(frame6, text="1", width=15, height=2, fg="black", bg="pink", border=2, command=lambda: self.ajouter_symbole("1"))
        bouton1.pack(side="left", fill="both", expand=True, anchor="w")
        bouton2 = tk.Button(frame6, text="2", width=15, height=2, fg="black", bg="pink", border=2, command=lambda: self.ajouter_symbole("2"))
        bouton2.pack(side="left", fill="both", expand=True, anchor="w")
        bouton3 = tk.Button(frame6, text="3", width=15, height=2, fg="black", bg="pink", border=2, command=lambda: self.ajouter_symbole("3"))
        bouton3.pack(side="left", fill="both", expand=True, anchor="w")
        bouton_egal = tk.Button(frame6, text="=", width=15, height=2, fg="black", bg="plum", border=2, command=lambda: self.calculer())
        bouton_egal.pack(side="left", fill="both", expand=True, anchor="w")

        frame7 = tk.Frame(bg="orange")
        frame7.pack(side="top", fill="both", expand = True)
        #boutons
        bouton0 = tk.Button(frame7, text="0", width=15, height=2, fg="black", bg="lightcoral", border=2, command=lambda: self.ajouter_symbole("0"))
        bouton0.pack(side="left", fill="both", expand=True, anchor="w")
        bouton_point = tk.Button(frame7, text=".", width=15, height=2, fg="black", bg="lightcoral", border=2, command=lambda: self.ajouter_symbole("."))
        bouton_point.pack(side="left", fill="both", expand=True, anchor="w")

    def ajouter_symbole(self, symbole):
        chiffre = self.affichage.get()
        if chiffre == "0":
            self.affichage.set(symbole)
        else:
            self.affichage.set(chiffre + symbole)

    def zero(self):
        self.affichage.set("0") #reinisialiser la calculatrice a 0

    def calculer(self):
        """Évalue l'expression et affiche le résultat"""
        try:
            resultat = eval(self.affichage.get())  # ⚠ eval simple pour commencer
            self.affichage.set(str(resultat))
        except:
            self.affichage.set("Erreur")






if __name__ == "__main__":
    app = Calculatrice()
    app.mainloop()
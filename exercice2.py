import tkinter as tk

class interface2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulaire")
        self.geometry("700x200")
        self.creerwidgets()  # Appel de la méthode pour créer les widgets

    def creerwidgets(self):
        # Cadre principal
        frm = tk.Frame(self, bg="mistyrose", padx=5, pady=10, relief="solid", bd=1)
        frm.pack(fill="both", padx=5, pady=5, expand=True)

        # Sous-cadre à gauche
        frm2 = tk.Frame(frm, bg="lightcyan", padx=5, pady=10)
        frm2.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Ligne contenant le label et l'entrée du nom
        ligne_nom = tk.Frame(frm2, bg="plum", padx=5, pady=10)
        ligne_nom.pack(fill="x", pady=5)

        ligne_email = tk.Frame(frm2, bg="plum", padx=5, pady=10)
        ligne_email.pack(fill="x", pady=5)

        bouton_frm = tk.Frame(frm2, bg="plum", padx=5, pady=10)
        bouton_frm.pack( fill="x", pady=5)

        # Label "Nom:"
        nom = tk.Label(ligne_nom, text="Nom:", bg="plum")
        nom.pack(side="left")

        # Champ de saisie
        ent_nom = tk.Entry(ligne_nom)
        ent_nom.pack(side="left", fill="x", expand=True, padx=5)

        # Label "Nom:"
        email = tk.Label(ligne_email, text="Email::", bg="plum")
        email.pack(side="left")

        # Champ de saisie
        ent_email = tk.Entry(ligne_email)
        ent_email.pack(side="left", fill="x", expand=True, padx=5)

        tk.Button(bouton_frm, text = "valider").pack(side="right", fill="x", padx=5)

if __name__ == "__main__":
    app = interface2()
    app.mainloop()
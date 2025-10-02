import tkinter as tk
from tkinter import messagebox


class interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestionnaire de tâches")
        self.geometry("400x576")
        self.tasks = []

        self.creer_widgets()


    def  creer_widgets(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        #conteneur
        content = tk.Frame(self)
        content.grid(row=0, column=0, sticky="nsew")
        content.columnconfigure(0, weight=0)
        content.columnconfigure(1, weight=1)
        content.rowconfigure(7, weight=1)

        self.title = tk.Label(content, text="Ma To-Do List", font=("Arial", 20, "bold"))
        self.title.grid(row=0, column=0,columnspan=2, sticky="nsew")

        tache = tk.Label(content, text = "Taper la tâche à ajouter:")
        tache.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.champ_tache = tk.Entry(content)
        self.champ_tache.grid(row=1, column=1, sticky="ew", padx= 10, pady=10)

        durer = tk.Label(content, text = "Durée estimée de la tâche en minutes:")
        durer.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.champ_duree = tk.Entry(content)
        self.champ_duree.grid(row=2, column=1, sticky="ew", padx=10, pady=10)

        self.prioritaire = tk.BooleanVar(value=False)
        self.cb_prioritaire = tk.Checkbutton(content, text = "Toutes les nouvelles tâche sont prioritaires:", variable=self.prioritaire)
        self.cb_prioritaire.grid(row=3, column=0, columnspan=2, sticky="ew",padx = (5,10), pady=10)

        t_tache = tk.Label(content, text = "Choir le type de la tâche:")
        t_tache.grid(row=4, column=0, rowspan = 2, sticky="w", padx=(5,10) , pady=10)
        self.type_tache = tk.StringVar(value= "Personnel")
        self.rb1 = tk.Radiobutton(content, text = "Personnel", variable = self.type_tache, value = "Personnel")
        self.rb2 = tk.Radiobutton(content, text = "Professionel", variable = self.type_tache, value = "Professionel")
        self.rb1.grid(row = 4, column = 1, sticky="w")
        self.rb2.grid(row = 5, column = 1, sticky="w")

        self.btn_ajouter = tk.Button(content, text = "Ajouter la tâche",command=self.ajouter_tache, state = "disabled")
        self.btn_ajouter.grid(row = 6, column = 0,columnspan=2, pady = 30)

        self.liste_taches = tk.Listbox(content, height = 15)
        self.liste_taches.grid(row = 7, column = 0, columnspan = 2,sticky = "nsew",padx = 10,pady = 10)

    def valider_entree(self, nouvelle_valeur):
        if (nouvelle_valeur.isdigit() and 0 < int(nouvelle_valeur) < 480):
            return True
        return False

    def entree_invalide(self):
        self.bell()  # Feedback discret :
        messagebox.showwarning("EntrÃ©e invalide", "Veuillez entrer un entier positif")

    def validate_tache(self, *args):
        tache = self.champ_tache.get()
        duree = self.champ_duree.get()

        # Validation des champs
        tache_valid = len(tache) > 0
        duree_valid = len(duree) > 0

        if tache_valid and duree_valid:
            self.btn_ajouter.config(state="normal")
        else:
            self.btn_ajouter.config(state="disabled")

    def ajouter_tache(self):
        titre = self.champ_tache.get().strip()
        if not titre:
            messagebox.showwarning("Validation", "Veuillez saisir un titre de tache.")
            return

        task = {"titre": titre, "DurÃ©e": self.champ_duree.get(), "type": self.type_tache.get(),
                "prioritaire": self.prioritaire.get()}
        self.tasks.append(task)
        self._refresh_listbox()

    def _refresh_listbox(self):
        self.liste_taches.delete(0, "end")
        for t in self.tasks:
            self.liste_taches.insert("end", self._format_task_for_list(t))

    def _format_task_for_list(self, task):
        p = "[P]" if task["prioritaire"] else ""
        t = "[Prof]" if task["type"] == "Professionnel" else "[Pers]"

        return f"{p}{t}[{task["DurÃ©e"]}] {task['titre']}".strip()






if __name__ == "__main__":
    app = interface()
    app.mainloop()

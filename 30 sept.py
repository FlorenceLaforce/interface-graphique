import tkinter as tk

class interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestionnaire de tâches")
        self.geometry("400x576")

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
        self.champ_tache2 = tk.Entry(content)
        self.champ_tache2.grid(row=2, column=1, sticky="ew", padx=10, pady=10)

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

        self.bnt_ajouter = tk.Button(content, text = "Ajouter la tâche")
        self.bnt_ajouter.grid(row = 6, column = 0,columnspan=2, pady = 30)

        self.liste_tache = tk.Listbox(content, height = 15)
        self.liste_tache.grid(row = 7, column = 0, columnspan = 2,sticky = "nsew",padx = 10,pady = 10)








if __name__ == "__main__":
    app = interface()
    app.mainloop()

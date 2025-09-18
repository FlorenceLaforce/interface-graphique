import tkinter as tk

class interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestionnaire de tâches")
        self.geometry("400x576")

        self.creerwidgets()

    def creerwidgets(self):
        #frame
        frm = tk.Frame(self, borderwidth=1, relief="ridge")
        frm.pack(fill="x")

        #titre
        label = tk.Label(frm, text="Ma To-Do List", font=("Arial", 22, "bold"))
        label.pack()

        #entrer (input)
        ent = tk.Entry(frm,width=30)
        ent.pack(pady = 10)

        #bouton click
        btn = tk.Button(frm, text = "Ajouter la tâche", command = "on_click", state = "normal")
        btn.pack()

        #text box
        txt = tk.Text(frm, width=30, height=14, wrap="word", undo=True)
        txt.pack( padx=20, pady=15)

        # check button
        v_news = tk.BooleanVar(value=True)
        chk = tk.Checkbutton(frm,text = "Toute les tâches sont prioritaires", variable=v_news)
        chk.pack(anchor="center")

        #radio button
        civ = tk.StringVar(value="M")
        tk.Radiobutton(frm, text="Personnel", variable=civ, value="M", anchor="center").pack()
        tk.Radiobutton(frm, text="Professionel", variable=civ, value="f", anchor="center").pack()

        #titre 2
        label2 = tk.Label(frm, text="Notes sur la tâche sélectionnée:", font=("", 9))
        label2.pack(pady=10)

        #text box 2
        txt2 = tk.Text(frm, width=38, height=4, wrap="word", undo=True)
        txt2.pack(padx=20, pady=2)


if __name__ == "__main__":
    app = interface()
    app.mainloop()


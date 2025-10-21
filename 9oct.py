import tkinter as tk
from tkinter import ttk

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dessiner graphique")
        self.geometry("800x600")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.type_graphique = tk.StringVar(value="Linéaire")

        self.creer_widgets()
        self.creer_canvas()



    def creer_widgets(self):

        frm1 = ttk.Frame(self)
        frm1.grid(row=0, column=0, sticky="ew", padx=10, pady=10)


        lbl_type = ttk.Label(frm1, text="Sélectionner type graphique :")
        lbl_type.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        combo = ttk.Combobox(frm1, textvariable=self.type_graphique, values = ["Linéaire", "Nuage de point", "Barre"],
                             state="readonly")
        combo.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        btn = tk.Button(frm1, text = "Tracer", width= 10, command=lambda : self.update())
        btn.grid(row=0, column=2)


    def creer_canvas(self):

        self.fig = Figure(figsize=(5, 4))
        self.ax = self.fig.add_subplot()

        self.canvas = FigureCanvasTkAgg(self.fig)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column=0,row=1)

        #canvas_widget = canvas.get_tk_widget()
        #canvas_widget.grid(row=0, column=0, sticky="nsew")

    def update(self):
        x=np.linspace(0,10,100)
        y=np.sin(x)

        type_graphique = self.type_graphique.get()

        if type_graphique == "Linéaire":
            self.ax.plot(x,y, label="sin(x)", color="red")
            self.ax.set_title("Courbe linéaire")

        elif type_graphique == "Nuage de points":
            self.ax.scatter(x,y, label="Nuage de points", color="blue")
            self.ax.set_title("Courbe Nuage de points")

        elif type_graphique == "Barre":
            nom = ["Mathias","Aaron", "Mahé", "Martin"]
            age = [12,19,54,3]
            self.ax.barh(nom, age, color="green")
            self.ax.set_title("Courbe Barre")

        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.grid(True)
        self.ax.legend()

        self.canvas.draw()


if __name__ == "__main__":
    app = interface()
    app.mainloop()
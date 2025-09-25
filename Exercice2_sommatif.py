import tkinter as tk


class Calculatrice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("450x400")
        self.creer_widgets()

    def creer_widgets(self):

        frame2 = tk.Frame(bg="green") #frame pour ecran calculatrice
        frame2.pack(side="top", fill="x", padx =10, pady = 10, expand = True, anchor = "n")

        frame3 = tk.Frame(bg="blue") # bouton dedans
        frame3.pack(side="top", fill="both", expand = True, anchor = "n")

        frame4 = tk.Frame(bg="orange") #1er ligne bouton
        frame4.pack(side="bottom", fill="x", expand = True)

        frame5 = tk.Frame(bg="red")
        frame5.pack(side="bottom", fill="x", expand = True)

        frame6 = tk.Frame(bg="green")
        frame6.pack(side="bottom", fill="x", expand = True)


        ecran = tk.Entry(frame2, width=15, bg="pink", border=10)
        ecran.pack(side= "top", fill ="x", expand = True)

        boutonC = tk.Button(frame3, text="C",width=15, height=2, fg="black", bg="pink", border=2)
        boutonC.pack(side= "left",expand = True, anchor = "w")


if __name__ == "__main__":
    app = Calculatrice()
    app.mainloop()
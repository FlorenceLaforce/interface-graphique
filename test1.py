import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BON MATIN")
        self.geometry("1000x800")
        #self.configure(bg="light blue")
        frm = tk.Frame(self, borderwidth=2, relief="ridge")
        frm.pack(side= "top", fill="x")
        label = tk.Label(frm, text= "BIENVENUE", font = ("", 35), fg = "Darkmagenta")
        label.pack()
        frm_header = tk.LabelFrame(self, bg="light pink",text= "preference")
        frm_header.pack( fill="x", padx=15, pady=15)
        #ent = tk.Entry(frm_header)
        #ent.pack(fill="x", padx = 8)
        txt = tk.Text(frm_header, width= 40, height= 10, wrap = "word", undo=True)
        txt.pack(fill="both", expand=True, padx=15, pady=15)
        btn = tk.Button(frm, bg = "plum", text = "Satisfaction", command = "on_click", state = "normal")
        btn.pack()
        btn_2 = tk.Button(frm_header,bg = "plum", text = ";)", command = "on_click", state = "normal")
        btn_2.pack()
        frm_ppale = tk.Frame(self, bg="light pink")
        frm_ppale.pack(side = "bottom",fill="x")
        self.label = tk.Label(frm_ppale,
                              text = "PREFERENCES",
                              font = ("Arial", 35, "bold"),
                              fg= "mediumslateblue",bg = "hot pink",
                              height= 10, width= 10,
                              cursor = "heart",
                              anchor = "e")
        self.label.pack(side = "left", fill="x", expand = True, padx=10, pady=10)
        civ = tk.StringVar(value = "M")
        tk.Radiobutton(frm_ppale, text = "Aaron aime les bananes", variable = civ, value = "M").pack(anchor="w")
        tk.Radiobutton(frm_ppale, text = "Aaron n'aime pas les bananes", variable = civ, value = "f").pack(anchor="w")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
import tkinter as tk
import klase.korisnici

class ManagerTransportaPanel(tk.Frame):
    def __init__(self, parent,controler):
        tk.Frame.__init__(self,parent)
        nekiLabel = tk.Label(self, text="Ulogavani ste kao manager transporta")
        nekiLabel.grid()


class ManagerHangaraPanel(tk.Frame):
    def __init__(self, parent,controler):
        tk.Frame.__init__(self,parent)
        nekiLabel = tk.Label(self, text="Ulogovani ste kao manager hangara")
        nekiLabel.grid()
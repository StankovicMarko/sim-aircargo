import tkinter as tk
from tkinter import simpledialog

class Menibar(tk.Frame):

    def __init__(self, controler):
        tk.Frame.__init__(self, controler, relief="flat", bd=1)
        self.controler = controler
        self.menubar = tk.Menu(self)

        fileMenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Exit",command=self.exit)


        pretragaMenu = tk.Menu(self.menubar, tearoff=0)

        # SubMenus
        pretragaHangara = tk.Menu(self.menubar, tearoff=0)
        pretragaAviona = tk.Menu(self.menubar, tearoff=0)
        pretragaRobe = tk.Menu(self.menubar,tearoff=0)
        #

        self.menubar.add_cascade(label="Pretraga", menu=pretragaMenu)

        pretragaMenu.add_cascade(label="Hangari",menu=pretragaHangara)
        pretragaMenu.add_cascade(label="Avioni", menu=pretragaAviona)
        pretragaMenu.add_cascade(label="Roba", menu=pretragaRobe)

        # Commands za Pretraga Hangara Meni
        pretragaHangara.add_command(label="Oznaka")
        pretragaHangara.add_command(label="Naziv")
        pretragaHangara.add_command(label="Duzina")
        pretragaHangara.add_command(label="Sirina")
        pretragaHangara.add_command(label="Visina")


        # Commands za Pretraga Aviona Meni
        pretragaAviona.add_command(label="Oznaka")
        pretragaAviona.add_command(label="Duzina")
        pretragaAviona.add_command(label="Sirina")
        pretragaAviona.add_command(label="Raspon Krila")
        pretragaAviona.add_command(label="Nosivost")
        pretragaAviona.add_command(label="Relacija")


        # COmmands za Pretraga Robe Meni
        pretragaRobe.add_command(label="Oznaka")
        pretragaRobe.add_command(label="Naziv")
        pretragaRobe.add_command(label="Opis")
        pretragaRobe.add_command(label="Duzina")
        pretragaRobe.add_command(label="Sirina")
        pretragaRobe.add_command(label="Visina")
        pretragaRobe.add_command(label="Tezina")
        pretragaRobe.add_command(label="ID Potrazitelja", command=self.inputDialog)


        controler.config(menu=self.menubar)


    def inputDialog(self):
        self.input = simpledialog.askstring("Pretraga!","Unesite Pojam za Pretragu")
        self.pretragaPoIDPotrazitelja(self.input)



    def pretragaPoIDPotrazitelja(self,ID):
        z = self.controler.m.pretraziRobuPoIDPotrazitelja(ID)

    def exit(self):
        self.quit()
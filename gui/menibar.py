import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

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
        pretragaHangara.add_command(label="Oznaka",command=self.pretragaHangaraPoOznaci)
        pretragaHangara.add_command(label="Naziv",command=self.pretragaHangaraPoNazivu)
        pretragaHangara.add_command(label="Duzina",command=self.pretraziHangarePoDuzini)
        pretragaHangara.add_command(label="Sirina",command=self.pretragaHangaraPoSirini)
        pretragaHangara.add_command(label="Visina",command=self.pretragaHangaraPoVisini)


        # Commands za Pretraga Aviona Meni
        pretragaAviona.add_command(label="Oznaka",command=self.pretragaAvionaPoOznaci)
        pretragaAviona.add_command(label="Duzina",command=self.pretragaAvionaPoDuzini)
        pretragaAviona.add_command(label="Sirina",command=self.pretragaAvionaPoSirini)
        pretragaAviona.add_command(label="Raspon Krila",command=self.pretragaAvionaPoRasponuKrila)
        pretragaAviona.add_command(label="Nosivost",command=self.pretragaAvionaPoNosivosti)
        pretragaAviona.add_command(label="Relacija",command=self.pretragaAvionaPoRelaciji)


        # COmmands za Pretraga Robe Meni
        pretragaRobe.add_command(label="Oznaka",command=self.pretragaRobePoOznaci)
        pretragaRobe.add_command(label="Naziv",command=self.pretragaRobePoNazivu)
        pretragaRobe.add_command(label="Opis",command=self.pretragaRobePoOpisu)
        pretragaRobe.add_command(label="Duzina",command=self.pretragaRobePoDuzini)
        pretragaRobe.add_command(label="Sirina",command=self.pretragaRobePoSirini)
        pretragaRobe.add_command(label="Visina",command=self.pretragaRobePoVisini)
        pretragaRobe.add_command(label="Tezina",command=self.pretragaRobePoTezini)
        pretragaRobe.add_command(label="ID Potrazitelja", command=self.pretragaPoIDPotrazitelja)


        controler.config(menu=self.menubar)
        

    # Pretraga Hangara:
    def pretragaHangaraPoOznaci(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Oznaku Hangara za Pretragu")
        lista = self.controler.m.pretraziHangarePoOznaci(pojam)
        self.prikaz(lista)

    def pretragaHangaraPoNazivu(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Naziv Hangara za Pretragu")
        lista = self.controler.m.pretraziHangarePoNazivu(pojam)
        self.prikaz(lista)

    def pretraziHangarePoDuzini(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Duzinu Hangara za Pretragu")
        lista = self.controler.m.pretraziHangarePoDuzini(pojam)
        self.prikaz(lista)

    def pretragaHangaraPoSirini(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Sirinu Hangara za Pretragu")
        lista = self.controler.m.pretraziHangarePoSirini(pojam)
        self.prikaz(lista)

    def pretragaHangaraPoVisini(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Visinu Hangara za Pretragu")
        lista = self.controler.m.pretraziHangarePoVisini(pojam)
        self.prikaz(lista)

    # Pretraga Aviona:
    def pretragaAvionaPoOznaci(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Oznaku Aviona za Pretragu")
        lista = self.controler.m.pretraziAvionePoOznaci(pojam)
        self.prikaz(lista)

    def pretragaAvionaPoDuzini(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Duzinu Aviona za Pretragu")
        lista = self.controler.m.pretraziAvionePoDuzini(pojam)
        self.prikaz(lista)


    def pretragaAvionaPoSirini(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Sirinu Aviona za Pretragu")
        lista = self.controler.m.pretraziAvionePoSirini(pojam)
        self.prikaz(lista)

    def pretragaAvionaPoRasponuKrila(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Raspon Krila Aviona za Pretragu")
        lista = self.controler.m.pretraziAvionePoRasponKrila(pojam)
        self.prikaz(lista)

    def pretragaAvionaPoNosivosti(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Nosivost Aviona za Pretragu")
        lista = self.controler.m.pretraziAvionePoNosivosti(pojam)
        self.prikaz(lista)

    def pretragaAvionaPoRelaciji(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Relaciju Aviona za Pretragu")
        lista = self.controler.m.pretraziAvionePoRelaciji(pojam)
        self.prikaz(lista)

    # Pretraga Robe:
    def pretragaRobePoOznaci(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Oznaku Robe za Pretragu")
        lista = self.controler.m.pretraziRobuPoOznaci(pojam)
        self.prikaz(lista)

    def pretragaRobePoNazivu(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Naziv Robe za Pretragu")
        lista = self.controler.m.pretraziRobuPoNazivu(pojam)
        self.prikaz(lista)

    def pretragaRobePoOpisu(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Opis Robe za Pretragu")
        lista = self.controler.m.pretraziRobuPoOpisu(pojam)
        self.prikaz(lista)

    def pretragaRobePoDuzini(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Duzinu Robe za Pretragu")
        lista = self.controler.m.pretraziRobuPoDuzini(pojam)
        self.prikaz(lista)

    def pretragaRobePoSirini(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Sirinu Robe za Pretragu")
        lista = self.controler.m.pretraziRobuPoSirini(pojam)
        self.prikaz(lista)

    def pretragaRobePoVisini(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Visinu Robe za Pretragu")
        lista = self.controler.m.pretraziRobuPoVisini(pojam)
        self.prikaz(lista)

    def pretragaRobePoTezini(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite Tezina Robe za Pretragu")
        lista = self.controler.m.pretraziRobuPoTezini(pojam)
        self.prikaz(lista)

    def pretragaPoIDPotrazitelja(self):
        pojam = simpledialog.askstring("Pretraga!","Unesite ID Potrazitelja za Pretragu")
        lista = self.controler.m.pretraziRobuPoIDPotrazitelja(pojam)
        self.prikaz(lista)


    def prikaz(self,lista):
        if lista == []:
            messagebox.showerror("Error!","Pojam nije pronadjen!")
        else:
            window = tk.Toplevel(self)
            for i in lista:
                tk.Label(window,text=i).grid()


    def exit(self):
        self.quit()
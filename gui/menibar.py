import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from klase import aplikacija


class Menibar(tk.Frame):
    def __init__(self, controler):
        tk.Frame.__init__(self, controler, relief="flat", bd=1)
        self.controler = controler
        self.menubar = tk.Menu(self)

        # fileMenu = tk.Menu(self.menubar, tearoff=0)
        # self.menubar.add_cascade(label="File", menu=fileMenu)
        # fileMenu.add_command(label="Exit", command=self.exit)

        pretragaMenu = tk.Menu(self.menubar, tearoff=0)
        # prikaz_meni=tk.Menu(self.menubar, tearoff=0)

        # SubMenus
        pretragaHangara = tk.Menu(self.menubar, tearoff=0)
        pretragaAviona = tk.Menu(self.menubar, tearoff=0)
        pretragaRobe = tk.Menu(self.menubar, tearoff=0)
        #

        self.menubar.add_cascade(label="Pretraga", menu=pretragaMenu)
        # self.menubar.add_cascade(label='Prikazi...', menu=prikaz_meni)
        # prikaz_meni.add_command(label='Sve Hangare',command=self.prikaz_hangara)

        pretragaMenu.add_cascade(label="Hangari", menu=pretragaHangara)
        pretragaMenu.add_cascade(label="Avioni", menu=pretragaAviona)
        pretragaMenu.add_cascade(label="Roba", menu=pretragaRobe)

        # Commands za Pretraga Hangara Meni
        pretragaHangara.add_command(label="Oznaka", command=self.pretragaHangaraPoOznaci)
        pretragaHangara.add_command(label="Naziv", command=self.pretragaHangaraPoNazivu)
        pretragaHangara.add_command(label="Duzina", command=self.pretraziHangarePoDuzini)
        pretragaHangara.add_command(label="Sirina", command=self.pretragaHangaraPoSirini)
        pretragaHangara.add_command(label="Visina", command=self.pretragaHangaraPoVisini)

        # Commands za Pretraga Aviona Meni
        pretragaAviona.add_command(label="Oznaka", command=self.pretragaAvionaPoOznaci)
        pretragaAviona.add_command(label="Duzina", command=self.pretragaAvionaPoDuzini)
        pretragaAviona.add_command(label="Sirina", command=self.pretragaAvionaPoSirini)
        pretragaAviona.add_command(label="Raspon Krila", command=self.pretragaAvionaPoRasponuKrila)
        pretragaAviona.add_command(label="Nosivost", command=self.pretragaAvionaPoNosivosti)
        pretragaAviona.add_command(label="Relacija", command=self.pretragaAvionaPoRelaciji)

        # COmmands za Pretraga Robe Meni
        pretragaRobe.add_command(label="Oznaka", command=self.pretragaRobePoOznaci)
        pretragaRobe.add_command(label="Naziv", command=self.pretragaRobePoNazivu)
        pretragaRobe.add_command(label="Opis", command=self.pretragaRobePoOpisu)
        pretragaRobe.add_command(label="Duzina", command=self.pretragaRobePoDuzini)
        pretragaRobe.add_command(label="Sirina", command=self.pretragaRobePoSirini)
        pretragaRobe.add_command(label="Visina", command=self.pretragaRobePoVisini)
        pretragaRobe.add_command(label="Tezina", command=self.pretragaRobePoTezini)
        pretragaRobe.add_command(label="ID Potrazitelja", command=self.pretragaPoIDPotrazitelja)

        controler.config(menu=self.menubar)

    # Pretraga Hangara:
    def pretragaHangaraPoOznaci(self):
        """prikazuje sve hangare koji su u avionu, ako se unese rec all prikazuje SVE hangare"""
        oznaka = simpledialog.askstring("Pretraga!", "Unesite Oznaku Hangara za Pretragu ili rec 'all'")
        if oznaka is None:
            return
        elif oznaka == 'all':
            lista = [hangar for hangar in aplikacija.aerodrom]
        else:
            lista = self.controler.m.pretrazi_hangare_po_oznaci(oznaka)
        self.prikaz(lista)

    def pretragaHangaraPoNazivu(self):
        naziv = simpledialog.askstring("Pretraga!", "Unesite Naziv Hangara za Pretragu")
        if naziv is None:
            return
        else:
            lista = self.controler.m.pretrazi_hangare_po_nazivu(naziv)
        self.prikaz(lista)

    def pretraziHangarePoDuzini(self):
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Duzinu Hangara za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Duzinu Hangara za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretrazi_hangare_po_duzini(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaHangaraPoSirini(self):
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Hangara za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Hangara za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretrazi_hangare_po_sirini(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaHangaraPoVisini(self):
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Visinu Hangara za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Visinu Hangara za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretrazi_hangare_po_visini(donja_granica, gornja_granica)
        self.prikaz(lista)

    # Pretraga Aviona:
    def pretragaAvionaPoOznaci(self):
        """prikazuje sve avione, ako se unese rec all prikazuje SVE avione"""
        oznaka = simpledialog.askstring("Pretraga!", "Unesite Oznaku Aviona za Pretragu ili rec 'all'")
        if oznaka is None:
            return
        elif oznaka == 'all':
            lista = [avion for avion in aplikacija.avioni_u_hangarima]
            for avion in lista:
                print(avion)
            lista.extend([avion for avion in aplikacija.avioni_van_hangara])
        else:
            lista = self.controler.m.pretrazi_avine_po_oznaci(oznaka)
        self.prikaz(lista)

    def pretragaAvionaPoDuzini(self):
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Duzinu Aviona za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Duzinu Aviona za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretrazi_avione_po_duzini(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaAvionaPoSirini(self):
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Aviona za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Aviona za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretrazi_avione_po_sirini(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaAvionaPoRasponuKrila(self):
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Raspon Krila Aviona za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Raspon Krila Aviona za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretrazi_avione_po_raspon_krila(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaAvionaPoNosivosti(self):
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Nosivost Aviona za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Nosivnost Aviona za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretrazi_avione_po_nosivosti(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaAvionaPoRelaciji(self):
        pojam = simpledialog.askstring("Pretraga!", "Unesite Relaciju Aviona za Pretragu")
        if pojam is None:
            return
        else:
            lista = self.controler.m.pretrazi_avione_po_relaciji(pojam)
        self.prikaz(lista)

    # Pretraga Robe:
    def pretragaRobePoOznaci(self):
        oznaka = simpledialog.askstring("Pretraga!", "Unesite Oznaku Robe za Pretragu")
        if oznaka is None:
            return
        else:
            lista = self.controler.m.pretraziRobuPoOznaci(oznaka)
        self.prikaz(lista)

    def pretragaRobePoNazivu(self):
        naziv = simpledialog.askstring("Pretraga!", "Unesite Naziv Robe za Pretragu")
        if naziv is None:
            return
        else:
            lista = self.controler.m.pretraziRobuPoNazivu(naziv)
        self.prikaz(lista)

    def pretragaRobePoOpisu(self):
        opis = simpledialog.askstring("Pretraga!", "Unesite Opis Robe za Pretragu")
        if opis is None:
            return
        else:
            lista = self.controler.m.pretraziRobuPoOpisu(opis)
        self.prikaz(lista)

    def pretragaRobePoDuzini(self):
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Duzinu Robe za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Duzinu Robe za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretraziRobuPoDuzini(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaRobePoSirini(self):
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Robe za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Robe za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretraziRobuPoSirini(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaRobePoVisini(self):
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Robe za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Robe za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretraziRobuPoVisini(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaRobePoTezini(self):
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Robe za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Robe za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretraziRobuPoTezini(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaPoIDPotrazitelja(self):
        pojam = simpledialog.askstring("Pretraga!", "Unesite ID Potrazitelja za Pretragu")
        if pojam is None:
            return
        else:
            lista = self.controler.m.pretraziRobuPoIDPotrazitelja(pojam)
        self.prikaz(lista)

    # def prikaz_hangara(self):
    #     """Poziva funkciju prikaz koristeci list-comprehension za sve hangare u aerodromu"""
    #     self.prikaz([hangar for hangar in aplikacija.aerodrom])

    def prikaz(self, lista):
        """Pravi modalni prozor koji sadrzi tekst stvari koje se nalaze u listi, dugme prikazi
            entitete prikazuje sadrzaj entiteta npr: prikazani su hangari, kliknemo na neki pa onda
            dugme dobicemo sve avione koji se nalaze u tom hangaru."""
        if not lista:
            messagebox.showerror("Error!", "Pojam nije pronadjen!")
        else:
            window = tk.Toplevel(self)
            window.transient(self)
            window.grab_set()
            scrollbary = tk.Scrollbar(window)
            scrollbary.pack(side='right', fill='y')
            scrollbarx = tk.Scrollbar(window, orient='horizontal')
            scrollbarx.pack(side='bottom', fill='x')
            lb = tk.Listbox(window, width=100)
            b = tk.Button(window, text="Prikazi sadrzaj",
                          command=lambda: prikaz_sadrzaja_entiteta(lb, lista))
            b.pack()

            lb.pack(side="left", fill="both", expand=True)
            for index, element in enumerate(lista):
                lb.insert(index, element)

            lb.config(yscrollcommand=scrollbary.set)
            scrollbary.config(command=lb.yview)

            lb.config(xscrollcommand=scrollbarx.set)
            scrollbarx.config(command=lb.xview)

        def prikaz_sadrzaja_entiteta(lb, lista):
            try:
                index_entiteta=lb.curselection()[0]
                lista_sadrzaja=[]

                for sadrzaj in lista[index_entiteta]:
                    lista_sadrzaja.append(sadrzaj)

                self.prikaz(lista_sadrzaja)
            except:
                tk.messagebox.showerror('Greska', 'Morate odabrati u sta zelite da pogledate')

    # def exit(self):
    #     self.quit()

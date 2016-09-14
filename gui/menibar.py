import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from klase import aplikacija


class Menibar(tk.Frame):
    """
    Ova klasa inicijalizuje menije
    """
    def __init__(self, controler):
        tk.Frame.__init__(self, controler, relief="flat", bd=1)
        self.controler = controler
        self.menubar = tk.Menu(self)

        pretragaMenu = tk.Menu(self.menubar, tearoff=0)

        # SubMenus
        pretragaHangara = tk.Menu(self.menubar, tearoff=0)
        pretragaAviona = tk.Menu(self.menubar, tearoff=0)
        pretragaRobe = tk.Menu(self.menubar, tearoff=0)
        #

        self.menubar.add_cascade(label="Search", menu=pretragaMenu)

        pretragaMenu.add_cascade(label="Hangars", menu=pretragaHangara)
        pretragaMenu.add_cascade(label="Airports", menu=pretragaAviona)
        pretragaMenu.add_cascade(label="Cargo", menu=pretragaRobe)

        # Commands za Pretraga Hangara Meni
        pretragaHangara.add_command(label="Oznaka(ID)", command=self.pretragaHangaraPoOznaci)
        pretragaHangara.add_command(label="Naziv(Name)", command=self.pretragaHangaraPoNazivu)
        pretragaHangara.add_command(label="Duzina(Len)", command=self.pretraziHangarePoDuzini)
        pretragaHangara.add_command(label="Sirina(Width)", command=self.pretragaHangaraPoSirini)
        pretragaHangara.add_command(label="Visina(Height)", command=self.pretragaHangaraPoVisini)

        # Commands za Pretraga Aviona Meni
        pretragaAviona.add_command(label="Oznaka(ID)", command=self.pretragaAvionaPoOznaci)
        pretragaAviona.add_command(label="Duzina(Len)", command=self.pretragaAvionaPoDuzini)
        pretragaAviona.add_command(label="Sirina(Width)", command=self.pretragaAvionaPoSirini)
        pretragaAviona.add_command(label="Raspon Krila(WingSpan)", command=self.pretragaAvionaPoRasponuKrila)
        pretragaAviona.add_command(label="Nosivost(Capacity)", command=self.pretragaAvionaPoNosivosti)
        pretragaAviona.add_command(label="Relacija(Dest)", command=self.pretragaAvionaPoRelaciji)

        # COmmands za Pretraga Robe Meni
        pretragaRobe.add_command(label="Oznaka(ID)", command=self.pretragaRobePoOznaci)
        pretragaRobe.add_command(label="Naziv(Name)", command=self.pretragaRobePoNazivu)
        pretragaRobe.add_command(label="Opis(Desc)", command=self.pretragaRobePoOpisu)
        pretragaRobe.add_command(label="Duzina(Len)", command=self.pretragaRobePoDuzini)
        pretragaRobe.add_command(label="Sirina(Width)", command=self.pretragaRobePoSirini)
        pretragaRobe.add_command(label="Visina(Height)", command=self.pretragaRobePoVisini)
        pretragaRobe.add_command(label="Tezina(Weigt)", command=self.pretragaRobePoTezini)
        pretragaRobe.add_command(label="ID Potrazitelja(Claimant ID) ", command=self.pretragaPoIDPotrazitelja)

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
        """
        Pretrazuje i prikazuje sve hangare po nazivu
        """
        naziv = simpledialog.askstring("Pretraga!", "Unesite Naziv Hangara za Pretragu")
        if naziv is None:
            return
        else:
            lista = self.controler.m.pretrazi_hangare_po_nazivu(naziv)
        self.prikaz(lista)

    def pretraziHangarePoDuzini(self):
        """
        Pretrazuje i prikazuje sve hangare po duzini
        """
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Duzinu Hangara za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Duzinu Hangara za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretrazi_hangare_po_duzini(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaHangaraPoSirini(self):
        """
        Pretrazuje i prikazuje sve hangare po sirini
        """
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Hangara za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Hangara za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretrazi_hangare_po_sirini(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaHangaraPoVisini(self):
        """
        Pretrazuje i prikazuje sve hangare po visini
        """
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
            lista.extend([avion for avion in aplikacija.avioni_van_hangara])
        else:
            lista = self.controler.m.pretrazi_avine_po_oznaci(oznaka)
        self.prikaz(lista)

    def pretragaAvionaPoDuzini(self):
        """
        Pretrazuje i prikazuje sve avione po duzini
        """
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Duzinu Aviona za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Duzinu Aviona za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretrazi_avione_po_duzini(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaAvionaPoSirini(self):
        """
        Pretrazuje i prikazuje sve avione po sirini
        """
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Aviona za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Aviona za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretrazi_avione_po_sirini(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaAvionaPoRasponuKrila(self):
        """
        Pretrazuje i prikazuje sve avione po rasponu krila
        """
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Raspon Krila Aviona za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Raspon Krila Aviona za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretrazi_avione_po_raspon_krila(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaAvionaPoNosivosti(self):
        """
        Pretrazuje i prikazuje sve avione po nosivosti
        """
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Nosivost Aviona za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Nosivnost Aviona za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretrazi_avione_po_nosivosti(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaAvionaPoRelaciji(self):
        """
        Pretrazuje i prikazuje sve avione po relaciji
        """
        pojam = simpledialog.askstring("Pretraga!", "Unesite Relaciju Aviona za Pretragu")
        if pojam is None:
            return
        else:
            lista = self.controler.m.pretrazi_avione_po_relaciji(pojam)
        self.prikaz(lista)

    # Pretraga Robe:
    def pretragaRobePoOznaci(self):
        """
        Pretrazuje i prikazuje svu robu po oznaci
        """
        oznaka = simpledialog.askstring("Pretraga!", "Unesite Oznaku Robe za Pretragu")
        if oznaka is None:
            return
        else:
            lista = self.controler.m.pretraziRobuPoOznaci(oznaka)
        self.prikaz(lista)

    def pretragaRobePoNazivu(self):
        """
        Pretrazuje i prikazuje svu robu po nazivu
        """
        naziv = simpledialog.askstring("Pretraga!", "Unesite Naziv Robe za Pretragu")
        if naziv is None:
            return
        else:
            lista = self.controler.m.pretraziRobuPoNazivu(naziv)
        self.prikaz(lista)

    def pretragaRobePoOpisu(self):
        """
        Pretrazuje i prikazuje svu robu po opisu
        """
        opis = simpledialog.askstring("Pretraga!", "Unesite Opis Robe za Pretragu")
        if opis is None:
            return
        else:
            lista = self.controler.m.pretraziRobuPoOpisu(opis)
        self.prikaz(lista)

    def pretragaRobePoDuzini(self):
        """
        Pretrazuje i prikazuje svu robu po duzini
        """
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Duzinu Robe za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Duzinu Robe za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretraziRobuPoDuzini(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaRobePoSirini(self):
        """
        Pretrazuje i prikazuje svu robu po sirini
        """
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Robe za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Robe za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretraziRobuPoSirini(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaRobePoVisini(self):
        """
        Pretrazuje i prikazuje svu robu po visini
        """
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Robe za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Robe za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretraziRobuPoVisini(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaRobePoTezini(self):
        """
        Pretrazuje i prikazuje svu robu po tezini
        """
        donja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Robe za Pretragu(donju granicu)")
        gornja_granica = simpledialog.askinteger("Pretraga!", "Unesite Sirinu Robe za Pretragu(gornju granicu)")
        if gornja_granica is None or donja_granica is None:
            return
        else:
            lista = self.controler.m.pretraziRobuPoTezini(donja_granica, gornja_granica)
        self.prikaz(lista)

    def pretragaPoIDPotrazitelja(self):
        """
        Pretrazuje i prikazuje svu robu po id-ju potrazitelja
        """
        pojam = simpledialog.askstring("Pretraga!", "Unesite ID Potrazitelja za Pretragu")
        if pojam is None:
            return
        else:
            lista = self.controler.m.pretraziRobuPoIDPotrazitelja(pojam)
        self.prikaz(lista)

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
                lb.insert(index, str(element))

            lb.config(yscrollcommand=scrollbary.set)
            scrollbary.config(command=lb.yview)

            lb.config(xscrollcommand=scrollbarx.set)
            scrollbarx.config(command=lb.xview)

        def prikaz_sadrzaja_entiteta(lb, lista):
            """
            Prikazuje sadrzaj entiteta
            """
            try:
                index_entiteta=lb.curselection()[0]
                lista_sadrzaja=[]

                for sadrzaj in lista[index_entiteta]:
                    lista_sadrzaja.append(sadrzaj)

                self.prikaz(lista_sadrzaja)
            except:
                tk.messagebox.showerror('Greska', 'Morate odabrati u sta zelite da pogledate')

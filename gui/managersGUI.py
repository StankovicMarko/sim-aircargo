import tkinter as tk
import klase.korisnici
import gui.windows
import klase.util_funk as util
from klase import hangar_funkcionalnosti
import tkinter.messagebox


class ManagerTransportaPanel(tk.Frame):
    def __init__(self, parent, controler):
        tk.Frame.__init__(self, parent)
        self.controler = controler
        self.createWidgets()
        # self.prikaZahtevaHeaderWidgets()

    def createWidgets(self):
        welcomeLabel = tk.Label(self, text="Ulogavani ste kao manager transporta")
        welcomeLabel.grid(row=0, column=1)

        self.prikazTransportButton = tk.Button(self, text="Transport Robe", command=self.prikazZahtevaTransportWidgets)
        self.prikazSmestanjeButton = tk.Button(self, text="Smestanje Aviona",
                                               command=self.prikazZahtevaSmestanjeWidgets)

        self.prikazTransportButton.grid(row=1, column=0)
        self.prikazSmestanjeButton.grid(row=1, column=2)

        self.frejmZahtevi = tk.Frame(self, bd=1, relief="solid")
        self.frejmZahtevi.grid(columnspan=3)
        self.logoutButton = tk.Button(self, text="Log Out!", command=self.logout)
        self.logoutButton.grid(column=1)

    def function(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def prikaZahtevaHeaderWidgets(self):
        self.headerFrame = tk.Frame(self.frejmZahtevi)
        self.headerFrame.grid(row=0, column=0)
        self.zahtevID = tk.Label(self.headerFrame, text="ID").grid(row=0, column=0)
        tk.Label(self.headerFrame, text="      ").grid(row=0, column=1)
        self.datumkreiranja = tk.Button(self.headerFrame, text="Datum Kreiranja", relief="flat",
                                        command=lambda: self.sortedPrikaz(1)).grid(row=0, column=2)
        self.datumTransporta = tk.Button(self.headerFrame, text="Datum Transpota", relief="flat",
                                         command=lambda: self.sortedPrikaz(2)).grid(row=0, column=3)
        self.odredite = tk.Label(self.headerFrame, text="  Odrediste  ").grid(row=0, column=4)
        self.idPotrazitelja = tk.Label(self.headerFrame, text="Potrazitelj").grid(row=0, column=5)
        self.oznakaAviona = tk.Label(self.headerFrame, text="  Avion  ").grid(row=0, column=6)
        self.status = tk.Button(self.headerFrame, text="Status", relief="flat",
                                command=lambda: self.sortedPrikaz(3)).grid(row=0, column=7)
        self.odobirZahtev = tk.Label(self.headerFrame, text="Odobri").grid(row=0, column=8)

    def prikazZahtevaTransportWidgets(self):
        try:
            self.znj1.destroy()
        except:
            pass

        self.prikaZahtevaHeaderWidgets()
        self.canvas = tk.Canvas(self.frejmZahtevi, bg="red", width=619)
        self.scrollbar = tk.Scrollbar(self.frejmZahtevi, orient="vertical", command=self.canvas.yview)
        self.newFrejm = tk.Frame(self.canvas, bd=1, relief="solid")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.grid(row=0, rowspan=2, column=9, sticky="ns")
        self.canvas.grid(row=1, columnspan=9, sticky="nsew")
        self.canvas.create_window((0, 0), window=self.newFrejm, anchor='n')
        self.newFrejm.bind("<Configure>", self.function)

        self.prikazTransportButton.config(state="disabled")
        self.prikazSmestanjeButton.config(state="normal")

        self.prikaz(self.controler.m.prikazZahteva())

    def prikaz(self, lista):
        self.priv = []
        r = -1
        for i in lista:
            r += 1
            a = tk.Label(self.newFrejm, text=i[0])
            a.grid(row=r, column=0, sticky="w")
            self.priv.append(a)  # Dodaje svaki objekat u listu da bi kasnije znao sta da obrise
            a1 = tk.Label(self.newFrejm, text="   ")
            a1.grid(row=r, column=1)
            self.priv.append(a1)
            a2 = tk.Label(self.newFrejm, text=i[1])
            a2.grid(row=r, column=2)
            self.priv.append(a2)
            a3 = tk.Label(self.newFrejm, text="              ")
            a3.grid(row=r, column=3)
            self.priv.append(a3)
            a4 = tk.Label(self.newFrejm, text=i[2])
            a4.grid(row=r, column=4)
            self.priv.append(a4)
            a5 = tk.Label(self.newFrejm, text="           ")
            a5.grid(row=r, column=5)
            self.priv.append(a5)
            a6 = tk.Label(self.newFrejm, text=i[3])
            a6.grid(row=r, column=6)
            self.priv.append(a6)
            a7 = tk.Label(self.newFrejm, text="      ")
            a7.grid(row=r, column=7)
            self.priv.append(a7)
            a8 = tk.Label(self.newFrejm, text=i[4])
            a8.grid(row=r, column=8, sticky="w")
            self.priv.append(a8)
            a9 = tk.Label(self.newFrejm, text="  ")
            a9.grid(row=r, column=9)
            self.priv.append(a9)
            a10 = tk.Label(self.newFrejm, text=i[5])
            a10.grid(row=r, column=10)
            self.priv.append(a10)
            a14 = tk.Label(self.newFrejm, text="   ")
            a14.grid(row=r, column=11)
            self.priv.append(a14)
            a11 = tk.Label(self.newFrejm, text=i[6])
            a11.grid(row=r, column=12)
            self.priv.append(a11)
            a12 = tk.Label(self.newFrejm, text="   ")
            a12.grid(row=r, column=13)
            self.priv.append(a12)
            a13 = tk.Checkbutton(self.newFrejm, text="")
            a13.grid(row=r, column=14)
            self.priv.append(a13)
            a15 = tk.Label(self.newFrejm, text=" ")
            a15.grid(row=r, column=15)
            self.priv.append(a15)

    def sortedPrikaz(self, broj):
        for p in self.priv:
            p.destroy()

        if broj == 1:
            self.prikaz(util.sortPoDatumuKreiranja(self.controler.m.prikazZahteva()))
        elif broj == 2:
            self.prikaz(util.sortPoDatumuRealizacije(self.controler.m.prikazZahteva()))
        elif broj == 3:
            self.prikaz(util.sortPoStatusu(self.controler.m.prikazZahteva()))

    def prikazZahtevaSmestanjeWidgets(self):
        self.headerFrame.destroy()
        self.canvas.destroy()
        self.prikazTransportButton.config(state="normal")
        self.prikazSmestanjeButton.config(state="disabled")
        self.znj1 = tk.Label(self.frejmZahtevi, text="hello1")
        self.znj1.grid(sticky="nsew")

    def logout(self):
        self.headerFrame.destroy()
        self.canvas.destroy()
        self.controler.meni.destroy()
        self.controler.show_frame(gui.windows.LoginWindow)


class ManagerHangaraPanel(tk.Frame):
    def __init__(self, parent, controler):
        tk.Frame.__init__(self, parent)
        nekiLabel = tk.Label(self, text="Ulogovani ste kao manager hangara")
        nekiLabel.grid()
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=2, columnspan=10, sticky='nsew')
        self.temp_duzina =0
        self.temp_sirina =0
        self.temp_visina =0

        self.create_widgets()

    def create_widgets(self):
        dug_smestanje = tk.Button(self, text="Zahtevi za smestanje aviona", command=self.zahtevi_smestanja)
        dug_smestanje.grid(row=1, column=0)

        dug_transport = tk.Button(self, text="Zahtevi za transport aviona", command=self.zahtevi_transport)
        dug_transport.grid(row=1, column=1)

        dug_dodaj_hangar = tk.Button(self, text='Dodaj hangar', command=self.add_hangar)
        dug_dodaj_hangar.grid(row=1, column=2)

        dug_dodaj_avion = tk.Button(self, text='Napravi avion', command=self.add_avion)
        dug_dodaj_avion.grid(row=1, column=3)

    def zahtevi_smestanja(self):
        zahtevi = hangar_funkcionalnosti.prikazi_zahteve_za_smestanje_aviona()
        lista_zahteva = zahtevi.split('\n')
        self.listbox.delete(0, self.listbox.size())
        for i, zahtev in enumerate(lista_zahteva):
            self.listbox.insert(i, zahtev)

    def zahtevi_transport(self):
        zahtevi = hangar_funkcionalnosti.prikaz_zahteva_za_transport_robe()
        lista_zahteva = zahtevi.split('\n')
        self.listbox.delete(0, self.listbox.size())
        for i, zahtev in enumerate(lista_zahteva):
            self.listbox.insert(i, zahtev)

    def add_hangar(self):
        top = tk.Toplevel()
        top.transient(self)
        top.grab_set()
        tk.Label(top, text='Naziv Hangara').grid(row=0, column=0)
        tk.Label(top, text='Duzina Hangara').grid(row=1, column=0)
        tk.Label(top, text='Sirina Hangara').grid(row=2, column=0)
        tk.Label(top, text='Visina Hangara').grid(row=3, column=0)

        entry_naziv = tk.Entry(top)
        entry_duzina = tk.Entry(top)
        entry_sirina = tk.Entry(top)
        entry_visina = tk.Entry(top)

        entry_naziv.grid(row=0, column=1)
        entry_duzina.grid(row=1, column=1)
        entry_sirina.grid(row=2, column=1)
        entry_visina.grid(row=3, column=1)

        dodaj_bnt = tk.Button(top, text='DODAJ',
                              command=lambda: self._pokupi_inpute_hangara(entry_naziv, entry_duzina, entry_sirina,
                                                                          entry_visina, top))
        dodaj_bnt.grid(row=4, columnspan=2, sticky='new')

    def add_avion(self):
        top = tk.Toplevel()
        top.transient(self)
        top.grab_set()
        tk.Label(top, text='Naziv Aviona').grid(row=0, column=0)
        tk.Label(top, text='Duzina Aviona').grid(row=1, column=0)
        tk.Label(top, text='Sirina Aviona').grid(row=2, column=0)
        tk.Label(top, text='Visina Aviona').grid(row=3, column=0)
        tk.Label(top, text='Raspon krila Aviona').grid(row=4, column=0)
        tk.Label(top, text='Godiste Aviona').grid(row=5, column=0)
        tk.Label(top, text='Nosivost Aviona').grid(row=6, column=0)
        tk.Label(top, text='Relacija Avion').grid(row=7, column=0)

        entry_naziv = tk.Entry(top)
        entry_duzina = tk.Entry(top)
        entry_sirina = tk.Entry(top)
        entry_visina = tk.Entry(top)
        entry_raspon_krila = tk.Entry(top)
        entry_godiste = tk.Entry(top)
        entry_nosivost = tk.Entry(top)
        entry_relacija = tk.Entry(top)

        entry_naziv.grid(row=0, column=1)
        entry_duzina.grid(row=1, column=1)
        entry_sirina.grid(row=2, column=1)
        entry_visina.grid(row=3, column=1)
        entry_raspon_krila.grid(row=4, column=1)
        entry_godiste.grid(row=5, column=1)
        entry_nosivost.grid(row=6, column=1)
        entry_relacija.grid(row=7, column=1)

        self.lbl_pzt = tk.Label(top, text='(prazno)')
        self.lbl_pzt.grid(row=8, column=1)

        self.btn_add_avion = tk.Button(top, text='Dodaj Avion',
                                       command=lambda: self._prikupi_inpute_aviona(entry_naziv, entry_duzina,
                                                                                   entry_sirina,
                                                                                   entry_visina,
                                                                                   entry_raspon_krila,
                                                                                   entry_godiste,
                                                                                   entry_nosivost,
                                                                                   entry_relacija, top))

        tk.Button(top, text='Dodaj Prostor za Teret', command=lambda: self.add_pzt(entry_naziv, entry_duzina,
                                                                                   entry_sirina,
                                                                                   entry_visina,
                                                                                   entry_raspon_krila,
                                                                                   entry_godiste,
                                                                                   entry_nosivost,
                                                                                   entry_relacija)).grid(row=8,
                                                                                                         column=0)

    def add_pzt(self, en, ed, es, ev, erk, eg, eno, er):
        en.config(state='disabled')
        ed.config(state='disabled')
        es.config(state='disabled')
        ev.config(state='disabled')
        erk.config(state='disabled')
        eg.config(state='disabled')
        eno.config(state='disabled')
        er.config(state='disabled')
        if self.temp_duzina==0:
            self.temp_duzina = int(ed.get())
            self.temp_sirina = int(es.get())
            self.temp_visina = int(ev.get())

        top = tk.Toplevel()
        top.transient(self)
        top.grab_set()
        tk.Label(top, text='Naziv Prostora za Teret').grid(row=0, column=0)
        tk.Label(top, text='Duzina Prostora za Teret').grid(row=1, column=0)
        tk.Label(top, text='Sirina Prostora za Teret').grid(row=2, column=0)
        tk.Label(top, text='Visina Prostora za Teret').grid(row=3, column=0)

        entry_naziv = tk.Entry(top)
        entry_duzina = tk.Entry(top)
        entry_sirina = tk.Entry(top)
        entry_visina = tk.Entry(top)

        entry_naziv.grid(row=0, column=1)
        entry_duzina.grid(row=1, column=1)
        entry_sirina.grid(row=2, column=1)
        entry_visina.grid(row=3, column=1)

        dodaj_bnt = tk.Button(top, text='DODAJ',
                              command=lambda: self._pokupi_inpute_pzt(entry_naziv, entry_duzina, entry_sirina,
                                                                      entry_visina, top))
        dodaj_bnt.grid(row=4, columnspan=2, sticky='new')

    def _pokupi_inpute_hangara(self, en, ed, es, ev, top):
        naziv = en.get()
        duzina = ed.get()
        sirina = es.get()
        visina = ev.get()

        if util.proveraInputa(naziv) and util.proveraInputaBroj(duzina) and util.proveraInputaBroj(
                sirina) and util.proveraInputaBroj(visina):
            hangar_funkcionalnosti.napravi_hangar(naziv, int(duzina), int(sirina), int(visina))
            tk.messagebox.showinfo('Dodavanje hangara u aerodrom', 'Uspesno dodat hangar')
            top.destroy()
        else:
            tk.messagebox.showerror('Invalid inputs', 'Molimo unesite validne inpute str/int/int/int')

    def _prikupi_inpute_aviona(self, en, ed, es, ev, erk, eg, eno, er, top):
        naziv = en.get()
        duzina = ed.get()
        sirina = es.get()
        visina = ev.get()
        raspon_krila = erk.get()
        godiste = eg.get()
        nosivost = eno.get()
        relacija = er.get()
        if util.proveraInputa(naziv) \
                and util.proveraInputaBroj(duzina) \
                and util.proveraInputaBroj(sirina) \
                and util.proveraInputaBroj(visina) \
                and util.proveraInputa(raspon_krila) \
                and util.proveraInputa(godiste) \
                and util.proveraInputa(nosivost) \
                and util.proveraInputa(relacija):
            hangar_funkcionalnosti.napravi_avion(naziv,
                                                 int(duzina),
                                                 int(sirina),
                                                 int(visina),
                                                 int(raspon_krila),
                                                 int(godiste),
                                                 int(nosivost),
                                                 relacija)
            tk.messagebox.showinfo('Narucivanje aviona', 'Uspesno napravljen avion')
            top.destroy()
        else:
            tk.messagebox.showerror('Invalid inputs',
                                    'Molimo unesite validne inpute str/int/int/int/int/int/int/str')

    def _pokupi_inpute_pzt(self, en, ed, es, ev, top):
        naziv = en.get()
        duzina = ed.get()
        sirina = es.get()
        visina = ev.get()

        if util.proveraInputa(naziv) and util.proveraInputaBroj(duzina) and util.proveraInputaBroj(
                sirina) and util.proveraInputaBroj(visina) \
                and int(duzina) < self.temp_duzina and int(sirina) < self.temp_sirina \
                and int(visina) < self.temp_visina:
            hangar_funkcionalnosti.napravi_prostor_za_robu(naziv, int(duzina), int(sirina), int(visina))
            self.temp_duzina -= int(duzina)
            tk.messagebox.showinfo('Dodavanje Prostora za Teret u Avion', 'Uspesno dodat Prostor za Teret')
            top.destroy()

            imena_prostora=''
            for prostor in hangar_funkcionalnosti.temp_prostor_za_robu:
                imena_prostora+=prostor.naziv+' '
            self.lbl_pzt.config(text=imena_prostora)

            self.btn_add_avion.grid(row=9, columnspan=2, sticky='nsew')

        else:
            tk.messagebox.showerror('Invalid inputs',
                                    'Molimo unesite validne inpute str/int/int/int ili manje dimenzije')


    #dodaj zahtev
            #list box u petlji insert str(avion)
            #imam dugme dodaj zahtev
            #salje id i kreira zahtev

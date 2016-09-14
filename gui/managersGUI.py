import tkinter as tk
import gui.windows
import klase.util_funk as util
from klase import aplikacija
import tkinter.messagebox
import copy


class ManagerTransportaPanel(tk.Frame):
    """
    Predstavlja klasu koja se kreira pri logovanju korisnika, poziva funkije koje su locirane u
    modulu aplikacija. Ova klasa sluzi samo za graficki prikaz onoga sto menadzer transporta moze da uradi
    """

    def __init__(self, parent, controler):
        tk.Frame.__init__(self, parent)
        self.controler = controler
        self.createWidgets()
        # self.prikaZahtevaHeaderWidgets()

    def createWidgets(self):
        """
        kreira potrebne widget-e (dugmice, labele, frejmove...) da bi prozor bio funkcionalan
        """
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
        self.logoutButton.grid(row=4, column=1)

    def function(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def prikaZahtevaHeaderWidgets(self):
        """
        Inicijalizuje potrebne widgete za prikaz header-a tabele
        """
        self.headerFrame = tk.Frame(self.frejmZahtevi)
        self.headerFrame.grid(row=0, column=0)
        self.zahtevID = tk.Label(self.headerFrame, text="{:^10}".format("ID")).grid(row=0, column=0)
        self.datumkreiranja = tk.Button(self.headerFrame, text="{:^10}".format("Datum Kreiranja"), relief="flat",
                                        command=lambda: self.sortedPrikaz(1)).grid(row=0, column=2)
        self.datumTransporta = tk.Button(self.headerFrame, text="{:^10}".format("Datum Transporta"), relief="flat",
                                         command=lambda: self.sortedPrikaz(2)).grid(row=0, column=3)
        self.odredite = tk.Label(self.headerFrame, text="{:^10}".format("Odrediste")).grid(row=0, column=4)
        self.idPotrazitelja = tk.Label(self.headerFrame, text="{:^12}".format("Potrazitelj")).grid(row=0, column=5)
        self.oznakaAviona = tk.Label(self.headerFrame, text="{:^15}".format("Avion")).grid(row=0, column=6)
        self.status = tk.Button(self.headerFrame, text="{:^16}".format("Status"), relief="flat",
                                command=lambda: self.sortedPrikaz(3)).grid(row=0, column=7)
        self.odobirZahtev = tk.Label(self.headerFrame, text="Odobri").grid(row=0, column=8)

    def prikazZahtevaTransportWidgets(self):
        """
        Inicijalizacija svih widgeta potrebnih za prikaz tabele zahteva za transport
        """
        try:
            self.listboxZahteviZaSmestanje.destroy()
            self.scrollbarx.destroy()
            self.scrollbary.destroy()

        except:
            pass

        self.prikaZahtevaHeaderWidgets()
        self.canvas = tk.Canvas(self.frejmZahtevi, width=680)
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
        """
        Kreiramo jednu listu i stavljamo je u recnik pod kljuc counter, i tako joj posle pristupamo
        """
        self.recnik = {}  # ovde cuvamo sve checkbox-ove, "counter":"i"
        self.checkboxovi = []
        counter = -1  # izracunava koji je redni broj checkbox-a
        self.priv = []
        r = -1
        for i in lista:
            counter += 1
            r += 1
            a = tk.Label(self.newFrejm, text="{:^10}".format(i[0][3:]))
            a.grid(row=r, column=0, sticky="w")
            self.priv.append(a)  # Dodaje svaki objekat u listu da bi kasnije znao sta da obrise

            a2 = tk.Label(self.newFrejm, text="{:^22}".format(i[1]))
            a2.grid(row=r, column=2)
            self.priv.append(a2)

            a4 = tk.Label(self.newFrejm, text="{:^29}".format(i[2]))
            a4.grid(row=r, column=4)
            self.priv.append(a4)

            a6 = tk.Label(self.newFrejm, text="{:^13}".format(i[3][:6]))
            a6.grid(row=r, column=6)
            self.priv.append(a6)

            a8 = tk.Label(self.newFrejm, text="{:^12}".format(i[4]))
            a8.grid(row=r, column=8, sticky="w")
            self.priv.append(a8)

            a10 = tk.Label(self.newFrejm, text="{:^10}".format(i[5][:9]))
            a10.grid(row=r, column=10)
            self.priv.append(a10)

            a11 = tk.Label(self.newFrejm, text="{:^24}".format(i[6][:9]))
            a11.grid(row=r, column=12)
            self.priv.append(a11)

            a13 = tk.Checkbutton(self.newFrejm, text="", command=lambda counter=counter: self.odobri(
                counter))  # svaki put kad se checkira dugme, salje se counter, pa se zna tacno koje dugme je kliknuto
            a13.grid(row=r, column=14)
            self.priv.append(a13)
            a15 = tk.Label(self.newFrejm, text=" ")
            a15.grid(row=r, column=15)
            self.priv.append(a15)
            self.recnik[counter] = i  # dodeljujemo i (jedna lista) pod kljuc counter
            self.checkboxovi.append(a13)  # dodeljujemo u ovu listu da bi znali koji je checkbox kliknut

            if i[6] != "kreiran":
                a13.config(state="disabled")

    def sortedPrikaz(self, broj):
        """
        Poziva funkcije za sortiranje, i prikazuje se sortirani prikaz
        """
        for p in self.priv:
            p.destroy()

        if broj == 1:
            self.prikaz(util.sortPoDatumuKreiranja(self.controler.m.prikazZahteva()))
        elif broj == 2:
            self.prikaz(util.sortPoDatumuRealizacije(self.controler.m.prikazZahteva()))
        elif broj == 3:
            self.prikaz(util.sortPoStatusu(self.controler.m.prikazZahteva()))

    def prikazZahtevaSmestanjeWidgets(self):
        """
        Inicijalizacija svih widget-a potrebnih za prikaz tabele zahteva za smestanje
        """
        self.headerFrame.destroy()
        self.canvas.destroy()

        self.prikazTransportButton.config(state="normal")
        self.prikazSmestanjeButton.config(state="disabled")

        self.prikazTransportButton.config(state="normal")
        self.prikazSmestanjeButton.config(state="disabled")

        self.listboxZahteviZaSmestanje = tk.Listbox(self.frejmZahtevi, width=70, height=20)
        self.listboxZahteviZaSmestanje.grid(row=1, columnspan=10, sticky='nsew')
        self.scrollbary = tk.Scrollbar(self)
        self.scrollbarx = tk.Scrollbar(self, orient='horizontal')
        self.listboxZahteviZaSmestanje.config(yscrollcommand=self.scrollbary.set)
        self.scrollbary.config(command=self.listboxZahteviZaSmestanje.yview)
        self.listboxZahteviZaSmestanje.config(xscrollcommand=self.scrollbarx.set)
        self.scrollbarx.config(command=self.listboxZahteviZaSmestanje.xview)
        self.scrollbarx.grid(row=3, columnspan=10, sticky='nsew')
        self.scrollbary.grid(row=2, column=4, sticky='nsew')
        self.prikaz1()

    def prikaz1(self):
        """
        Prikaz zahteva za smestanje
        """
        zahtevi = aplikacija.prikazi_zahteve_za_smestanje_aviona()
        for i, zahtev in enumerate(zahtevi):
            self.listboxZahteviZaSmestanje.insert(i, zahtev)

    def logout(self):
        """
        Izlazi iz menadzer transporta panel-a i vraca na login prozor
        """
        self.headerFrame.destroy()
        self.canvas.destroy()
        self.controler.meni.destroy()

        try:
            self.listboxZahteviZaSmestanje.destroy()
            self.scrollbarx.destroy()
            self.scrollbary.destroy()

        except:
            pass

        self.controler.show_frame(gui.windows.LoginWindow)

    def odobri(self, counter):
        """Vrsi odobravanje zahteva za transport, ako roba moze da stane odmah je utovara (po sablonu iz
            modula-entiteti.py, klasa-Dimenzije, metoda-self.dodaj(other)).
            time se pri odobravanju drugog zahteva uzima u obzir roba iz zahteva koji je vec odobren"""
        self.checkboxovi[counter].config(state="disabled")

        zahtev = None
        pozicija_zahteva = None
        smesten = False

        for pozicija_zahteva, z in enumerate(
                aplikacija.zahtevi_za_transport_robe['kreiran']):  # pronalazi sve 'kreiran' zahteve
            if z.IDZahteva == self.recnik[counter][0]:
                zahtev = z
                break

        for avion in aplikacija.avioni_u_hangarima:  # za svaki avion u hangaru trazi da li odgovara odrediste
            if avion.relacija == zahtev.odrediste:
                avionCopy = copy.deepcopy(avion)
                kol_robe = len(zahtev.roba)
                for r in zahtev.roba:
                    for prostor in avionCopy:  # za svaki prostor u avion-kopiji proba da smesti rob
                        if r < prostor and r.tezina < avionCopy.nosivost:
                            prostor.dodaj(r)  # dodata roba u prostor
                            avionCopy.nosivost -= int(r.tezina)
                            kol_robe -= 1
                            if kol_robe == 0:
                                break
                            break
                            # zahtevCopy.roba.remove(r)  # skida robu iz zahteva ako je utovarena
                if kol_robe == 0:
                    for roba in zahtev.roba:
                        for prostor in avion:  # za svaki prostor u avion-kopiji proba da smesti robu
                            if prostor > roba:
                                prostor.dodaj(roba)
                                avion.nosivost -= int(roba.tezina)
                                break
                                # dodata roba u prostor
                    zahtev.statusZahteva = 'odobren'
                    zahtev.avion = avion
                    avion.zahtev_transport.append(zahtev)
                    # stavlja u listu odobrenih iz liste kreiranih
                    aplikacija.zahtevi_za_transport_robe['odobren'].append(
                        aplikacija.zahtevi_za_transport_robe['kreiran'].pop(pozicija_zahteva))
                    smesten = True
                    break
        if smesten:
            tkinter.messagebox.showinfo('uspeh!', 'uspesno je odobren zahtev za transport')
        else:
            tkinter.messagebox.showerror('Greska', 'Nije odobren zahtev za transport '
                                                   '(nema aviona sa dovoljno mesta)')


class ManagerHangaraPanel(tk.Frame):
    """Predstavlja klasu koja se kreira pri logovanju korisnika, poziva funkije koje su locirane u
        modulu aplikacija. Ova klasa sluzi samo za graficki prikaz onoga sto menadzer hangara moze da uradi"""

    def __init__(self, parent, controler):
        self.controler = controler
        tk.Frame.__init__(self, parent)
        nekiLabel = tk.Label(self, text="Ulogovani ste kao manager hangara")
        nekiLabel.grid()

        self.temp_duzina = 0
        self.temp_sirina = 0
        self.temp_visina = 0

    def create_widgets(self):
        """Kreira potrebne widget-e (dugmice, labele, listbox...) da bi prozor bio funkcionalan"""
        self.frejm = tk.Frame(self)
        self.frejm.grid()
        self.listbox = tk.Listbox(self.frejm)
        self.listbox.grid(row=3, columnspan=4, sticky='nsew')
        scrollbary = tk.Scrollbar(self.frejm)
        scrollbarx = tk.Scrollbar(self.frejm, orient='horizontal')
        self.listbox.config(yscrollcommand=scrollbary.set)
        scrollbary.config(command=self.listbox.yview)
        self.listbox.config(xscrollcommand=scrollbarx.set)
        scrollbarx.config(command=self.listbox.xview)
        scrollbarx.grid(row=4, columnspan=4, sticky='nsew')
        scrollbary.grid(row=3, column=5, sticky='nse')

        self.dug_smesti_avion = tk.Button(self.frejm, text='Land Airplane', state='disabled')
        self.dug_kreiraj_zah = tk.Button(self.frejm, text='Create request', state='disabled')
        self.dug_transportuj_odobrene = tk.Button(self.frejm, text='Transport cargo', state='disabled')
        self.dug_prikazi_avione_za_transport = tk.Button(self.frejm, text='Airplanes ready for trans',
                                                         command=self.prikazi_avione_za_transport)

        self.dug_smesti_avion.grid(row=6, column=3, sticky='nsew')
        self.dug_kreiraj_zah.grid(row=5, column=3, sticky='nsew')
        self.dug_transportuj_odobrene.grid(row=2, column=1, sticky='nsew')
        self.dug_prikazi_avione_za_transport.grid(row=1, column=1, sticky='nsew')

        dug_smestanje = tk.Button(self.frejm, text='Requests for landing', command=self.zahtevi_smestanja)
        dug_smestanje.grid(row=1, column=0, sticky='nsew')

        dug_transport = tk.Button(self.frejm, text='Requests for transport(cargo loaded)',
                                  command=self.zahtevi_transport)
        dug_transport.grid(row=2, column=0, sticky='nsew')

        dug_dodaj_hangar = tk.Button(self.frejm, text='Add(make) Hangar', command=self.add_hangar)
        dug_dodaj_hangar.grid(row=1, column=2, sticky='nsew')

        dug_dodaj_avion = tk.Button(self.frejm, text='Add(make) Airplane', command=self.add_avion)
        dug_dodaj_avion.grid(row=2, column=2, sticky='nsew')

        dug_prikazi_avione_bez_zahteva = tk.Button(self.frejm, text='Airplanes without request',
                                                   command=self.prikazi_avione_bez_zahteva)
        dug_prikazi_avione_bez_zahteva.grid(row=1, column=3, sticky='nsew')

        dug_prikazi_avione_sa_zahtevom = tk.Button(self.frejm, text='Airplanes with request',
                                                   command=self.prikazi_avione_sa_zahtevom)
        dug_prikazi_avione_sa_zahtevom.grid(row=2, column=3, sticky='nsew')

        self.logout_button = tk.Button(self.frejm, text="Log Out!", command=self.logout)
        self.logout_button.grid(row=6, sticky='sw')

    def logout(self):
        """Izlazi iz menadzer hangara panel-a i vraaa na login screen"""
        self.frejm.destroy()
        self.controler.meni.destroy()
        self.controler.show_frame(gui.windows.LoginWindow)

    def zahtevi_smestanja(self):
        """Prikazuje zahteve za smestanje"""
        self.iskljuci_dugmad()
        zahtevi = aplikacija.prikazi_zahteve_za_smestanje_aviona()
        self.listbox.delete(0, 'end')
        for i, zahtev in enumerate(zahtevi):
            self.listbox.insert(i, zahtev)

    def zahtevi_transport(self):
        """Prikazuje zahteve za transport cija je roba utovarena"""
        self.iskljuci_dugmad()
        zahtevi = aplikacija.prikaz_zahteva_za_transport_utovarene_robe()
        self.listbox.delete(0, 'end')
        for i, zahtev in enumerate(zahtevi):
            self.listbox.insert(i, zahtev)

    def add_hangar(self):
        """Prvi korak u dodavanju hangara, kreira prozor u koji se unose vrednosti"""
        self.iskljuci_dugmad()
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

    def _ocisti_robu(self, top):
        aplikacija.temp_prostor_za_robu.clear()
        top.destroy()

    def add_avion(self):
        """Prvi korak dodavanja aviona, kreira prozor u koji se unose vrednosti i prostori za teret"""
        self.iskljuci_dugmad()
        top = tk.Toplevel()
        top.protocol('WM_DELETE_WINDOW', lambda: self._ocisti_robu(top))
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

        self.btn_add_avion = tk.Button(top, text='Add(make) Airplane',
                                       command=lambda: self._prikupi_inpute_aviona(entry_naziv, entry_duzina,
                                                                                   entry_sirina,
                                                                                   entry_visina,
                                                                                   entry_raspon_krila,
                                                                                   entry_godiste,
                                                                                   entry_nosivost,
                                                                                   entry_relacija, top))

        tk.Button(top, text='Add cargo space', command=lambda: self.add_pzt(entry_naziv, entry_duzina,
                                                                                   entry_sirina,
                                                                                   entry_visina,
                                                                                   entry_raspon_krila,
                                                                                   entry_godiste,
                                                                                   entry_nosivost,
                                                                                   entry_relacija)).grid(row=8,
                                                                                                         column=0)

    def add_pzt(self, en, ed, es, ev, erk, eg, eno, er):
        """Prvi korak u dodavanju prostora za teret, kreira prozor u koji se upisuju vrednosti"""
        en.config(state='disabled')
        ed.config(state='disabled')
        es.config(state='disabled')
        ev.config(state='disabled')
        erk.config(state='disabled')
        eg.config(state='disabled')
        eno.config(state='disabled')
        er.config(state='disabled')
        if self.temp_duzina == 0:
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
        """Drugi korak u dodavanju hangara, prikuplja unesene vrednosti i pravi objekat hangara (koji ce biti
            dodat u aerodrom)"""
        naziv = en.get()
        duzina = ed.get()
        sirina = es.get()
        visina = ev.get()

        if aplikacija.proveri_inpute_hangar(naziv, duzina, sirina, visina):
            aplikacija.napravi_hangar(naziv, int(duzina), int(sirina), int(visina))
            tk.messagebox.showinfo('Dodavanje hangara u aerodrom', 'Uspesno dodat hangar')
            top.destroy()
        else:
            tk.messagebox.showerror('Invalid inputs', 'Molimo unesite validne inpute str/int/int/int')

    def _prikupi_inpute_aviona(self, en, ed, es, ev, erk, eg, eno, er, top):
        """Drugi korak u dodavanju aviona, uzima unete vrednosti i stvara objekat aviona(koji dodaje van hangara)"""
        naziv = en.get()
        duzina = ed.get()
        sirina = es.get()
        visina = ev.get()
        raspon_krila = erk.get()
        godiste = eg.get()
        nosivost = eno.get()
        relacija = er.get()
        if aplikacija.proveri_inpute_avion(naziv, duzina, sirina, visina,
                                           raspon_krila, godiste, nosivost, relacija):

            aplikacija.napravi_avion(naziv, int(duzina), int(sirina), int(visina), int(raspon_krila),
                                     int(godiste), int(nosivost), relacija)

            aplikacija.dodaj_odrediste(relacija)
            tk.messagebox.showinfo('Narucivanje aviona', 'Uspesno napravljen avion')
            self._resetuj_temp(top)
            top.destroy()
        else:
            tk.messagebox.showerror('Invalid inputs',
                                    'Molimo unesite validne inpute str/int/int/int/int/int/int/str')

    def _resetuj_temp(self, top):
        """Pomocna funkcija koja resetuje pomocne dimenzije koje se koriste pri proveravanju da li su dimenzije
            prostora odgovarajuce da bi mogle da udju u avion. Kada se napravi avion one se resetuju"""
        self.temp_duzina = 0
        self.temp_sirina = 0
        self.temp_visina = 0
        aplikacija.temp_prostor_za_robu.clear()
        top.destroy()

    def _pokupi_inpute_pzt(self, en, ed, es, ev, top):
        """Drugi korak u dodavanju prostora za robe u avion pri kreiranju aviona, kupi unesene podatke
            uporedjuje sa dimenzijama aviona, sve dok se ne unesu dobre dimenzije(prostor je dovoljno mali da
            moze da udje u avion) prozor ce biti aktivan"""
        naziv = en.get()
        duzina = ed.get()
        sirina = es.get()
        visina = ev.get()

        if aplikacija.proveri_inpute_prostor_za_robu(naziv, duzina, sirina, visina) \
                and int(duzina) < self.temp_duzina and int(sirina) < self.temp_sirina \
                and int(visina) < self.temp_visina:
            aplikacija.napravi_prostor_za_robu(naziv, int(duzina), int(sirina), int(visina))
            self.temp_duzina -= int(duzina)
            tk.messagebox.showinfo('Dodavanje Prostora za Teret u Avion', 'Uspesno dodat Prostor za Teret')
            top.destroy()

            imena_prostora = ''
            for prostor in aplikacija.temp_prostor_za_robu:
                imena_prostora += prostor.naziv + ' '
            self.lbl_pzt.config(text=imena_prostora)

            self.btn_add_avion.grid(row=9, columnspan=2, sticky='nsew')

        else:
            tk.messagebox.showerror('Invalid inputs',
                                    'Molimo unesite validne inpute str/int/int/int ili manje dimenzije')

    def prikazi_avione_bez_zahteva(self):
        """Prikazuje sve avione koji su van aerodroma i nemaju zahtev za smestanje"""
        self.iskljuci_dugmad()
        self.listbox.delete(0, 'end')
        avioni_bez_zahteva = []
        for i, avion in enumerate(aplikacija.avioni_van_hangara):
            if avion.zahtev_smestanje is None:
                avioni_bez_zahteva.append(avion)
                self.listbox.insert(i, str(avion))
        if avioni_bez_zahteva:
            self.dug_kreiraj_zah.config(state='normal', command=lambda: self._create_request(avioni_bez_zahteva))

    def _create_request(self, avioni_bez_zahteva):
        """Stvara zahtev za smestanje za prosledjen avion bez zahteva. Ovo je moguce uraditi tek kada se prikazu
            avioni bez zahteva i kada se odabere onaj za koji zelimo da kreiramo zahtev, uspesnost kreiranja
            zahteva ce biti prikaza u vidu prozora sa porukom"""
        try:
            odabran_avion = avioni_bez_zahteva[self.listbox.curselection()[0]]
            aplikacija.napravi_zahtev_za_smestanje(odabran_avion, self.controler.m)
            self.dug_kreiraj_zah.config(state='disabled')
            tk.messagebox.showinfo('', 'Zahtev uspesno kreiran')
            self.listbox.delete(0, 'end')
        except:
            tk.messagebox.showinfo('', 'Molimo izaberite avion za koji zelite da napravite zahtev za smestanje')

    def prikazi_avione_sa_zahtevom(self):
        """Prikazuje sve avione koji imaju zahtev a nisu u aerodromu (spremni su za smestanje)"""
        self.iskljuci_dugmad()
        self.listbox.delete(0, 'end')
        avioni_sa_zahtevom = []
        for i, avion in enumerate(aplikacija.avioni_van_hangara):
            if avion.zahtev_smestanje is not None:
                avioni_sa_zahtevom.append(avion)
                self.listbox.insert(i, str(avion))
        if avioni_sa_zahtevom:
            self.dug_smesti_avion.config(state='normal', command=lambda: self._smesti_avion(avioni_sa_zahtevom))

    def _smesti_avion(self, avioni_sa_zahtevom):
        """Smesta odabrani avion za zahtevom u aerodrom, uspesnost smestanja ce biti prikazana u vidu prozora
            sa porukom"""
        try:
            odabran_avion = avioni_sa_zahtevom[self.listbox.curselection()[0]]
            if aplikacija.smesti_avion(odabran_avion):
                aplikacija.avioni_van_hangara.remove(odabran_avion)
                tk.messagebox.showinfo('Uspeh!', 'Uspesno je smesten Avion')
                self.dug_smesti_avion.config(state='disabled')
                self.listbox.delete(0, 'end')
            else:
                tk.messagebox.showinfo('', 'Nije smesten Avion (nema mesta)')
        except:
            tk.messagebox.showinfo('', 'Molimo izaberite avion koji zelite da smestite')

    def prikazi_avione_za_transport(self):
        """Prikazuje sve avione za transport. Sva roba iz svih zahteva koji su odobreni za taj avoion je
            utovarena. Uspesnost transporta je izrazena prozorom sa porukom."""
        self.iskljuci_dugmad()
        self.listbox.delete(0, 'end')
        avioni_sa_zahtevom_trans = []
        for i, avion in enumerate(aplikacija.avioni_u_hangarima):
            statusi = set()
            for zahtev in avion.zahtev_transport:
                statusi.add(zahtev.statusZahteva)
            if len(statusi) != 1:
                continue
            elif len(statusi) == 1 and 'robaUtovarena' in statusi:
                avioni_sa_zahtevom_trans.append(avion)
                self.listbox.insert(i, str(avion))

        if avioni_sa_zahtevom_trans:
            self.dug_transportuj_odobrene.config(state='normal',
                                                 command=lambda:
                                                 self._transportuj_odobrene(avioni_sa_zahtevom_trans))

    def _transportuj_odobrene(self, avioni_sa_zahtevom_trans):
        """Pomocna metoda koja transportuje robu za odabran avion"""
        try:
            odabran_avion = avioni_sa_zahtevom_trans[self.listbox.curselection()[0]]
            aplikacija.transportuj_robu(odabran_avion)
            self.listbox.delete(0, 'end')
            tk.messagebox.showinfo('', 'Uspesno je transportovana sva roba iz: ' + odabran_avion.naziv)

        except:
            tk.messagebox.showinfo('', 'Molimo izaberite avion koji zelite da transportuje')

    def iskljuci_dugmad(self):
        """Metoda koja iskljucuje dugmad koji treba da se pojave tek posle prikaza nekih funkcionalnosti."""
        self.dug_smesti_avion.config(state='disabled')
        self.dug_kreiraj_zah.config(state='disabled')
        self.dug_transportuj_odobrene.config(state='disabled')

import klase.util_funk as util
from klase.entiteti import OznakaINaziv
import klase
# from klase import hangar_funkcionalnosti


class Osoba(OznakaINaziv):
    """Svi korisnici aplikacije"""
    def __init__(self, ID, naziv, prezime):
        OznakaINaziv.__init__(self, ID, naziv)
        self.prezime = prezime


class Zaposlen(Osoba):
    """To su sve osobe koje rade sa aplikacijom, dakle Menadzeri Hangara, Transporta i Radnik"""
    def __init__(self, ID, naziv, prezime, usn, psw=None):
        Osoba.__init__(self, ID, naziv, prezime)
        self.username = usn
        self.password = psw

    def pretrazi_hangare_po_oznaci(self, oznaka):
        """Vraca hangare cija je oznaka ista unetoj oznaci"""
        rezultat_pretrage = []
        for hangar in klase.aplikacija.aerodrom:
            if str(hangar.id) == oznaka:
                rezultat_pretrage.append(hangar)
        return rezultat_pretrage

    def pretrazi_hangare_po_nazivu(self, naziv):
        """Vraca hangare ako se argument 'naziv' nalazi u imenu hangara.
            Bez obzira sta je unet naziv i naziv hangara poredice se kao str.lower()"""
        rezultat_pretrage = []
        for hangar in klase.aplikacija.aerodrom:
            if naziv.lower() in hangar.naziv.lower():
                rezultat_pretrage.append(hangar)
        rezultat_pretrage.sort(key=lambda x: x.naziv)
        return rezultat_pretrage

    def pretrazi_hangare_po_duzini(self, donja_granica, gornja_granica):
        """Vraca sve hangare cija je duzina manja ili jednaka od unete duzine"""
        rezultat_pretrage = []
        for hangar in klase.aplikacija.aerodrom:
            if donja_granica <= hangar.duzina <= gornja_granica:
                rezultat_pretrage.append(hangar)
        rezultat_pretrage.sort(key=lambda x: x.duzina)
        return rezultat_pretrage

    def pretrazi_hangare_po_sirini(self, donja_granica, gornja_granica):
        """Vraca sve hangare cija je sirina manja ili jednaka od unete sirina"""
        rezultat_pretrage = []
        for hangar in klase.aplikacija.aerodrom:
            if donja_granica <= hangar.sirina <= gornja_granica:
                rezultat_pretrage.append(hangar)
        rezultat_pretrage.sort(key=lambda x: x.sirina)
        return rezultat_pretrage

    def pretrazi_hangare_po_visini(self, donja_granica, gornja_granica):
        """Vraca sve hangare cija je visina manja ili jednaka od unete visina"""
        rezultat_pretrage = []
        for hangar in klase.aplikacija.aerodrom:
            if donja_granica <= hangar.visina <= gornja_granica:
                rezultat_pretrage.append(hangar)
        rezultat_pretrage.sort(key=lambda x: x.visina)
        return rezultat_pretrage

    def pretrazi_avine_po_oznaci(self, oznaka):
        """Vraca avione cija je oznaka ista unetoj oznaci"""
        rezultat_pretrage = []
        for avion in klase.aplikacija.avioni_u_hangarima:
            if str(avion.id) == oznaka:
                rezultat_pretrage.append(avion)
        for avion in klase.aplikacija.avioni_van_hangara:
            if str(avion.id) == oznaka:
                rezultat_pretrage.append(avion)
        return rezultat_pretrage

    def pretrazi_avione_po_duzini(self, donja_granica, gornja_granica):
        """Vraca sve avione cija je duzina manja ili jednaka od unete duzine"""
        rezultat_pretrage = []
        for avion in klase.aplikacija.avioni_u_hangarima:
            if donja_granica <= avion.duzina <= gornja_granica:
                rezultat_pretrage.append(avion)
        for avion in klase.aplikacija.avioni_van_hangara:
            if donja_granica <= avion.duzina <= gornja_granica:
                rezultat_pretrage.append(avion)
        rezultat_pretrage.sort(key=lambda x: x.duzina)
        return rezultat_pretrage

    def pretrazi_avione_po_sirini(self, donja_granica, gornja_granica):
        """Vraca sve avione cija je sirina manja ili jednaka od unete sirine"""
        rezultat_pretrage = []
        for avion in klase.aplikacija.avioni_u_hangarima:
            if donja_granica <= avion.sirina <= gornja_granica:
                rezultat_pretrage.append(avion)
        for avion in klase.aplikacija.avioni_van_hangara:
            if donja_granica <= avion.sirina <= gornja_granica:
                rezultat_pretrage.append(avion)
        rezultat_pretrage.sort(key=lambda x: x.sirina)
        return rezultat_pretrage

    def pretrazi_avione_po_raspon_krila(self, donja_granica, gornja_granica):
        """Vraca sve avione ciji je raspon krila manji ili jednak od unetog raspona krila"""
        rezultat_pretrage = []
        for avion in klase.aplikacija.avioni_u_hangarima:
            if donja_granica <= avion.raspon_krila <= gornja_granica:
                rezultat_pretrage.append(avion)
        for avion in klase.aplikacija.avioni_van_hangara:
            if donja_granica <= avion.raspon_krila <= gornja_granica:
                rezultat_pretrage.append(avion)
        rezultat_pretrage.sort(key=lambda x: x.raspon_krila)
        return rezultat_pretrage

    def pretrazi_avione_po_nosivosti(self, donja_granica, gornja_granica):
        """Vraca sve avione cija je nosivost manja ili jednaka od unete nosivosti"""
        rezultat_pretrage = []
        for avion in klase.aplikacija.avioni_u_hangarima:
            if donja_granica <= avion.nosivost <= gornja_granica:
                rezultat_pretrage.append(avion)
        for avion in klase.aplikacija.avioni_van_hangara:
            if donja_granica <= avion.nosivost <= gornja_granica:
                rezultat_pretrage.append(avion)
        rezultat_pretrage.sort(key=lambda x: x.nosivost)
        return rezultat_pretrage

    def pretrazi_avione_po_relaciji(self, relacija):
        """Vraca sve avione koji lete na datoj relaciji. Relacije se porede kao str.lower()"""
        rezultat_pretrage = []
        for avion in klase.aplikacija.avioni_u_hangarima:
            if relacija.lower() in avion.relacija.lower():
                rezultat_pretrage.append(avion)
        for avion in klase.aplikacija.avioni_van_hangara:
            if relacija.lower() in avion.relacija.lower():
                rezultat_pretrage.append(avion)
        rezultat_pretrage.sort(key=lambda x: x.relacija)
        return rezultat_pretrage

    def pretraziRobuPoOznaci(self, oznaka):
        rezultat_pretrage = []

        for key in klase.aplikacija.zahtevi_za_transport_robe.keys():
            for zahtev in klase.aplikacija.zahtevi_za_transport_robe[key]:
                for roba in zahtev.roba:
                    if str(roba.oznaka) == oznaka:
                        rezultat_pretrage.append(roba)
        return rezultat_pretrage

    def pretraziRobuPoNazivu(self, naziv):
        rezultat_pretrage = []

        for key in klase.aplikacija.zahtevi_za_transport_robe.keys():
            for zahtev in klase.aplikacija.zahtevi_za_transport_robe[key]:
                for roba in zahtev.roba:
                    if naziv in roba.naziv:
                        rezultat_pretrage.append(roba)
        rezultat_pretrage.sort(key=lambda x: x.naziv)
        return rezultat_pretrage

    def pretraziRobuPoOpisu(self, opis):
        rezultat_pretrage = []

        for key in klase.aplikacija.zahtevi_za_transport_robe.keys():
            for zahtev in klase.aplikacija.zahtevi_za_transport_robe[key]:
                for roba in zahtev.roba:
                    if opis in roba.opis:
                        rezultat_pretrage.append(roba)
        return rezultat_pretrage

    def pretraziRobuPoDuzini(self, donja_granica, gornja_granica):
        rezultat_pretrage = []

        for key in klase.aplikacija.zahtevi_za_transport_robe.keys():
            for zahtev in klase.aplikacija.zahtevi_za_transport_robe[key]:
                for roba in zahtev.roba:
                    if donja_granica <= roba.duzina <= gornja_granica:
                        rezultat_pretrage.append(roba)
        rezultat_pretrage.sort(key=lambda x: x.duzina)
        return rezultat_pretrage

    def pretraziRobuPoSirini(self, donja_granica, gornja_granica):
        rezultat_pretrage = []

        for key in klase.aplikacija.zahtevi_za_transport_robe.keys():
            for zahtev in klase.aplikacija.zahtevi_za_transport_robe[key]:
                for roba in zahtev.roba:
                    if donja_granica <= roba.sirina <= gornja_granica:
                        rezultat_pretrage.append(roba)
        rezultat_pretrage.sort(key=lambda x: x.sirina)
        return rezultat_pretrage

    def pretraziRobuPoVisini(self, donja_granica, gornja_granica):
        rezultat_pretrage = []

        for key in klase.aplikacija.zahtevi_za_transport_robe.keys():
            for zahtev in klase.aplikacija.zahtevi_za_transport_robe[key]:
                for roba in zahtev.roba:
                    if donja_granica <= roba.visina <= gornja_granica:
                        rezultat_pretrage.append(roba)
        rezultat_pretrage.sort(key=lambda x: x.visina)
        return rezultat_pretrage

    def pretraziRobuPoTezini(self, donja_granica, gornja_granica):
        rezultat_pretrage = []

        for key in klase.aplikacija.zahtevi_za_transport_robe.keys():
            for zahtev in klase.aplikacija.zahtevi_za_transport_robe[key]:
                for roba in zahtev.roba:
                    if donja_granica <= roba.tezina <= gornja_granica:
                        rezultat_pretrage.append(roba)

        rezultat_pretrage.sort(key=lambda x: x.tezina)
        return rezultat_pretrage

    def pretraziRobuPoIDPotrazitelja(self, IDPotrazitelja):
        rezultat_pretrage = []
        zahteviTransport = util.readFile("zahteviZaTransport.txt")

        for zahtev in zahteviTransport:
            l = zahtev.split("|")
            if l[4] == IDPotrazitelja:
                rezultat_pretrage.append(l[0])

        svaRoba = []
        robaLines = util.readFile("roba.txt")

        for roba in robaLines:
            r = roba.strip().split("|")
            if r[7] in rezultat_pretrage:
                svaRoba.append(r)

        return svaRoba


class MenadzerHangara(Zaposlen):
    """Menadzer hangara ima ovlascenje da:
        -Vidi sve zahteve za smeštanje aviona u hangar
        -Vidi zahteve za transport robe kojima je status postavljen na roba utovarena
        -Dodaje nove hangare
        -Dodaje nove avione i određuje koliki prostor za smeštanje robe postoji u avionu
        -Kreira Zahtev za smestanje Aviona u Hangar
        -Izvrsi transport robe (Avioni koji su utovareni i spremni za poletanje)"""
    uloga = "Menadzer Hangara"

    def __int__(self, ID, naziv, prezime, username, password):
        Zaposlen.__init__(self, ID, naziv, prezime, username, password)

    def __str__(self):
        return "Uloga: {}, ID: {}, Ime: {}, Prezime: {}, username: {}".format(self.uloga, self.id, self.naziv,
                                                                              self.prezime, self.username)


class Potrazitelj(Osoba):
    def __init__(self, ID, ime, prezime, brojTelefona, email):
        Osoba.__init__(self, ID, ime, prezime)
        self.ID = ID
        self.ime = ime
        self.prezime = prezime
        self.brojTelefona = brojTelefona
        self.email = email

    def prikazZahteva(self):
        '''
        Vraca zahteve za transport, ako je parametar "sve"=True
        vraca sve zahteve, ako je False, vraca samo od ulogovanog potrazitelja
        '''
        zahtevi = []
        lines = util.readFile("zahteviZaTransport.txt")
        for line in lines:
            l = line.strip().split("|")
            if l[4] == self.ID:
                zahtevi.append(l)
        return zahtevi


class ManagerTransport(Zaposlen):
    def __init__(self, ID, ime, prezime, username=None, password=None):
        Zaposlen.__init__(self, ID, ime, prezime, username, password)
        self.username = username
        self.password = password

    def prikazZahteva(self):
        '''
        Vraca sve zahteve za transport
        '''
        zahtevi = []
        lines = util.readFile("zahteviZaTransport.txt")
        for line in lines:
            l = line.strip().split("|")
            zahtevi.append(l)
        return zahtevi

    def prikazZahtevaSmestanje(self):
        '''
        Vraca sve zahteve za smestanje
        '''
        zahtevi = []
        lines = util.readFile("zahteviZaSmestanje.txt")
        for line in lines:
            l = line.strip().split("|")
            zahtevi.append(l)
        return zahtevi
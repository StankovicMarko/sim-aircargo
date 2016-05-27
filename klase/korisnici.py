import klase.util_funk as util
from klase.entiteti import OznakaINaziv


class Osoba(OznakaINaziv):
    def __init__(self, ID, naziv, prezime):
        OznakaINaziv.__init__(self, ID, naziv)
        self.prezime = prezime


class Zaposlen(Osoba):
    def __init__(self, ID, naziv, prezime, usn, psw):
        Osoba.__init__(self, ID, naziv, prezime)
        self.username = usn
        self.password = psw

    def pretraziHangarePo_(self):
        # oznaka
        # naziv
        # duzina
        # sirina
        # visina
        pass

    def pretraziAvionePo_(self):
        # oznaka
        # duzina
        # sirina
        # rasponKrila
        # nosivost
        # relacija
        pass

    def pretraziRobuPo_(self):
        # Oznaci
        # Nazivu
        # Opisu
        # Dužini
        # Širini
        # Visini
        # Težini robe
        # Identifikacionom kodu potražitelja
        pass

    def pretraziRobuPoIDPotrazitelja(self, IDPotrazitelja):
        sviZahtevi = []
        zahteviTransport = util.readFile("zahteviZaTransport.txt")

        for zahtev in zahteviTransport:
            l = zahtev.split("|")
            if l[4] == IDPotrazitelja:
                sviZahtevi.append(l[0])

        svaRoba = []
        robaLines = util.readFile("roba.txt")

        for roba in robaLines:
            r = roba.strip().split("|")
            if r[7] in sviZahtevi:
                svaRoba.append(r)

        return svaRoba


class MenadzerHangara(Zaposlen):
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
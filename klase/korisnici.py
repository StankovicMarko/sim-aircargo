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


class MenadzerHangara(Zaposlen):
    uloga = "Menadzer Hangara"

    def __int__(self, ID, naziv, prezime, username, password):
        Zaposlen.__init__(self, ID, naziv, prezime, username, password)

    def __str__(self):
        return ('Uloga: '+ self.uloga + OznakaINaziv.__str__(self)+ 'Prezime: '+self.prezime
                + ', Username: '+ self.username)

        #
        #
        # def prikazZahteva(self,sve=False):
        #     '''
        #     Vraca zahteve za transport, ako je parametar "sve"=True
        #     vraca sve zahteve, ako je False, vraca samo od ulogovanog potrazitelja
        #     '''
        #     zahtevi = []
        #     lines = util.readFile("files/zahteviZaTransport.txt")
        #     for line in lines:
        #         l = line.strip().split("|")
        #         if sve == True:
        #             zahtevi.append(l)
        #         else:
        #             if l[4] == self.ID:
        #                 zahtevi.append(l)
        #     return zahtevi


class Potrazitelj(Osoba):
    def __init__(self, ID, ime, prezime, brojTelefona, email):
        Osoba.__init__(self, ID, ime, prezime)
        self.ID = ID
        self.ime = ime
        self.prezime = prezime
        self.brojTelefona = brojTelefona
        self.email = email


class ManagerTransport(Osoba):
    def __init__(self, ID, ime, prezime, username, password):
        Osoba.__init__(self, ID, ime, prezime)
        self.username = username
        self.password = password

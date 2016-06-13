import klase.util_funk as util
from klase.entiteti import OznakaINaziv
import klase
# from klase import hangar_funkcionalnosti


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

    def pretraziHangarePoOznaci(self,oznaka):
        sviHang = []
        for hangar in klase.hangar_funkcionalnosti.aerodrom:
            if str(hangar.id) == oznaka:
                string = str(hangar) # prebacuje objekat hangar u string
                for a in hangar:
                    string+=str(a) # prikaz i aviona
                sviHang.append(string)
        return sviHang

    def pretraziHangarePoNazivu(self,naziv):
        sviHang = []
        for hangar in klase.hangar_funkcionalnosti.aerodrom:
            if hangar.naziv == naziv:
                string = str(hangar) # prebacuje objekat hangar u string
                for a in hangar:
                    string+=str(a) # prikaz i aviona
                sviHang.append(string)
        return sviHang

    def pretraziHangarePoDuzini(self,duzina):
        sviHang = []
        for hangar in klase.hangar_funkcionalnosti.aerodrom:
            if hangar.duzina == int(duzina):
                string = str(hangar) # prebacuje objekat hangar u string
                for a in hangar:
                    string+=str(a) # prikaz i aviona
                sviHang.append(string)
        return sviHang

    def pretraziHangarePoSirini(self,sirina):
        sviHang = []
        for hangar in klase.hangar_funkcionalnosti.aerodrom:
            if hangar.sirina == int(sirina):
                string = str(hangar) # prebacuje objekat hangar u string
                for a in hangar:
                    string+=str(a) # prikaz i aviona
                sviHang.append(string)
        return sviHang

    def pretraziHangarePoVisini(self,visina):
        sviHang = []
        for hangar in klase.hangar_funkcionalnosti.aerodrom:
            if hangar.visina == int(visina):
                string = str(hangar) # prebacuje objekat hangar u string
                for a in hangar:
                    string+=str(a) # prikaz i aviona
                sviHang.append(string)
        return sviHang

    def pretraziAvionePo_(self):
        # oznaka
        # duzina
        # sirina
        # rasponKrila
        # nosivost
        # relacija
        pass

    def pretraziAvionePoOznaci(self,oznaka):
        sviAvioni = []
        for avion in klase.hangar_funkcionalnosti.avioni_u_hangarima:
            if str(avion.id) == oznaka:
                sviAvioni.append(str(avion))
        for avion1 in klase.hangar_funkcionalnosti.avioni_van_hangara:
            if str(avion1.id) == oznaka:
                sviAvioni.append(str(avion1))
        return sviAvioni


    def pretraziAvionePoDuzini(self,duzina):
        sviAvioni = []
        for avion in klase.hangar_funkcionalnosti.avioni_u_hangarima:
            if avion.duzina == int(duzina):
                sviAvioni.append(str(avion))
        for avion1 in klase.hangar_funkcionalnosti.avioni_van_hangara:
            if avion1.duzina == int(duzina):
                sviAvioni.append(str(avion1))
        return sviAvioni


    def pretraziAvionePoSirini(self,sirina):
        sviAvioni = []
        for avion in klase.hangar_funkcionalnosti.avioni_u_hangarima:
            if avion.sirina == int(sirina):
                sviAvioni.append(str(avion))
        for avion1 in klase.hangar_funkcionalnosti.avioni_van_hangara:
            if avion1.sirina == int(sirina):
                sviAvioni.append(str(avion1))
        return sviAvioni

    def pretraziAvionePoRasponKrila(self,rasponKrila):
        sviAvioni = []
        for avion in klase.hangar_funkcionalnosti.avioni_u_hangarima:
            if avion.raspon_krila == int(rasponKrila):
                sviAvioni.append(str(avion))
        for avion1 in klase.hangar_funkcionalnosti.avioni_van_hangara:
            if avion1.raspon_krila == int(rasponKrila):
                sviAvioni.append(str(avion1))
        return sviAvioni

    def pretraziAvionePoNosivosti(self,nosivost):
        sviAvioni = []
        for avion in klase.hangar_funkcionalnosti.avioni_u_hangarima:
            if avion.nosivost == int(nosivost):
                sviAvioni.append(str(avion))
        for avion1 in klase.hangar_funkcionalnosti.avioni_van_hangara:
            if avion1.nosivost == int(nosivost):
                sviAvioni.append(str(avion1))
        return sviAvioni

    def pretraziAvionePoRelaciji(self,relacija):
        sviAvioni = []
        for avion in klase.hangar_funkcionalnosti.avioni_u_hangarima:
            if avion.relacija == relacija:
                sviAvioni.append(str(avion))
        for avion1 in klase.hangar_funkcionalnosti.avioni_van_hangara:
            if avion1.relacija == relacija:
                sviAvioni.append(str(avion1))
        return sviAvioni

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

    def pretraziRobuPoOznaci(self,oznaka):
        svaRoba = []

        for key in klase.hangar_funkcionalnosti.zahtevi_za_transport_robe.keys():
            for zahtev in klase.hangar_funkcionalnosti.zahtevi_za_transport_robe[key]:
                for roba in zahtev.roba:
                    if roba.oznaka == oznaka:
                        svaRoba.append(str(roba))
        return svaRoba

    def pretraziRobuPoNazivu(self,naziv):
        svaRoba = []

        for key in klase.hangar_funkcionalnosti.zahtevi_za_transport_robe.keys():
            for zahtev in klase.hangar_funkcionalnosti.zahtevi_za_transport_robe[key]:
                for roba in zahtev.roba:
                    if roba.naziv == naziv:
                        svaRoba.append(str(roba))
        return svaRoba

    def pretraziRobuPoOpisu(self,opis):
        svaRoba = []

        for key in klase.hangar_funkcionalnosti.zahtevi_za_transport_robe.keys():
            for zahtev in klase.hangar_funkcionalnosti.zahtevi_za_transport_robe[key]:
                for roba in zahtev.roba:
                    if opis in roba.opis:
                        svaRoba.append(str(roba))
        return svaRoba

    def pretraziRobuPoDuzini(self,duzina):
        svaRoba = []

        for key in klase.hangar_funkcionalnosti.zahtevi_za_transport_robe.keys():
            for zahtev in klase.hangar_funkcionalnosti.zahtevi_za_transport_robe[key]:
                for roba in zahtev.roba:
                    if roba.duzina == int(duzina):
                        svaRoba.append(str(roba))
        return svaRoba

    def pretraziRobuPoSirini(self,sirina):
        svaRoba = []

        for key in klase.hangar_funkcionalnosti.zahtevi_za_transport_robe.keys():
            for zahtev in klase.hangar_funkcionalnosti.zahtevi_za_transport_robe[key]:
                for roba in zahtev.roba:
                    if roba.sirina == int(sirina):
                        svaRoba.append(str(roba))
        return svaRoba

    def pretraziRobuPoVisini(self,visina):
        svaRoba = []

        for key in klase.hangar_funkcionalnosti.zahtevi_za_transport_robe.keys():
            for zahtev in klase.hangar_funkcionalnosti.zahtevi_za_transport_robe[key]:
                for roba in zahtev.roba:
                    if roba.visina == int(visina):
                        svaRoba.append(str(roba))
        return svaRoba

    def pretraziRobuPoTezini(self,tezina):
        svaRoba = []

        for key in klase.hangar_funkcionalnosti.zahtevi_za_transport_robe.keys():
            for zahtev in klase.hangar_funkcionalnosti.zahtevi_za_transport_robe[key]:
                for roba in zahtev.roba:
                    if roba.tezina == int(tezina):
                        svaRoba.append(str(roba))
        return svaRoba

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
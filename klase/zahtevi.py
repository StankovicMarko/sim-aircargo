from datetime import datetime
import klase.util_funk as util
from klase.entiteti import OznakaINaziv


class Zahtev(OznakaINaziv):
    def __init__(self, ID, naziv=None):
        OznakaINaziv.__init__(self, ID, naziv)
        self.datumKreiranja = datetime.now()


class ZahtevZaSmestanjeAviona(Zahtev):
    def __init__(self, ID, naziv, hangar, avion, menadzerHangara):
        Zahtev.__init__(self, ID, naziv)
        self.vremeSmestanjaAviona = None
        self.vremeNapustanjaHangara = None
        self.hangar = hangar
        self.avion = avion
        self.menadzer = menadzerHangara

    def __str__(self):
        return 'Zahtev za smestanje aviona - Oznaka: '+self.id + ', ID hangara: '+ self.hangar.id \
                + ', ID Aviona: ' + self.avion.id + ', ID Menadzera: ' + self.menadzer.id


class ZahtevZaTransport(Zahtev):
    def __init__(self, odrediste, IDPotrazitelja):
        Zahtev.__init__(self)
        self.datumTransporta = "None"
        self.odrediste = odrediste
        self.IDPotrazitelja = IDPotrazitelja
        self.oznakaAviona = "None"
        self.statusZahteva = "kreiran"

        util.saveFile("zahteviZaTransport.txt",
                      self.IDZahteva + "|" + self.datumKreiranja + "|" + self.datumTransporta +
                      "|" + self.odrediste + "|" + self.IDPotrazitelja + "|" + self.oznakaAviona + "|" + self.statusZahteva + "\n")

    def prikazZahteva(self, IDPotrazitelja):
        lines = util.readFile("zahteviZaTransport.txt")
        for line in lines:
            l = line.strip().split("|")
            if l[4] == IDPotrazitelja:
                print(l)

    def odrediDatum(self):
        return datetime.now().strftime("%d/%m/%Y")

    def odrediIDZahteva(self):
        lines = util.readFile("zahteviZaTransport.txt")
        lastLine = lines[-1].split("|")
        l = lastLine[0].split("#")
        return "ZT#" + str(int(l[1]) + 1)

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
        self.idHangara = hangar.id
        self.idAviona = avion.id
        self.idMenadzera = menadzerHangara.id

    def __str__(self):
        return 'Zahtev za smestanje aviona - Oznaka: '+self.id + ', ID hangara: '+ self.idHangara \
                + ', ID Aviona: ' + self.idAviona + ', ID Menadzera: ' + self.idMenadzera


class ZahtevZaTransport(Zahtev):
    def __init__(self, odrediste, IDPotrazitelja):
        Zahtev.__init__(self)
        self.datumTransporta = "None"
        self.odrediste = odrediste
        self.IDPotrazitelja = IDPotrazitelja
        self.oznakaAviona = "None"
        self.statusZahteva = "kreiran"

        util.saveFile("files/zahteviZaTransport.txt",
                      self.IDZahteva + "|" + self.datumKreiranja + "|" + self.datumTransporta +
                      "|" + self.odrediste + "|" + self.IDPotrazitelja + "|" + self.oznakaAviona + "|" + self.statusZahteva + "\n")

    def prikazZahteva(self, IDPotrazitelja):
        lines = util.readFile("files/zahteviZaTransport.txt")
        for line in lines:
            l = line.strip().split("|")
            if l[4] == IDPotrazitelja:
                print(l)

    def odrediDatum(self):
        return datetime.now().strftime("%d/%m/%Y")

    def odrediIDZahteva(self):
        lines = util.readFile("files/zahteviZaTransport.txt")
        lastLine = lines[-1].split("|")
        l = lastLine[0].split("#")
        return "ZT#" + str(int(l[1]) + 1)

from datetime import datetime
import klase.util_funk as util
from klase.entiteti import OznakaINaziv


class Zahtev(OznakaINaziv):
    def __init__(self, ID, naziv):
        OznakaINaziv.__init__(self, ID, naziv)
        self.vremeKreiranja = datetime.now()


class ZahtevZaSmestanjeAviona(Zahtev):
    def __init__(self, ID, avion, menadzer_hangara, naziv=None):
        Zahtev.__init__(self, ID, naziv)
        self.vreme_smestanja_aviona = None
        self.vreme_napustanja_hangara = None
        self.hangar = None
        self.avion = avion
        self.menadzer = menadzer_hangara

    def __str__(self):
        if self.hangar is None:
            return 'Zahtev za smestanje aviona - Oznaka: {}, Vreme kreiranja: {}, Vreme smestanja: {}, ' \
               'Vreme napustanja: {}, ID Aviona: {}, ID Menadzera: {}'.format(
                                                                        self.id, self.vremeKreiranja,
                                                                        self.vreme_smestanja_aviona,
                                                                        self.vreme_napustanja_hangara,
                                                                        self.avion.id, self.menadzer.id)

        else:
            return 'Zahtev za smestanje aviona - Oznaka: {}, Vreme kreiranja: {}, Vreme smestanja: {}, ' \
               'Vreme napustanja: {}, ID Hangara: {}, ID Aviona: {}, ID Menadzera: {}'.format(
                                                                        self.id, self.vremeKreiranja,
                                                                        self.vreme_smestanja_aviona,
                                                                        self.vreme_napustanja_hangara,
                                                                        self.hangar.id,
                                                                        self.avion.id, self.menadzer.id)


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

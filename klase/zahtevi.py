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
        if self.hangar:
            id_hangara = self.hangar.id
        else:
            id_hangara = None

        if self.vremeKreiranja:
            vreme_kreiranja = '{}.{}.{}, {}:{}'.format(self.vremeKreiranja.day,
                                                       self.vremeKreiranja.month,
                                                       self.vremeKreiranja.year,
                                                       self.vremeKreiranja.hour,
                                                       self.vremeKreiranja.minute)
        else:
            vreme_kreiranja = None

        if self.vreme_smestanja_aviona:
            vreme_smestanja = '{}.{}.{}, {}:{}'.format(self.vreme_smestanja_aviona.day,
                                                       self.vreme_smestanja_aviona.month,
                                                       self.vreme_smestanja_aviona.year,
                                                       self.vreme_smestanja_aviona.hour,
                                                       self.vreme_smestanja_aviona.minute)
        else:
            vreme_smestanja = None

        if self.vreme_napustanja_hangara:
            vreme_napustanja_hangara = '{}.{}.{}, {}:{}'.format(self.vreme_napustanja_hangara.day,
                                                                self.vreme_napustanja_hangara.month,
                                                                self.vreme_napustanja_hangara.year,
                                                                self.vreme_napustanja_hangara.hour,
                                                                self.vreme_napustanja_hangara.minute)
        else:
            vreme_napustanja_hangara = None

        return 'Zahtev za smestanje aviona - Oznaka: {}, Vreme kreiranja: {}, ' \
               'Vreme smestanja: {}, Vreme napustanja: {}, ' \
               'ID Hangara: {}, ID Aviona: {}, ID Menadzera: {} '.format(
                self.id, vreme_kreiranja,
                vreme_smestanja,
                vreme_napustanja_hangara,
                id_hangara,
                self.avion.id, self.menadzer.id)


class ZahtevZaTransport(object):
    def __init__(self, odrediste, IDPotrazitelja, IDZahteva=None,
                 datumKreiranja=None, statusZahteva="kreiran", naziv=None):
        if IDZahteva == None:
            self.IDZahteva = self.odrediIDZahteva()
        else:
            self.IDZahteva = IDZahteva

        if datumKreiranja == None:
            self.datumKreiranja = self.odrediDatum()
        else:
            self.datumKreiranja = datumKreiranja
        self.naziv = naziv
        self.datumTransporta = "None"
        self.odrediste = odrediste
        self.IDPotrazitelja = IDPotrazitelja
        self.avion = "None"  # ovde ces napraviti referencu na avion koji moze da primi robu iz ovog zahteva
        self.statusZahteva = statusZahteva
        self.roba = []

    def sacuvaj(self):
        util.addToFile("zahteviZaTransport.txt",
                       self.IDZahteva + "|" + self.datumKreiranja + "|" + self.datumTransporta +
                       "|" + self.odrediste + "|" + self.IDPotrazitelja + "|" + self.avion +
                       "|" + self.statusZahteva + "\n")

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
        ID=len(lines)+1
        return "ZT#" + str(ID)

    def __str__(self):
        if self.datumTransporta != 'None':
            datumTransporta = '{}.{}.{}, {}:{}'.format(self.datumTransporta.day,
                                                       self.datumTransporta.month,
                                                       self.datumTransporta.year,
                                                       self.datumTransporta.hour,
                                                       self.datumTransporta.minute)
        else:
            datumTransporta = None

        robe = ""
        for r in self.roba:
            robe += r.naziv + ", "
        return "Zahtev za transport - {}, Datum Kreiranja: {}, Odrediste: {}" \
               ", Status: {}, Datum Transporta: {}, Roba: {}".format(self.IDZahteva,
                                                                     self.datumKreiranja,
                                                                     self.odrediste,
                                                                     self.statusZahteva,
                                                                     datumTransporta,
                                                                     robe)

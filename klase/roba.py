import klase.util_funk as util


class Roba(object):
    def __init__(self, naziv, opis, duzina, sirina, visina, tezina, IDZahteva, oznaka=None):
        if oznaka is None:
            self.oznaka = self.odrediIDRobe()
        else:
            self.oznaka = oznaka
        self.naziv = naziv
        self.opis = opis
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina
        self.tezina = tezina
        self.IDZahteva = IDZahteva

    def sacuvaj(self):
        util.addToFile("roba.txt", self.oznaka + "|" + self.naziv + "|" + self.opis + "|" +
                       str(self.duzina) + "|" + str(self.sirina) + "|" + str(self.visina) + "|" + str(self.tezina)
                       + "|" + self.IDZahteva + "\n")

    def odrediIDRobe(self):
        lines = util.readFile("roba.txt")
        ID= len(lines)+1
        return "R#" + str(int(ID))

    def __str__(self):
        return "Roba - {}, Naziv {}, Opis - {}, Duzina:{},Sirina:{},Visina:{},Tezina:{}".format(self.oznaka,
                                                                                                self.naziv,
                                                                                                self.opis,
                                                                                                str(self.duzina),
                                                                                                str(self.sirina),
                                                                                                str(self.visina),
                                                                                                str(self.tezina))

class OznakaINaziv(object):
    def __init__(self, ID, naziv):
        self.id = ID
        self.naziv = naziv


class Dimenzije:
    def __int__(self, duzina, sirina, visina):
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina


class Kolekcija(list):
    def append(self, p_object):
        raise NotImplementedError

    def dodaj(self, objekat):
        list.append(self, objekat)


class Aerodrom(OznakaINaziv, Kolekcija):
    def __init__(self, naziv, adresa, mesto, ID=None):
        OznakaINaziv.__init__(self, ID, naziv)
        self.adresa = adresa
        self.mesto = mesto
        self.hangari = Kolekcija()

    def __str__(self):
        return 'Aerodrom - Naziv: ' + self.naziv + ' Adresa: ' + self.adresa + ' Mesto: ' + self.mesto


class Hangar(OznakaINaziv, Dimenzije, Kolekcija):
    def __init__(self,ID,naziv,duzina,sirina,visina):
        OznakaINaziv.__init__(self,ID,naziv)
        Dimenzije.__int__(self,duzina,sirina,visina)
        self.avioni=Kolekcija()

    def __str__(self):
        av = ''
        for avion in self.avioni:
            av = av + avion.naziv + ','
        return 'Hangar - Oznaka: '+ self.id + ' Naziv: ' + self.naziv + ' Avioni: ' + av


class Avion(OznakaINaziv, Dimenzije, Kolekcija):

    def __init__(self, naziv, duzina, sirina, visina, ID, godiste, rasponKrila, nosivost):
        OznakaINaziv.__init__(self, ID, naziv)
        Dimenzije.__int__(self, duzina, sirina, visina)
        self.godiste = godiste
        self.rasponKrila = rasponKrila
        self.nosivost = nosivost
        self.relacije = Kolekcija()
        self.prostorZaTeret = Kolekcija()

    def __str__(self):
        rel = ''
        for relacija in self.relacije:
            rel = rel + relacija + ','

        return 'Avion - Naziv: ' + self.naziv + ' ID: ' + self.id + ' Godiste: ' + self.godiste + \
               ' Raspon Krila: ' + self.rasponKrila + ' Nosivost: ' + self.nosivost + \
               ' Relacije: ' + rel

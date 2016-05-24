class OznakaINaziv(object):
    def __init__(self, ID, naziv):
        self.id = ID
        self.naziv = naziv

    def __str__(self):
        return ' Oznaka: ' + str(self.id) + ', Naziv: ' + self.naziv


class Dimenzije:
    def __int__(self, duzina, sirina, visina):
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina

    def __lt__(self, other):
        '''self je manji ako je manji po duzini i sirini i visini, odnosno other ne moze da stane u self'''
        if isinstance(self, Hangar) and isinstance(other, Avion):
            return self.duzina < other.duzina and self.sirina < other.rasponKrila and self.visina < other.visina

        elif isinstance(self, Avion) and isinstance(other, Hangar):
            return self.duzina < other.duzina and self.rasponKrila < other.sirina and self.visina < other.visina

        return self.duzina < other.duzina and self.sirina and other.sirina and self.visina < other.visina

    def __le__(self, other):
        if isinstance(self, Hangar) and isinstance(other, Avion):
            return self.duzina <= other.duzina and self.sirina <= other.rasponKrila and self.visina <= other.visina

        elif isinstance(self, Avion) and isinstance(other, Hangar):
            return self.duzina <= other.duzina and self.rasponKrila <= other.sirina and self.visina <= other.visina

        return self.duzina <= other.duzina and self.sirina <= other.sirina and self.visina <= other.visina

    def __eq__(self, other):
        if isinstance(self, Hangar) and isinstance(other, Avion):
            return self.duzina == other.duzina and self.sirina == other.rasponKrila and self.visina == other.visina

        elif isinstance(self, Avion) and isinstance(other, Hangar):
            return self.duzina == other.duzina and self.rasponKrila == other.sirina and self.visina == other.visina

        return self.duzina == other.duzina and self.sirina == other.sirina and self.visina == other.visina

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        if isinstance(self, Hangar) and isinstance(other, Avion):
            return self.duzina >= other.duzina and self.sirina >= other.rasponKrila and self.visina >= other.visina

        elif isinstance(self, Avion) and isinstance(other, Hangar):
            return self.duzina >= other.duzina and self.rasponKrila >= other.sirina and self.visina >= other.visina

        return self.duzina >= other.duzina and self.sirina >= other.sirina and self.visina >= other.visina

    def __gt__(self, other):
        if isinstance(self, Hangar) and isinstance(other, Avion):
            return self.duzina > other.duzina and self.sirina > other.rasponKrila and self.visina > other.visina

        elif isinstance(self, Avion) and isinstance(other, Hangar):
            return self.duzina > other.duzina and self.rasponKrila > other.sirina and self.visina > other.visina

        return self.duzina > other.duzina and self.sirina > other.sirina and self.visina > other.visina


        # poredjenja za sve objekte koji imaju dimenzije


class Kolekcija(list):
    def __init__(self):
        super().__init__(self)

    def append(self, p_object):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    def copy(self):
        raise NotImplementedError

    def extend(self, iterable):
        raise NotImplementedError

    def insert(self, index, p_object):
        raise NotImplementedError

    def pop(self, index=None):
        raise NotImplementedError

    def remove(self, value):
        raise NotImplementedError

    def dodaj(self, objekat):
        list.append(self, objekat)


class Aerodrom(OznakaINaziv, Kolekcija):
    def __init__(self, naziv, adresa, mesto, ID=None):
        OznakaINaziv.__init__(self, ID, naziv)
        Kolekcija.__init__(self)
        self.adresa = adresa
        self.mesto = mesto

    def __str__(self):
        hangari = ''
        for hangar in self:
            hangari = hangari + hangar.naziv + ', '
        return 'Aerodrom - Naziv: ' + self.naziv + ', Adresa: ' + self.adresa + ', Mesto: ' + self.mesto \
               + ', Hangari: ' + hangari


class Hangar(OznakaINaziv, Dimenzije, Kolekcija):
    def __init__(self, ID, naziv, duzina, sirina, visina):
        OznakaINaziv.__init__(self, ID, naziv)
        Dimenzije.__int__(self, duzina, sirina, visina)
        Kolekcija.__init__(self)

    def __str__(self):
        av = ''
        for avion in self:
            av = av + avion.naziv + ','
        return 'Hangar ' + OznakaINaziv.__str__(self) + ', Avioni: ' + av


class Avion(OznakaINaziv, Dimenzije, Kolekcija):
    def __init__(self, ID, naziv, duzina, sirina, visina, godiste, rasponKrila, nosivost, relacija):
        OznakaINaziv.__init__(self, ID, naziv)
        Dimenzije.__int__(self, duzina, sirina, visina)
        Kolekcija.__init__(self)
        self.godiste = godiste
        self.rasponKrila = rasponKrila
        self.nosivost = nosivost
        self.relacija = relacija

    def __str__(self):
        return 'Avion ' + OznakaINaziv.__str__(self) + ', Godiste: ' + str(self.godiste) + \
               ', Raspon Krila: ' + str(self.rasponKrila) + ', Nosivost: ' + str(self.nosivost) + \
               ', Relacije: ' + self.relacija


class ProstorZaTeret(OznakaINaziv, Dimenzije, Kolekcija):
    def __init__(self, naziv, duzina, sirina, visina, ID=None):
        OznakaINaziv.__init__(self, ID, naziv)
        Dimenzije.__int__(self, duzina, visina, sirina)
        Kolekcija.__init__(self)

    def __str__(self):
        roba = ''
        for r in self:
            roba = roba + r + ', '

        return OznakaINaziv.__str__(self) + ' Roba: ' + roba




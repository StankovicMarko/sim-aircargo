class OznakaINaziv(object):
    def __init__(self, ID, naziv):
        self.id = ID
        self.naziv = naziv


class Dimenzije:
    def __int__(self, duzina, sirina, visina):
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina

    def smanji_dimenzije(self, other):
        """umanjuje dimenzije objekta self za dimenzije objekta other. Funkcija ce smanjiti onu dimenziju
        objekta self koja je suprotna vecoj. npr ako je sirina objekta other veca od njegove duzine, self-u
        ce se smanjiti duzina"""
        if isinstance(self, Hangar) and isinstance(other, Avion):
            if other.duzina >= other.raspon_krila:
                self.sirina -= other.raspon_krila
            elif other.duzina < other.raspon_krila:
                self.duzina -= other.duzina
        else:
            if other.duzina >= other.sirina:
                self.sirina -= other.sirina
            elif other.duzina < other.sirina:
                self.duzina -= other.duzina

    def povecaj_dimenzije(self, other):
        """funkcija je inverzna funkciji smanji_dimenziju, kada other napusti self dimenzije self-a se
        povecavaju za ono sto je other smanjio"""
        if isinstance(self, Hangar) and isinstance(other, Avion):
            if other.duzina >= other.raspon_krila:
                self.sirina += other.raspon_krila
            elif other.duzina < other.raspon_krila:
                self.duzina += other.duzina
        else:
            if other.duzina >= other.sirina:
                self.sirina += other.sirina
            elif other.duzina < other.sirina:
                self.duzina += other.duzina

    def __lt__(self, other):
        """self je manji ako je manji po duzini i sirini i visini, odnosno other ne moze da stane u self"""
        if isinstance(self, Hangar) and isinstance(other, Avion):
            return self.duzina < other.duzina and self.sirina < other.raspon_krila and self.visina < other.visina

        elif isinstance(self, Avion) and isinstance(other, Hangar):
            return self.duzina < other.duzina and self.raspon_krila < other.sirina and self.visina < other.visina

        return self.duzina < other.duzina and self.sirina and other.sirina and self.visina < other.visina

    def __le__(self, other):
        if isinstance(self, Hangar) and isinstance(other, Avion):
            return self.duzina <= other.duzina and self.sirina <= other.raspon_krila and self.visina <= other.visina

        elif isinstance(self, Avion) and isinstance(other, Hangar):
            return self.duzina <= other.duzina and self.raspon_krila <= other.sirina and self.visina <= other.visina

        return self.duzina <= other.duzina and self.sirina <= other.sirina and self.visina <= other.visina

    def __eq__(self, other):
        if isinstance(self, Hangar) and isinstance(other, Avion):
            return self.duzina == other.duzina and self.sirina == other.raspon_krila and self.visina == other.visina

        elif isinstance(self, Avion) and isinstance(other, Hangar):
            return self.duzina == other.duzina and self.raspon_krila == other.sirina and self.visina == other.visina

        return self.duzina == other.duzina and self.sirina == other.sirina and self.visina == other.visina

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        if isinstance(self, Hangar) and isinstance(other, Avion):
            return self.duzina >= other.duzina and self.sirina >= other.raspon_krila and self.visina >= other.visina

        elif isinstance(self, Avion) and isinstance(other, Hangar):
            return self.duzina >= other.duzina and self.raspon_krila >= other.sirina and self.visina >= other.visina

        return self.duzina >= other.duzina and self.sirina >= other.sirina and self.visina >= other.visina

    def __gt__(self, other):
        if isinstance(self, Hangar) and isinstance(other, Avion):
            return self.duzina > other.duzina and self.sirina > other.raspon_krila and self.visina > other.visina

        elif isinstance(self, Avion) and isinstance(other, Hangar):
            return self.duzina > other.duzina and self.raspon_krila > other.sirina and self.visina > other.visina

        return self.duzina > other.duzina and self.sirina > other.sirina and self.visina > other.visina


class Kolekcija(Dimenzije, list):
    def __init__(self, duzina, sirina, visina):
        Dimenzije.__int__(self, duzina, sirina, visina)
        list.__init__(self)

    # def append(self, p_object):
    #     raise NotImplementedError
    #
    # def clear(self):
    #     raise NotImplementedError
    #
    # def copy(self):
    #     raise NotImplementedError
    #
    # def extend(self, iterable):
    #     raise NotImplementedError
    #
    # def insert(self, index, p_object):
    #     raise NotImplementedError
    #
    # def remove(self, value):
    #     raise NotImplementedError

    def dodaj(self, other):
        if isinstance(self, Aerodrom) and isinstance(other, Hangar) \
                or isinstance(self, Avion) and isinstance(other, ProstorZaRobu):
            list.append(self, other)
        else:
            list.append(self, other)
            self.smanji_dimenzije(other)

    def ukloni(self, other):
        if isinstance(self, Aerodrom) and isinstance(other, Hangar) \
                or isinstance(self, Avion) and isinstance(other, ProstorZaRobu):
            list.remove(self, other)
        else:
            list.remove(self, other)
            self.povecaj_dimenzije(other)


class Aerodrom(OznakaINaziv, Kolekcija):
    def __init__(self, naziv, adresa, mesto, ID=None, duzina=None, sirina=None, visina=None):
        OznakaINaziv.__init__(self, ID, naziv)
        Kolekcija.__init__(self, duzina, sirina, visina)
        self.adresa = adresa
        self.mesto = mesto

    def __str__(self):
        hangari = ''
        for hangar in self:
            hangari = hangari + hangar.naziv + ', '
        return "Aerodrom - Naziv: {}, Adresa: {}, Mesto: {}, Hangari: {}".format(self.naziv, self.adresa, self.mesto,
                                                                                 hangari)


class Hangar(OznakaINaziv, Kolekcija):
    def __init__(self, ID, naziv, duzina, sirina, visina):
        OznakaINaziv.__init__(self, ID, naziv)
        Kolekcija.__init__(self, duzina, sirina, visina)

    def __str__(self):
        av = ''
        for avion in self:
            av = av + avion.naziv + ','
        return 'Hangar - Oznaka: {}, Naziv: {}, Avioni: {}'.format(self.id, self.naziv, av)


class Avion(OznakaINaziv, Kolekcija):
    def __init__(self, ID, naziv, duzina, sirina, visina, raspon_krila, godiste, nosivost, relacija):
        OznakaINaziv.__init__(self, ID, naziv)
        Kolekcija.__init__(self, duzina, sirina, visina)
        self.raspon_krila = raspon_krila
        self.godiste = godiste
        self.nosivost = nosivost
        self.relacija = relacija
        self.se_nalazi = None
        self.zahtev_smestanje = None
        self.zahtev_transport = None

    def __str__(self):
        return 'Avion - Oznaka: {}, Godiste: {}, Raspon krila: {}, ' \
               'Nosivost: {}, Relacija: {}'.format(self.id,
                                                   self.godiste,
                                                   str(
                                                       self.raspon_krila),
                                                   str(
                                                       self.nosivost),
                                                   self.relacija)


class ProstorZaRobu(OznakaINaziv, Kolekcija):
    def __init__(self, naziv, duzina, sirina, visina, ID=None):
        OznakaINaziv.__init__(self, ID, naziv)
        Kolekcija.__init__(self, duzina, visina, sirina)

    def __str__(self):
        roba = ''
        for r in self:
            roba = roba + r + ', '

        return 'Oznaka: {}, Naziv: {}, Roba: {}'.format(self.id, self.naziv, roba)

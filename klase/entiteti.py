class OznakaINaziv(object):
    """Klasa sadrzi: Oznaku (id) i naziv (ime) svih entiteta u projektu"""
    def __init__(self, ID, naziv):
        self.id = ID
        self.naziv = naziv


class Dimenzije:
    """Ova klasa sadrzi podatke o dimenzijama, svaki objekat koji ima dimenziju nasledjuje ovu klasu"""
    def __int__(self, duzina, sirina, visina):
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina

    def smanji_dimenzije(self, other):
        """umanjuje dimenzije objekta self za dimenzije objekta other. Funkcija ce smanjiti onu dimenziju
        objekta self koja je suprotna vecoj. npr ako je sirina objekta other veca od njegove duzine, self-u
        ce se smanjiti duzina. Graficki primer je

                    HANGAR        sirina=60                 |              HANGAR        sirina=60
        +------------------------------------------+        |  +------------------------------------------+
        |                                          |        |  | +---------------+     X    X       X     |
        |                                          |        |  | |               |  X      X    X      X  |
        |                                          |        |  | |               |      zauzet prostor    |
        |                                          |        |  | |               |   X                 X  |
        |                                          |d       |  | |               |    X  X   X   X  X     |d
        |                                          |u       |  | +---------------+      X      X     X  X |u
        |                                          |z=40    |  +------------------------------------------+z=40
        |                                          |i       |  |                                          |i
        |                                          |n       |  |                                          |n
        |                                          |a       |  |                                          |a
        |                                          |        |  |                                          |
        |                                          |        |  |                                          |
        |                                          |        |  |                                          |
        |                                          |        |  |                                          |
        |                                          |        |  |                                          |
        |                                          |        |  |                                          |
        |                                          |        |  |                                          |
        |                                          |        |  |                                          |
        +------------------------------------------+        |  +------------------------------------------+
                                                            |
                                                            |       sirina AVIONA je veca od njegove duzine
                AVION                                       |       stoga se smanjuje duzina hangara
            +---------------+d                              |
            |               |u                              |
            |               |z=15                           |
            |               |i                              |
            |               |n                              |
            +---------------+a                              |
               sirina = 20                                  |

        specijalni slucajevi:
        -ako je duzina objekta other veca ili jednaka sirini (other.duzina >= other.sirina):
            smanjuje se sirina objekta self
        """
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
        """objekat self je manji od objekta other ako je manji po duzini i sirini i visini.
            Odnosno objekat other moze da stane u objekat self.
            Specijalni slucajevi:
                -ako se porede Hangar i Avion:
                    u obzir se uzima raspon krila aviona, a ne njegova sirina"""
        if isinstance(self, Hangar) and isinstance(other, Avion):
            return self.duzina < other.duzina and self.sirina < other.raspon_krila and self.visina < other.visina

        elif isinstance(self, Avion) and isinstance(other, Hangar):
            return self.duzina < other.duzina and self.raspon_krila < other.sirina and self.visina < other.visina

        return self.duzina < other.duzina and self.sirina and other.sirina and self.visina < other.visina

    def __le__(self, other):
        """objekat self je manji ili jednak objektu other ako je self manji ili jednak po duzini i sirini i visini.
            Specijalni slucajevi:
                -ako se porede Hangar i Avion:
                    u obzir se uzima raspon krila aviona, a ne njegova sirina"""
        if isinstance(self, Hangar) and isinstance(other, Avion):
            return self.duzina <= other.duzina and self.sirina <= other.raspon_krila and self.visina <= other.visina

        elif isinstance(self, Avion) and isinstance(other, Hangar):
            return self.duzina <= other.duzina and self.raspon_krila <= other.sirina and self.visina <= other.visina

        return self.duzina <= other.duzina and self.sirina <= other.sirina and self.visina <= other.visina

    def __eq__(self, other):
        """objekat self je jednak objektu other ako su jednaki po duzini i sirini i visini.
            Specijalni slucajevi:
                -ako se porede Hangar i Avion:
                    u obzir se uzima raspon krila aviona, a ne njegova sirina"""
        if isinstance(self, Hangar) and isinstance(other, Avion):
            return self.duzina == other.duzina and self.sirina == other.raspon_krila and self.visina == other.visina

        elif isinstance(self, Avion) and isinstance(other, Hangar):
            return self.duzina == other.duzina and self.raspon_krila == other.sirina and self.visina == other.visina

        return self.duzina == other.duzina and self.sirina == other.sirina and self.visina == other.visina

    def __ne__(self, other):
        """operator !=, not ==, invertno od == (eq) funkcije"""
        return not self.__eq__(other)

    def __ge__(self, other):
        """objekat self je veci ili jednak od objekta other ako je veci ili jednak po duzini i sirini i visini.
            Specijalni slucajevi:
                -ako se porede Hangar i Avion:
                    u obzir se uzima raspon krila aviona, a ne njegova sirina"""
        if isinstance(self, Hangar) and isinstance(other, Avion):
            return self.duzina >= other.duzina and self.sirina >= other.raspon_krila and self.visina >= other.visina

        elif isinstance(self, Avion) and isinstance(other, Hangar):
            return self.duzina >= other.duzina and self.raspon_krila >= other.sirina and self.visina >= other.visina

        return self.duzina >= other.duzina and self.sirina >= other.sirina and self.visina >= other.visina

    def __gt__(self, other):
        """objekat self je veci od objekta other ako je veci po duzini i sirini i visini.
            Specijalni slucajevi:
                -ako se porede Hangar i Avion:
                    u obzir se uzima raspon krila aviona, a ne njegova sirina"""
        if isinstance(self, Hangar) and isinstance(other, Avion):
            return self.duzina > other.duzina and self.sirina > other.raspon_krila and self.visina > other.visina

        elif isinstance(self, Avion) and isinstance(other, Hangar):
            return self.duzina > other.duzina and self.raspon_krila > other.sirina and self.visina > other.visina

        return self.duzina > other.duzina and self.sirina > other.sirina and self.visina > other.visina


class Kolekcija(Dimenzije, list):
    """Klasa koja nasledjuje listu, inicijalizuje se pri kreiranju objekata
        Aerodroma, Hangara, Aviona, Prostora za teret."""
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
        """Dodaje objekat other u objekat self i pritom smanjuje dimenzije prema sablonu iz Klase Dimenzije
            metoda: smanji_dimenzije.
        Specijalni slucajevi:
            -ako se u Aerodrom dodaje Hangar ne smanjuju se dimenzije jer Aerodrom nema definisane dimenzije
            -ako se u Avion dodaje Prostor za robu ne smanjuju se dimenzije (ali pri stvaranju Prostora za robu
                proverava da moze da stane u Avion)"""

        if isinstance(self, Aerodrom) and isinstance(other, Hangar) \
                or isinstance(self, Avion) and isinstance(other, ProstorZaRobu):
            list.append(self, other)
        else:
            list.append(self, other)
            self.smanji_dimenzije(other)

    def ukloni(self, other):
        """Izbacuje objekat other iz objekta self i pritom uvecava dimenzije prema sablonu iz Klase Dimenzije
            metoda: povecaj_dimenzije(inverzno smanji_dimenzije).
        Specijalni slucajevi:
            -ako se u Aerodrom dodaje Hangar ne smanjuju se dimenzije jer Aerodrom nema definisane dimenzije
            -ako se u Avion dodaje Prostor za robu ne smanjuju se dimenzije (ali pri stvaranju Prostora za robu
                proverava da moze da stane u Avion)"""
        if isinstance(self, Aerodrom) and isinstance(other, Hangar) \
                or isinstance(self, Avion) and isinstance(other, ProstorZaRobu):
            list.remove(self, other)
        else:
            list.remove(self, other)
            self.povecaj_dimenzije(other)


class Aerodrom(OznakaINaziv, Kolekcija):
    """Pravi objekat Aerodroma. Mogu da se dodaju Hangari (neogranicen broj jer nema definisanih dimenzija)
        Aerodrom opisuju Naziv, Adresa, Mesto i Hangari koje sadrzi"""
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
    """Pravi objekat Hangara. Mogu da se dodaju Avioni. Hangar opisuju ID, Naziv, Duzina, Sirina, Visina i Avioni
    koje sadrzi"""
    def __init__(self, ID, naziv, duzina, sirina, visina):
        OznakaINaziv.__init__(self, ID, naziv)
        Kolekcija.__init__(self, duzina, sirina, visina)

    def __str__(self):
        av = ''
        for avion in self:
            av += avion.naziv + ', '
        return 'Hangar - Oznaka: {}, Naziv: {}, Duzina: {}, Sirina: {}, Visina: {}' \
               ' Avioni: {}'.format(self.id, self.naziv, self.duzina, self.sirina, self.visina, av)


class Avion(OznakaINaziv, Kolekcija):
    """Pravi objekat Aviona. Mogu da se dodaju Prostori za robu. Avion opisuju
        ID, Naziv, Duzina, Sirina, Visina i Prostori za robu koje sadrzi"""
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
        if self.se_nalazi:
            naziv_hangara=self.se_nalazi.naziv
        else:
            naziv_hangara='Van Aerodroma'
        return 'Avion - Oznaka: {}, Naziv: {}, Godiste: {}, ' \
               'Duzina: {}, Raspon krila: {}, Visina: {}, ' \
               'Nosivost: {}, Relacija: {}, Nalazi se: {}'.format(self.id,
                                                                  self.naziv,
                                                                  self.godiste,
                                                                  str(self.duzina),
                                                                  str(
                                                                       self.raspon_krila),
                                                                  str(self.visina),
                                                                  str(
                                                                       self.nosivost),
                                                                  self.relacija,
                                                                  naziv_hangara)


class ProstorZaRobu(OznakaINaziv, Kolekcija):
    """Pravi objekat Prostora za robu. Moze da se dodaje Roba.
        Prostor za robu opisuju ID, Naziv, Duzina, Sirina, Visina i Roba koju sadrzi"""
    def __init__(self, naziv, duzina, sirina, visina, ID=None):
        OznakaINaziv.__init__(self, ID, naziv)
        Kolekcija.__init__(self, duzina, visina, sirina)

    def __str__(self):
        roba = ''
        for r in self:
            roba += r.naziv + ', '

        return 'Oznaka: {}, Naziv: {}, Duzina: {}, Sirina: {}, Visina: {}, Roba: {}'.format(self.id,
                                                                                            self.naziv,
                                                                                            self.duzina,
                                                                                            self.sirina,
                                                                                            self.visina,
                                                                                            roba)

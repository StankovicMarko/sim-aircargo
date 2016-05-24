from gui.windows import Glavna
from klase.korisnici import MenadzerHangara, Zaposlen, Osoba
from klase.entiteti import Kolekcija, Aerodrom, Avion, Hangar, ProstorZaTeret
from klase.zahtevi import ZahtevZaSmestanjeAviona

zahteviZaSmestanjeAviona = []
zahteviZaTransportRobe = {'kreiran': [], 'odobren': [], 'robaUtovarena': [], 'robaTransportovana': []}
avioniUHangarima = []
avioniVanHangara = []
aerodrom = Aerodrom('Nikola Tesla', 'Futoski Put', 'Novi Sad')


def main():
    hangar = Hangar(1, 'HANG1', 100, 100, 30)
    aerodrom.dodaj(hangar)
    # avion = Avion(1, 'Av1', 5, 5, 5, 2012, 10, 10)
    # avion.relacije.dodaj('Pariz')
    # avion.relacije.dodaj('London')
    # avion.relacije.dodaj('Lisabon')
    #
    # hangar.avioni.dodaj(avion)
    # avioniUHangarima.extend(hangar.avioni)

    menHangara = MenadzerHangara(1, 'Lepan', 'Lepavi', 'lepi', 12345)

    print(aerodrom, hangar, menHangara, len(aerodrom), sep='\n')
    #
    # print(hangar < avion, hangar > avion, avion < hangar, avion > hangar)
    # print()
    # print(hangar >= avion, hangar <= avion, hangar == avion, avion >= hangar, avion <= hangar, avion == hangar,
    #       avion != hangar, hangar != avion)

    dodajHangar()

    for hangar in aerodrom:
        print(hangar)

    dodajAvion()

    for hangar in aerodrom:
        print(hangar)

    for avion in avioniUHangarima:
        print(avion)

    print('---------')
    for hangar in aerodrom:
        for avion in hangar:
            for pzt in avion:
                print(pzt)


# ovo koristi menazder hangara (pitao sam profu kaze moze ovako a i meni je lakse zbog gui-a)

def prikaziZahteveZaSmestanjeAviona():
    prikaz = ''
    for zahtev in zahteviZaSmestanjeAviona:
        prikaz = prikaz + str(zahtev) + '\n'
    return prikaz


def prikazZahtevaZaTransportRobe():
    prikaz = ''
    for zahtev['robaUtovarena'] in zahteviZaTransportRobe:
        prikaz = prikaz + str(zahtev) + '\n'
    return prikaz


def uzmiInpute():
    inputi = []
    unos = ''
    while unos != 'q':
        inputi.append(unos)
        unos = input('unesite input, q za kraj:')

    inputi = [unos for unos in inputi if unos != '']

    return inputi


def dodajHangar():
    # u gui-u ce ovo uzimati input
    ID = len(aerodrom) + 1
    print('unesite Hangar treba nam: naziv, duzinu, sirinu, visinu')
    l = uzmiInpute()
    while len(l) < 4:
        print('premalo unesenih inputa')
        print('unesite Hangar treba nam: naziv, duzinu, sirinu, visinu')
        l = uzmiInpute()
    hangar = Hangar(ID, naziv=l[0], duzina=int(l[1]), sirina=int(l[2]), visina=int(l[3]))
    aerodrom.dodaj(hangar)


def dodajAvion():
    ID = len(avioniUHangarima)
    print('unesite Avion treba nam: naziv,duzinu, sirinu, visinu, godiste, rasponKrila, nosivost, relacija')
    l = uzmiInpute()
    while len(l) < 7:
        print('premalo unesenih inputa')
        print('unesite Avion treba nam: naziv,duzinu, sirinu, visinu, godiste, rasponKrila, nosivost, relacija')
        l = uzmiInpute()
    avion = Avion(ID, naziv=l[0], duzina=int(l[1]), sirina=int(l[2]), visina=int(l[3]), godiste=l[4],
                  rasponKrila=int(l[5]), nosivost=int(l[6]), relacija=l[7])
    proZaTeret = _napraviProstorZaTeret()
    while avion < proZaTeret:
        proZaTeret = _napraviProstorZaTeret()

    avion.dodaj(proZaTeret)
    try:
        _smesti(avion)
    except:
        print('Avion je prevelik i ne moze da stane ni u jedan hangar, molimo dodajte hangar,'
              ' ovaj avion ce biti u aerodromu poslovnog partnera')
        avioniVanHangara.append(avion)


def _smesti(avion):
    for hangar in aerodrom:
        if hangar > avion:
            hangar.dodaj(avion)
            avioniUHangarima.append(avion)
            break
    raise NemaMesta as Warning


def _napraviProstorZaTeret():
    print('unesite Prostor Za Teret treba nam: naziv, duzinu, sirinu, visinu')
    l = uzmiInpute()
    while len(l) < 4:
        print('premalo unesenih inputa')
        print('unesite Prostor Za Teret treba nam: naziv, duzinu, sirinu, visinu')
        l = uzmiInpute()
    proZaTer = ProstorZaTeret(naziv=l[0], duzina=int(l[1]), sirina=int(l[2]), visina=int(l[3]), ID=None)

    return proZaTer

    # def kreirajZahtevZaSmestanje():
    #
    #     for i, avion in enumerate(avioniVanHangara):
    #         try:
    #             _smesti(avion)
    #             avionZaSmestanje=avioniVanHangara.pop(i)
    #
    #
    #         except:



    # application = Glavna()
    # application.mainloop()


if __name__ == "__main__":
    main()

from gui.windows import Glavna
from klase.korisnici import MenadzerHangara, Zaposlen, Osoba
from klase.entiteti import Kolekcija, Aerodrom, Avion, Hangar, ProstorZaTeret
from klase.zahtevi import ZahtevZaSmestanjeAviona

zahtevi_za_smestanje_aviona = []
zahtevi_za_transport_robe = {'kreiran': [], 'odobren': [], 'robaUtovarena': [], 'robaTransportovana': []}
avioni_u_hangarima = []
avioni_van_hangara = []
aerodrom = Aerodrom('Nikola Tesla', 'Futoski Put', 'Novi Sad')


def main():
    h = Hangar(1, 'HANG1', 100, 100, 30)

    han = Hangar(2, 'hang007', 100, 100, 300)

    aerodrom.dodaj(han)
    aerodrom.dodaj(h)
    # avion = Avion(1, 'Av1', 5, 5, 5, 2012, 10, 10)
    # avion.relacije.dodaj('Pariz')
    # avion.relacije.dodaj('London')
    # avion.relacije.dodaj('Lisabon')
    #
    # hangar.avioni.dodaj(avion)
    # avioniUHangarima.extend(hangar.avioni)

    men_hangara = MenadzerHangara(1, 'Lepan', 'Lepavi', 'lepi', 12345)

    print(aerodrom, h, han, men_hangara, len(aerodrom), sep='\n')
    #
    # print(hangar < avion, hangar > avion, avion < hangar, avion > hangar)
    # print()
    # print(hangar >= avion, hangar <= avion, hangar == avion, avion >= hangar, avion <= hangar, avion == hangar,
    #       avion != hangar, hangar != avion)

    dodaj_hangar()

    for hangar in aerodrom:
        print(hangar)

    dodaj_avion()

    for hangar in aerodrom:
        print(hangar)

    for avion in avioni_u_hangarima:
        print(avion)

    print('---------')
    for hangar in aerodrom:
        for avion in hangar:
            for pzt in avion:
                print(pzt)


def prikazi_zahteve_za_smestanje_aviona():
    prikaz = ''
    for zahtev in zahtevi_za_smestanje_aviona:
        prikaz = prikaz + str(zahtev) + '\n'
    return prikaz


def prikaz_zahteva_za_transport_robe():
    prikaz = ''
    for zahtev in zahtevi_za_transport_robe['robaUtovarena']:
        prikaz = prikaz + str(zahtev) + '\n'
    return prikaz


def uzmi_inpute():
    inputi = []
    unos = ''
    while unos != 'q':
        inputi.append(unos)
        unos = input('unesite input, q za kraj:')

    inputi = [unos for unos in inputi if unos != '']

    return inputi


def dodaj_hangar():
    # u gui-u ce ovo uzimati input
    ID = len(aerodrom) + 1
    print('unesite Hangar treba nam: naziv, duzinu, sirinu, visinu')
    l = uzmi_inpute()
    while len(l) < 4:
        print('premalo unesenih inputa')
        print('unesite Hangar treba nam: naziv, duzinu, sirinu, visinu')
        l = uzmi_inpute()
    hangar = Hangar(ID, naziv=l[0], duzina=int(l[1]), sirina=int(l[2]), visina=int(l[3]))
    aerodrom.dodaj(hangar)


def dodaj_avion():
    ID = len(avioni_u_hangarima)
    print('unesite Avion treba nam: naziv,duzinu, sirinu, visinu, godiste, rasponKrila, nosivost, relacija')
    l = uzmi_inpute()
    while len(l) < 7:
        print('premalo unesenih inputa')
        print('unesite Avion treba nam: naziv,duzinu, sirinu, visinu, godiste, rasponKrila, nosivost, relacija')
        l = uzmi_inpute()
    avion = Avion(ID, naziv=l[0], duzina=int(l[1]), sirina=int(l[2]), visina=int(l[3]), godiste=l[4],
                  raspon_krila=int(l[5]), nosivost=int(l[6]), relacija=l[7])
    pr_za_ter = _napravi_prostor_za_teret()
    while avion < pr_za_ter:
        pr_za_ter = _napravi_prostor_za_teret()

    avion.dodaj(pr_za_ter)
    try:
        _smesti(avion)
    except:
        print('Avion je prevelik i ne moze da stane ni u jedan hangar, molimo dodajte hangar,'
              ' ovaj avion ce biti u aerodromu poslovnog partnera')
        avioni_van_hangara.append(avion)


def _smesti(avion):
    for hangar in aerodrom:
        if hangar > avion:
            hangar.dodaj(avion)
            avioni_u_hangarima.append(avion)
            break
    raise Warning


def _napravi_prostor_za_teret():
    print('unesite Prostor Za Teret treba nam: naziv, duzinu, sirinu, visinu')
    l = uzmi_inpute()
    while len(l) < 4:
        print('premalo unesenih inputa')
        print('unesite Prostor Za Teret treba nam: naziv, duzinu, sirinu, visinu')
        l = uzmi_inpute()
    pr_za_ter = ProstorZaTeret(naziv=l[0], duzina=int(l[1]), sirina=int(l[2]), visina=int(l[3]), ID=None)

    return pr_za_ter

    # def kreirajZahtevZaSmestanje():
    #
    #     for i, avion in enumerate(avioniVanHangara):
    #         try:
    #             _smesti(avion)
    #             avionZaSmestanje=avioniVanHangara.pop(i)
    #
    #
    #         except:


    # menHangara= MenadzerHangara("1","petar","peric", 'aaaa', 12345, )

    # print(menHangara)


if __name__ == "__main__":
    # main()
    application = Glavna()
    application.mainloop()

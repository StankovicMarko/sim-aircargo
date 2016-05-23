from gui.windows import Glavna
from klase.korisnici import MenadzerHangara, Zaposlen, Osoba
from klase.entiteti import Kolekcija, Aerodrom, Avion, Hangar
from klase.zahtevi import ZahtevZaSmestanjeAviona
from collections import deque

zahteviZaSmestanjeAviona = []
zahteviZaTransportRobe = {'kreiran': [], 'odobren': [], 'robaUtovarena': [], 'robaTransportovana': []}
avioniUHangarima = []
avioniVanHangara = deque()

# def main():
aerodrom = Aerodrom('Nikola Tesla', 'Futoski Put', 'Novi Sad')
hangar = Hangar(1, 'HANG1', 10, 11, 10)
aerodrom.hangari.dodaj(hangar)
avion = Avion(1, 'Av1', 5, 5, 5, 2012, 10, 10)
avion.relacije.dodaj('Pariz')
avion.relacije.dodaj('London')
avion.relacije.dodaj('Lisabon')

hangar.avioni.dodaj(avion)
avioniUHangarima.extend(hangar.avioni)

menHangara = MenadzerHangara(1, 'Lepan', 'Lepavi', 'lepi', 12345)

print(aerodrom, hangar, avion, menHangara, sep='\n')

print(hangar < avion, hangar > avion, avion < hangar, avion > hangar)
print()
print(hangar >= avion, hangar <= avion, hangar == avion, avion >= hangar, avion <= hangar, avion == hangar,
      avion != hangar, hangar != avion)


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


def dodajHangar():
    # u gui-u ce ovo uzimati input
    ID = len(aerodrom.hangari)
    naziv = input('naziv hangara: ')
    duzina = input('duzina hangara: ')
    sirina = input('sirina hangara: ')
    visina = input('visina hangara: ')

    hangar = Hangar(ID, naziv, duzina, sirina, visina)
    aerodrom.hangari.dodaj(hangar)


def dodajAvion():
    ID = len(avioniUHangarima)
    naziv = input('naziv aviona: ')
    duzina = input('duzina aviona: ')
    sirina = input('sirina aviona: ')
    visina = input('visina aviona: ')
    godiste = input('godiste aviona: ')
    rasponKrila = input('raspon krila: ')
    nosivost = input('nosivost: ')
    avion = Avion(ID, naziv, duzina, sirina, visina, godiste, rasponKrila, nosivost)

    # i tu ce morati inputi menazdera
    naziv = input('naziv prostoraZaTeret: ')
    duzina = input('duzina prostoraZaTeret: ')
    sirina = input('sirina prostoraZaTeret: ')
    visina = input('visina prostoraZaTeret: ')
    proZaTer = ProstorZaTeret()

    # mora biti provera
    if avion > proZaTer:
        avion.prostorZaTeret.dodaj(proZaTer)

    # mora da proba da udje u hangar ako ne moze ide u deque
    for hangar in aerodrom.hangari:
        if avion < hangar:
            hangar.dodaj(avion)

    avioniVanHangara.append(avion)




    # application = Glavna()
    # application.mainloop()

# if __name__ == "__main__":
#    main()

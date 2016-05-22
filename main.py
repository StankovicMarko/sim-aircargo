from gui.windows import Glavna
from klase.korisnici import MenadzerHangara, Zaposlen, Osoba
from klase.entiteti import Kolekcija, Aerodrom, Avion, Hangar


def main():
    avion = Avion('Boing 747', '5', '3', '2', '123', '2014', '39', '459')
    print(avion)

    print(avion.relacije)

    avion.relacije.dodaj("Pariz")
    avion.relacije.dodaj("London")
    avion.relacije.dodaj("Lisabon")

    print(avion)

    hangar1=Hangar('1','hangar1','30','40','10')
    hangar1.avioni.dodaj(avion)

    print(hangar1)

    # menHangara= MenadzerHangara("1","petar","peric", 'aaaa', 12345, )
    #
    # print(menHangara)

    # lala='aakala'
    #
    # kol=Kolekcija()
    #
    # kol.dodaj(lala)
    #
    # print(kol)
    # kol.append(lala)


    # hangar = 'lolisa'
    # hangar2= 'alavko'
    # aero = Aerodrom('aerodrom', 1, 2, 3, 'ns', 'ns')
    #
    # print(aero)
    #
    # print(hangar)
    #
    # aero.dodaj(hangar)
    # aero.dodaj(hangar2)
    #
    # print(aero.hangari)



    # application = Glavna()
    # application.mainloop()


if __name__ == "__main__":
    main()

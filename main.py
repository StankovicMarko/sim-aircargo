from gui.windows import Glavna
from klase.korisnici import MenadzerHangara, Zaposlen, Osoba


def main():



    menHangara= MenadzerHangara("1","petar","peric", 'aaaa', 12345, )

    print(menHangara)

    # application = Glavna()
    # application.mainloop()


if __name__ == "__main__":
    main()

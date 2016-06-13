from klase.korisnici import MenadzerHangara
from klase.entiteti import Aerodrom, Avion, Hangar, ProstorZaRobu
from klase.util_funk import snimi_entitet, ucitaj_entitet
from klase.zahtevi import ZahtevZaSmestanjeAviona
import datetime as dt
# Marko J dodao:
import klase.util_funk as util
import klase.zahtevi
import klase.roba


# zahtevi_za_smestanje_aviona = []
# zahtevi_za_transport_robe = {'kreiran': [], 'odobren': [], 'robaUtovarena': [], 'robaTransportovana': []}
# avioni_u_hangarima = []
# avioni_van_hangara = []  # deque
# aerodrom = Aerodrom('Nikola Tesla', 'Futoski Put', 'Novi Sad')
# menadzer_hangara = MenadzerHangara(1, 'Lepan', 'Lepavi', 'lepi', 12345)  # PROBA MEN HANGARA TREBA DA JE ULOGOVAN
# temp_prostor_za_robu = []

zahtevi_za_smestanje_aviona = None
zahtevi_za_transport_robe = None
avioni_u_hangarima = None
avioni_van_hangara = None
aerodrom = None
menadzer_hangara = MenadzerHangara(1, 'Lepan', 'Lepavi', 'lepi', 12345)  # PROBA MEN HANGARA TREBA DA JE ULOGOVAN
temp_prostor_za_robu = []


# def ucitaj_sve_entitete():
#     zahtevi_za_smestanje_aviona=ucitaj_entitet('zahteviZaSmestanjeAviona.txt')
#     zahtevi_za_transport_robe = ucitaj_entitet('zahteviZaTransportRobe.txt')
#     avioni_u_hangarima = ucitaj_entitet('avioniUHangarima.txt')
#     avioni_van_hangara = ucitaj_entitet('avioniVanHangara.txt')
#     aerodrom = ucitaj_entitet('aerodrom.txt')



def snimi_sve_entitete():
    """Cuva stanje entiteta u memoriji prilikom izlaska iz aplikacije"""
    snimi_entitet(zahtevi_za_smestanje_aviona, 'zahteviZaSmestanjeAviona.txt')
    snimi_entitet(zahtevi_za_transport_robe, 'zahteviZaTransportRobe.txt')
    snimi_entitet(avioni_u_hangarima, 'avioniUHangarima.txt')
    snimi_entitet(avioni_van_hangara, 'avioniVanHangara.txt')
    snimi_entitet(aerodrom, 'aerodrom.txt')


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


#
# def uzmi_inpute():
#     inputi = []
#     unos = ''
#     while unos != 'q':
#         inputi.append(unos)
#         unos = input('unesite input, q za kraj:')
#
#     inputi = [unos for unos in inputi if unos != '']
#
#     return inputi


def napravi_hangar(naziv, duzina, sirina, visina):
    # u gui-u ce ovo uzimati input
    ID = len(aerodrom) + 1
    # print('unesite Hangar treba nam: naziv, duzinu, sirinu, visinu')
    # l = uzmi_inpute()
    # while len(l) < 4:
    #     print('premalo unesenih inputa')
    #     print('unesite Hangar treba nam: naziv, duzinu, sirinu, visinu')
    #     l = uzmi_inpute()
    hangar = Hangar(ID, naziv, int(duzina), int(sirina), int(visina))
    aerodrom.dodaj(hangar)


def napravi_avion(naziv, duzina, sirina, visina, raspon_krila, godiste, nosivost, relacija):
    ID = len(avioni_u_hangarima) + len(avioni_van_hangara) + 1
    # print('unesite Avion treba nam: naziv,duzinu, sirinu, visinu, raspon_krila, godiste, nosivost, relacija')
    # l = uzmi_inpute()
    # while len(l) < 7:
    #     print('premalo unesenih inputa')
    #     print('unesite Avion treba nam: naziv,duzinu, sirinu, visinu, raspon_krila, godiste, nosivost, relacija')
    #     l = uzmi_inpute()
    avion = Avion(ID, naziv, duzina, sirina, visina, raspon_krila,
                  godiste, nosivost, relacija)
    # pr_za_ter = napravi_prostor_za_robu()
    # while avion < pr_za_ter:
    #     pr_za_ter = napravi_prostor_za_robu()

    avion.extend(temp_prostor_za_robu)
    temp_prostor_za_robu.clear()

    # avion.dodaj(pr_za_ter)
    try:
        smesti_avion(avion)
    except Exception as exc:
        print(exc.args)
        avioni_van_hangara.append(avion)
        for avion in avioni_van_hangara:
            print(avion)


def smesti_avion(avion):
    smestio = False
    for hangar in aerodrom:
        if hangar > avion:
            avion.zahtev_smestanje.hangar = hangar
            avion.zahtev_smestanje.vreme_smestanja_aviona = dt.datetime.now()
            hangar.dodaj(avion)
            avioni_u_hangarima.append(avion)
            avion.se_nalazi = hangar
            smestio = True
            break
    if smestio:
        return
    else:
        return Exception('Avion je prevelik', 'dodajte hangar ili oslobodite mesto', 'avion ce biti van aerodroma')


# ovo treba da bude notifikacija menadzeru hangara


def napravi_prostor_za_robu(naziv, duzina, sirina, visina):
    # print('unesite Prostor Za Teret treba nam: naziv, duzinu, sirinu, visinu')
    # l = uzmi_inpute()
    # while len(l) < 4:
    #     print('premalo unesenih inputa')
    #     print('unesite Prostor Za Teret treba nam: naziv, duzinu, sirinu, visinu')
    #     l = uzmi_inpute()
    pr_za_ter = ProstorZaRobu(naziv, duzina, sirina, visina)
    temp_prostor_za_robu.append(pr_za_ter)


# def dodaj_prostor_za_robu(avion):
#     pzr = napravi_prostor_za_robu()
#     # ovde treba napraviti proveru postojeci prostor + ovaj sto sam napravio, ako moze dodaj, ako ne
#     # sugestiraj dimenzije koje su dozvoljene
#     while pzr > avion:
#         pzr = napravi_prostor_za_robu()
#     avion.dodaj(pzr)


#   bez toga ne moze da se smesti avion
def kreiraj_zahtev_za_smestanje_aviona():
    prikazi_avione_koji_nemaju_zahtev()
    dodaj_zahtev_avionu_van_hangara()


def prikazi_avione_koji_nemaju_zahtev():
    for avion in avioni_van_hangara:
        if avion.zahtev_smestanje is None:
            print(avion)


def dodaj_zahtev_avionu_van_hangara():
    id_aviona = None
    while True:
        try:
            id_aviona = int(input('unesite ID aviona kojem zelite da napravite zahtev za smestanje: '))
            break
        except:
            print('molimo unesite broj')
    for i, avion in enumerate(avioni_van_hangara):
        if avion.id == id_aviona:
            id_zahteva = len(zahtevi_za_smestanje_aviona) + 1
            zahtev = ZahtevZaSmestanjeAviona(id_zahteva, avion, menadzer_hangara)
            zahtevi_za_smestanje_aviona.append(zahtev)
            avion.zahtev_smestanje = zahtev
            break


# samo avoni sa zahtevom mogu da se smeste u hangar
def smesti_avion_koji_ima_zahtev():
    avioni = uzmi_avione_koji_imaju_zahtev_i_mogu_da_udju()
    avion = uzmi_avion_van_hangara(avioni)
    smesti_avion(avion)


def uzmi_avione_koji_imaju_zahtev_i_mogu_da_udju():
    avioni = []
    for avion in avioni_van_hangara:
        if avion.zahtev_smestanje is not None:
            for hangar in aerodrom:
                if avion < hangar:
                    if avion in avioni:
                        continue
                    else:
                        avioni.append(avion)
                        break

    return avioni


def uzmi_avion_van_hangara(avioni):
    for avion in avioni:
        print(avion)
    id_aviona = None
    while True:
        try:
            id_aviona = int(input('unesite ID aviona koji zelite da smestite: '))
            break
        except:
            print('molimo unesite broj')
    for i, avion in enumerate(avioni_van_hangara):
        if avion.id == id_aviona:
            return avioni_van_hangara.pop(i)


def transportuj_robu():
    for zahtev in zahtevi_za_transport_robe['robaUtovarena']:
        for i, avion in enumerate(zahtev.avion.se_nalazi):
            avion_koji_transportuje = zahtev.avion.se_nalazi.pop(i)
            avion.se_nalazi = None
            avion_koji_transportuje.zahtev_smetanja.vreme_napustanja_hangara = dt.datetime.now()
            avion_koji_transportuje.zahtev_smetanja = None
            avion_koji_transportuje.zahtev_transport = None
            avioni_van_hangara.append(avion_koji_transportuje)
            avioni_u_hangarima.remove(avion_koji_transportuje)
            break
    zahtevi_za_transport_robe['robaTransportovana'].extend(zahtevi_za_transport_robe['robaUtovarena'])
    zahtevi_za_transport_robe['robaUtovarena'].clear()




# h1 = Hangar(1, 'HANG1', 100, 100, 30)
# #
# # h2 = Hangar(2, 'hang007', 100, 100, 300)
# #
# aerodrom.dodaj(h1)
# # aerodrom.dodaj(h2)
# a1 = Avion(1, 'Av1', 20, 10, 10, 20, 2012, 10, 'Pariz')
# a2 = Avion(2, 'Av2', 22, 20, 10, 30, 2011, 30, 'London')
# a3 = Avion(3, 'Av3', 23, 20, 10, 50, 2014, 20, 'London')
# a4 = Avion(4, 'Av4', 25, 20, 10, 40, 2005, 40, 'London')
#
# # a3 = Avion(3, 'Av3', 24, 10, 10, 30, 2005, 20, 'lisabon')
# # a4 = Avion(4, 'Av4', 25, 15, 8, 1500, 2006, 22, 'kijev')
# # a5 = Avion(5, 'Av5', 500, 500, 5, 10, 2008, 32, 'moskva')
# # a6 = Avion(6, 'Av6', 5, 5, 5, 2000, 2015, 42, 'kopenhagen')
# #
#
# p1 = ProstorZaRobu("p1",10,10,10)
# p2 = ProstorZaRobu("p1",20,20,20)
# a1.dodaj(p1)
# a1.dodaj(p2)
#
# p3 = ProstorZaRobu("p2",12,15,8)
# a2.dodaj(p3)
#
# # h1.dodaj(a1)
# # h1.dodaj(a2)
#
# avioni_u_hangarima.append(a1)
# avioni_u_hangarima.append(a2)
# avioni_u_hangarima.append(a3)
# avioni_u_hangarima.append(a4)


# avioni_van_hangara.append(a1)
# avioni_van_hangara.append(a2)
# avioni_van_hangara.append(a3)
# avioni_van_hangara.append(a4)
# avioni_van_hangara.append(a5)
# avioni_van_hangara.append(a6)
#
# print(aerodrom, h1, h2, menadzer_hangara, len(aerodrom), sep='\n')
#
# for i, avion in enumerate(avioni_van_hangara):
#     print(i, avion.zahtev_smestanje)
#
# kreiraj_zahtev_za_smestanje_aviona()
#
# for i, avion in enumerate(avioni_van_hangara):
#     print(i, avion.zahtev_smestanje)
#
# kreiraj_zahtev_za_smestanje_aviona()
#
# for i, avion in enumerate(avioni_van_hangara):
#     print(i, avion.zahtev_smestanje)
#
# # print(avioni_u_hangarima[0].zahtev.menadzer.id)
#
# for avion in avioni_van_hangara:
#     print(avion)
#
# print('--------------')
#
# smesti_avion_koji_ima_zahtev()
#
# for avion in avioni_van_hangara:
#     print(avion)
#
# print('****************')
# for avion in avioni_u_hangarima:
#     print(avion)


# men transporta...

# def ucitajZahteveIRobu():
#     zahteviLines = util.readFile("zahteviZaTransport.txt")
#     robaLines = util.readFile("roba.txt")
#
#     for linija in zahteviLines:
#         z = linija.strip().split("|")
#         zahtev = klase.zahtevi.ZahtevZaTransport(z[3],z[4],z[0],z[2],z[6])
#
#         for rlinija in robaLines:
#             r = rlinija.strip().split("|")
#             if r[7] == z[0]:
#                 robaa = klase.roba.Roba(r[1],r[2],int(r[3]),int(r[4]),int(r[5]),int(r[5]),r[7],r[0])
#                 zahtev.roba.append(robaa)
#
#         zahtevi_za_transport_robe[zahtev.statusZahteva].append(zahtev)
#
#     for znj in zahtevi_za_transport_robe['kreiran']: # ovo je samo za test, mos brisati kasnije..
#         print(znj)



from klase.entiteti import Avion, Hangar, ProstorZaRobu, Aerodrom
from klase.util_funk import snimi_entitet, ucitaj_entitet, set_path, readFile, addToFile, proveraInputa, \
    proveraInputaBroj
from klase.zahtevi import ZahtevZaSmestanjeAviona
import datetime as dt

# zahtevi_za_smestanje_aviona = []
# zahtevi_za_transport_robe = {'kreiran': [], 'odobren': [], 'robaUtovarena': [], 'robaTransportovana': []}
# avioni_u_hangarima = []
# avioni_van_hangara = []  # deque
# aerodrom = Aerodrom('Nikola Tesla', 'Futoski Put', 'Novi Sad')
# #menadzer_hangara = MenadzerHangara(1, 'Lepan', 'Lepavi', 'lepi', 12345)  # PROBA MEN HANGARA TREBA DA JE ULOGOVAN
# temp_prostor_za_robu = []

zahtevi_za_smestanje_aviona = None
zahtevi_za_transport_robe = None
avioni_u_hangarima = None
avioni_van_hangara = None
aerodrom = None
temp_prostor_za_robu = []


def ucitaj_sve_entitete():
    """Ucitava sve globalne entitete u memoriju iz jednog pickle fajla koji cuva sve entitete u jednom tuple-u"""
    globalni_entiteti = ucitaj_entitet('globalni_entiteti.txt')
    global zahtevi_za_smestanje_aviona, zahtevi_za_transport_robe, avioni_u_hangarima, avioni_van_hangara, aerodrom
    zahtevi_za_smestanje_aviona = globalni_entiteti[0]
    zahtevi_za_transport_robe = globalni_entiteti[1]
    avioni_u_hangarima = globalni_entiteti[2]
    avioni_van_hangara = globalni_entiteti[3]
    aerodrom = globalni_entiteti[4]


def snimi_sve_entitete(application):
    """Cuva stanje entiteta u memoriji prilikom izlaska iz aplikacije kao jedan tuple u pickle fajlu"""
    globalni_entiteti = (zahtevi_za_smestanje_aviona, zahtevi_za_transport_robe,
                         avioni_u_hangarima, avioni_van_hangara, aerodrom)
    snimi_entitet(globalni_entiteti, 'globalni_entiteti.txt')
    application.destroy()


def prikazi_zahteve_za_smestanje_aviona():
    """Vraca listu svih zahteva za smestanje aviona u hangar"""
    prikaz = []
    for zahtev in zahtevi_za_smestanje_aviona:
        prikaz.append(zahtev)
    return prikaz


def prikaz_zahteva_za_transport_utovarene_robe():
    """Vraca listu svih zahteva za transport robe ciji je status roba utovarena(robaUtovarena)"""
    prikaz = []
    for zahtev in zahtevi_za_transport_robe['robaUtovarena']:
        prikaz.append(zahtev)
    return prikaz


def proveri_inpute_hangar(naziv, duzina, sirina, visina):
    """Vraca True ako su svi unosi koje je korisnik uneo validni(nazivi su string, dimenzije int ...)"""
    if proveraInputa(naziv) and proveraInputaBroj(duzina) and \
            proveraInputaBroj(sirina) and proveraInputaBroj(visina):
        return True


def napravi_hangar(naziv, duzina, sirina, visina):
    """Pravi objekat hangara i ubacije ga u aerodrom"""
    ID = len(aerodrom) + 1
    hangar = Hangar(ID, naziv, int(duzina), int(sirina), int(visina))
    aerodrom.dodaj(hangar)


def proveri_inpute_avion(naziv, duzina, sirina, visina, raspon_krila, godiste, nosivost, relacija):
    """Vraca True ako su svi unosi koje je korisnik uneo validni(nazivi su string, dimenzije int ...)"""
    if proveraInputa(naziv) and proveraInputaBroj(duzina) and proveraInputaBroj(sirina) \
        and proveraInputaBroj(visina) and proveraInputa(raspon_krila) and proveraInputa(godiste) \
            and proveraInputa(nosivost) and proveraInputa(relacija):
        return True


def napravi_avion(naziv, duzina, sirina, visina, raspon_krila, godiste, nosivost, relacija):
    """Pravi objekat aviona, dodaje mu kreirane prostore za teret i ubacuje ga u avione van hangara
    (globalni objekat svih aviona koji nisu u aerodromu)"""
    ID = len(avioni_u_hangarima) + len(avioni_van_hangara) + 1
    avion = Avion(ID, naziv, duzina, sirina, visina, raspon_krila,
                  godiste, nosivost, relacija)
    avion.extend(temp_prostor_za_robu)
    temp_prostor_za_robu.clear()
    avioni_van_hangara.append(avion)


def smesti_avion(avion):
    """Smesta objekat aviona (koji je poslat kao argument) u hangar i postavlja vreme smestanja u hangar
        u zahtevu za smestanje aviona"""
    smestio = False
    for hangar in aerodrom:
        if hangar > avion:
            avion.zahtev_smestanje.hangar = hangar
            avion.zahtev_smestanje.vreme_smestanja_aviona = dt.datetime.now()
            hangar.dodaj(avion)
            avioni_u_hangarima.append(avion)
            avion.se_nalazi = hangar
            smestio = True
        if smestio:
            return smestio


def dodaj_odrediste(relacija):
    """Odrediste se dodaje kada relacija (koja se salje kao argument) ne postoji u fajlu odredista. Izvrsava
        se kada menadzer hangara dodaje avion."""
    path = set_path('odredista.txt')
    odredista = readFile(path)
    relacija += '\n'
    if relacija not in odredista:
        addToFile(path, relacija)


def proveri_inpute_prostor_za_robu(naziv, duzina, sirina, visina):
    if proveraInputa(naziv) and proveraInputaBroj(duzina) and \
         proveraInputaBroj(sirina) and proveraInputaBroj(visina):
        return True


def napravi_prostor_za_robu(naziv, duzina, sirina, visina):
    """Pravi prostor za robu(koji ce se dodati avionu)"""
    pr_za_ter = ProstorZaRobu(naziv, duzina, sirina, visina)
    temp_prostor_za_robu.append(pr_za_ter)


def napravi_zahtev_za_smestanje(odabran_avion, menadzer):
    """Pravi zahtev za smestanje za avion koji je poslat kao argument"""
    id_zahteva = len(zahtevi_za_smestanje_aviona) + 1
    zahtev = ZahtevZaSmestanjeAviona(id_zahteva, odabran_avion, menadzer)
    zahtevi_za_smestanje_aviona.append(zahtev)
    odabran_avion.zahtev_smestanje = zahtev


def transportuj_robu(odabran_avion):
    """Transportuje robu iz odabranog aviona (koji se salje kao argument), salje ga van aerodroma"""
    avioni_van_hangara.append(odabran_avion)
    avioni_u_hangarima.remove(odabran_avion)
    odabran_avion.se_nalazi.ukloni(odabran_avion)
    odabran_avion.se_nalazi = None
    odabran_avion.zahtev_smestanje.vreme_napustanja_hangara = dt.datetime.now()
    odabran_avion.zahtev_smestanje = None
    for zahtev in odabran_avion.zahtev_transport:
        zahtev.statusZahteva = 'robaTransportovana'
        zahtevi_za_transport_robe['robaTransportovana'].append(zahtev)
        zahtevi_za_transport_robe['robaUtovarena'].remove(zahtev)
        zahtev.datumTransporta = dt.datetime.now()
        for roba in zahtev.roba:
            for prostor in odabran_avion:
                if roba in prostor:
                    prostor.ukloni(roba)
                    odabran_avion.nosivost += roba.tezina
                    break
    odabran_avion.zahtev_transport.clear()


def prikazi_zahteve_za_transport_odobrene_robe():
    """Vraca listu zahteva ciji je status odobren"""
    prikaz = []
    for zahtev in zahtevi_za_transport_robe['odobren']:
        prikaz.append(zahtev)
    return prikaz


def utovari_robu(zahtev):
    """Utovara robu iz zahteva (koji je prosledjen kao parametar) i menja njegov status"""
    zahtev.statusZahteva = 'robaUtovarena'
    for i, zah in enumerate(zahtevi_za_transport_robe['odobren']):
        if zah == zahtev:
            zahtevi_za_transport_robe['robaUtovarena'].append(zahtevi_za_transport_robe['odobren'].pop(i))
            break

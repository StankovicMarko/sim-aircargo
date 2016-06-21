import os
import sys
import datetime
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from klase import aplikacija
from klase.entiteti import Avion
from klase.korisnici import MenadzerHangara
from klase.aplikacija import napravi_zahtev_za_smestanje


def test_prikaz_zahtevi_smestanje():
    aplikacija.ucitaj_sve_entitete()
    zahtevi_za_smestanje = aplikacija.prikazi_zahteve_za_smestanje_aviona()
    assert isinstance(zahtevi_za_smestanje, list)


def test_zahtev_smestanje():
    aplikacija.ucitaj_sve_entitete()
    broj_zahteva_pre = len(aplikacija.zahtevi_za_smestanje_aviona)
    menadzer = MenadzerHangara(1, 'Petar', 'Peric', 'perica')
    avion = Avion(1, 'avion1', 30, 10, 10, 30, 2012, 8000, 'Pariz')
    napravi_zahtev_za_smestanje(avion, menadzer)
    broj_zahteva_posle = len(aplikacija.zahtevi_za_smestanje_aviona)

    assert broj_zahteva_pre < broj_zahteva_posle
    assert broj_zahteva_pre == broj_zahteva_posle - 1
    assert isinstance(aplikacija.zahtevi_za_smestanje_aviona[broj_zahteva_posle-1].vremeKreiranja, datetime.datetime)
    assert aplikacija.zahtevi_za_smestanje_aviona[broj_zahteva_posle-1].avion.id == 1
    assert aplikacija.zahtevi_za_smestanje_aviona[broj_zahteva_posle-1].menadzer.naziv == 'Petar'

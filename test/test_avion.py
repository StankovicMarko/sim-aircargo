import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from klase.aplikacija import napravi_zahtev_za_smestanje, smesti_avion, napravi_avion
from klase.entiteti import Avion, Hangar
from klase import aplikacija
from klase.korisnici import MenadzerHangara


def test_dodaj_avion():
    aplikacija.ucitaj_sve_entitete()
    hangar_sirina=100
    hangar = Hangar(1, 'hang001', 100, hangar_sirina, 30)
    aplikacija.aerodrom.dodaj(hangar)
    avion = Avion(1, 'avion1', 30, 10, 10, 30, 2012, 8000, 'Pariz')
    menadzer = MenadzerHangara(1, 'Petar', 'Peric', 'perica')
    napravi_zahtev_za_smestanje(avion, menadzer)
    broj_aviona_u_hangarima = len(aplikacija.avioni_u_hangarima)
    smesti_avion(avion)
    broj_aviona_u_hangarima_posle = len(aplikacija.avioni_u_hangarima)
    assert broj_aviona_u_hangarima != broj_aviona_u_hangarima_posle
    assert broj_aviona_u_hangarima == broj_aviona_u_hangarima_posle - 1
    assert aplikacija.avioni_u_hangarima[broj_aviona_u_hangarima_posle-1].id == 1
    assert aplikacija.avioni_u_hangarima[broj_aviona_u_hangarima_posle-1].zahtev_smestanje is not None
    #assert hangar.sirina < hangar_sirina
    #assert hangar.sirina + 30 == hangar_sirina


def test_dodaj_avion_none():
    with pytest.raises(AttributeError):
        smesti_avion(None)


def test_dodaj_avion_string():
    with pytest.raises(AttributeError):
        smesti_avion("test")


def test_napravi_avion_none():
    with pytest.raises(TypeError):
        aplikacija.proveri_inpute_avion(None, None, None, None, None, None, None, None)



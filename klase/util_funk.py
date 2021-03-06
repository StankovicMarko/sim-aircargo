from datetime import datetime
import os
import pickle


def set_path(file_name):
    """Postavlja apsolutnu putanju do """
    fullPath = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(fullPath, "..", "files", file_name)
    return path


def readFile(filename):
    """
    Citanje fajla
    """
    path = set_path(filename)
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines


def addToFile(filename, string):
    """
    Dodavanje u fajl
    """
    path = set_path(filename)
    with open(path, 'a') as f:
        f.write(string)


def sortPoDatumuKreiranja(lista):
    """
    Koristi se za sortiranje zahteva za transport po datumu kreiranja
    """
    return sorted(lista, key=lambda x: datetime.strptime(x[1], "%d/%m/%Y"))


def sortPoDatumuRealizacije(lista):
    """
    Koristi se za sortiranje zahteva za transport po datumu realizacije
    """
    try:
        return sorted(lista, key=lambda x: datetime.strptime(x[2], "%d/%m/%Y"))
    except:
        return sorted(lista, key=lambda x: x[2])


def sortPoStatusu(lista):
    """
    Sortiranje zahteva za transport po statusu
    """
    return sorted(lista, key=lambda x: x[6])


def proveraInputa(string):
    """
    Proverava se da li input sadrzi zabranjeni karakter
    """
    bannedChars = ["`", "~", "!", "#", "$", "%", "^", "&",
                   "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", "'", "|", "\\", "/", "?", "<", ">", ",",
                   ":", ";", '"']

    for i in string:
        if i in bannedChars:
            return False
    return True


def proveraInputaBroj(broj):
    """
    Provera da li je input broj
    """
    try:
        broj = int(broj)
        if broj <= 0:
            return False
        return True
    except:
        return False


def ucitaj_entitet(file_name):
    """Ucitava iz datog fajla podatke koristeci pickle modul"""
    path = set_path(file_name)
    with open(path, 'rb') as f:
        return pickle.load(f)


def snimi_entitet(data, file_name):
    """Cuva data argument koristeci pickle modul sa HIGHEST_PROTOCOL-om u fajl pod imenom file_name"""
    path = set_path(file_name)
    with open(path, 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)


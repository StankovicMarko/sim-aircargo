from datetime import datetime
import os

def readFile(filename):
    fullPath = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(fullPath,"..","files",filename)

    f = open(path,"r")
    lines = f.readlines()
    f.close()
    return lines

def saveFile(filename,string):
    fullPath = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(fullPath,"..","files",filename)
    
    f = open(path,"a")
    f.write(string)
    f.close()


def sortPoDatumuKreiranja(lista):
	'''
	Koristi se za sortiranje zahteva za transport po datumu kreiranja
	'''
	return sorted(lista,key=lambda x: datetime.strptime(x[1],"%d/%m/%Y"))


def sortPoDatumuRealizacije(lista):
	'''
	Koristi se za sortiranje zahteva za transport po datumu realizacije
	'''
	try:
		return sorted(lista,key=lambda x: datetime.strptime(x[2],"%d/%m/%Y"))
	except:
		return sorted(lista,key=lambda x:x[2])

def sortPoStatusu(lista):
	'''
	Sortiranje zahteva za transport po statusu
	'''
	return sorted(lista,key=lambda x: x[6])
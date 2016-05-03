from datetime import datetime

class Zahtev(object):
	def __init__(self):
		self.IDZahteva = self.odrediIDZahteva()
		self.datumKreiranja = self.odrediDatum()


	def __readFile(self):
		filename = "files/zahteviZaTransport.txt"
		f = open(filename,"r")
		lines = f.readlines()
		f.close()
		return lines

	def odrediDatum(self):
		return datetime.now().strftime("%d/%m/%Y")

	def odrediIDZahteva(self):
		lines = self.__readFile()
		l = lines[-1].split("|")
		return str(int(l[0])+1)
		


class ZahtevZaTransport(Zahtev):
	def __init__(self,odrediste,IDPotrazitelja):
		Zahtev.__init__(self)
		self.datumTransporta = None
		self.odrediste = odrediste
		self.IDPotrazitelja = IDPotrazitelja
		self.oznakaAviona = None
		self.statusZahteva = "kreiran"


class ZahtevZaSmestanjeAviona(Zahtev):
	def __init__(self,vremeSmestanjaUHangar,vremeNapustanjaHangara,oznakaHangara,oznakaAviona,IDMenadzeraHangara):
		Zahtev.__init__(self,oznakaAviona)
		self.vremeSmestanjaUHangar = vremeSmestanjaUHangar
		self.vremeNapustanjaHangara = vremeNapustanjaHangara
		self.oznakaHangara = oznakaHangara
		self.IDMenadzeraHangara = IDMenadzeraHangara
		
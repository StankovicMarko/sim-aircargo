from datetime import datetime
import klase.util_klase as util

class Zahtev(object):
	def __init__(self):
		self.IDZahteva = self.odrediIDZahteva()
		self.datumKreiranja = self.odrediDatum()

	def odrediDatum(self):
		return datetime.now().strftime("%d/%m/%Y")

	def odrediIDZahteva(self):
		lines = util.readFile("files/zahteviZaTransport.txt")
		l = lines[-1].split("|")
		return str(int(l[0])+1)
		


class ZahtevZaTransport(Zahtev):
	def __init__(self,odrediste,IDPotrazitelja):
		Zahtev.__init__(self)
		self.datumTransporta = "None"
		self.odrediste = odrediste
		self.IDPotrazitelja = IDPotrazitelja
		self.oznakaAviona = "None"
		self.statusZahteva = "kreiran"
		util.saveFile("files/zahteviZaTransport.txt",self.IDZahteva+"|"+self.datumKreiranja+"|"+self.datumTransporta+
			"|"+self.odrediste+"|"+self.IDPotrazitelja+"|"+self.oznakaAviona+"|"+self.statusZahteva+"\n")

	# def sacuvajZahtev(self):
	# 	filename = "files/zahteviZaTransport.txt"
	# 	f = open(filename,"a")
	# 	f.write(self.IDZahteva+"|"+self.datumKreiranja+"|"+self.datumTransporta+"|"+self.odrediste+"|"
	# 		+self.IDPotrazitelja+"|"+self.oznakaAviona+"|"+self.statusZahteva+"\n")
	# 	f.close()


class ZahtevZaSmestanjeAviona(Zahtev):
	def __init__(self,vremeSmestanjaUHangar,vremeNapustanjaHangara,oznakaHangara,oznakaAviona,IDMenadzeraHangara):
		Zahtev.__init__(self,oznakaAviona)
		self.vremeSmestanjaUHangar = vremeSmestanjaUHangar
		self.vremeNapustanjaHangara = vremeNapustanjaHangara
		self.oznakaHangara = oznakaHangara
		self.IDMenadzeraHangara = IDMenadzeraHangara
		
import klase.util_klase as util

class Roba(object):
	def __init__(self,naziv,opis,duzina,sirina,visina,tezina,IDPotrazitelja):
		self.oznaka = self.odrediIDRobe()
		self.naziv = naziv
		self.opis = opis
		self.duzina = duzina
		self.sirina = sirina
		self.visina = visina
		self.tezina = tezina
		self.IDPotrazitelja = IDPotrazitelja

		util.saveFile("files/roba.txt",self.oznaka+"|"+self.naziv+"|"+self.opis+"|"+
			self.duzina+"|"+self.sirina+"|"+self.visina+"|"+self.tezina+"|"+self.IDPotrazitelja+"\n")
		

	def odrediIDRobe(self):
		lines = util.readFile("files/roba.txt")
		lastLine = lines[-1].split("|")
		l = lastLine[0].split("#")
		return "R#"+str(int(l[1])+1)
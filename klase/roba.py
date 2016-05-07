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

		self.sacuvajRobu(self.oznaka+"|"+self.naziv+"|"+self.opis+"|"+
			self.duzina+"|"+self.sirina+"|"+self.visina+"|"+self.tezina+"|"+self.IDPotrazitelja+"\n")
		

	def odrediIDRobe(self):
		lines = self.readFile()
		l = lines[-1].split("|")
		return str(int(l[0])+1)

	def readFile(self):
		filename = "files/roba.txt"
		f = open(filename,"r")
		lines = f.readlines()
		f.close()
		return lines

	def sacuvajRobu(self,string):
		filename = "files/roba.txt"
		f = open(filename,"a")
		f.write(string)
		f.close()
import klase.util_klase as util

class User(object):

	def __init__(self,ID,ime,prezime):
		self.ID = ID
		self.ime = ime
		self.prezime = prezime


	def prikazZahteva(self,sve=False):
		'''
		Vraca zahteve za transport, ako je parametar "sve"=True
		vraca sve zahteve, ako je False, vraca samo od ulogovanog potrazitelja
		'''
		zahtevi = []
		lines = util.readFile("files/zahteviZaTransport.txt")
		for line in lines:
			l = line.strip().split("|")
			if sve == True:
				zahtevi.append(l)
			else:
				if l[4] == self.ID:
					zahtevi.append(l)
		return zahtevi


class Potrazitelj(User):
	def __init__(self,ID,ime,prezime,brojTelefona,email):
		User.__init__(self,ID,ime,prezime)
		self.ID = ID
		self.ime = ime
		self.prezime = prezime
		self.brojTelefona = brojTelefona
		self.email = email



class ManagerTransport(User):
		def __init__(self,ID,ime,prezime,username,password):
			User.__init__(self,ID,ime,prezime)
			self.username = username
			self.password = password
			
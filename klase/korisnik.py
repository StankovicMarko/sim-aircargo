import klase.util_klase as util

class User(object):

	def __init__(self,ID,ime,prezime):
		self.ID = ID
		self.ime = ime
		self.prezime = prezime

	'''
	Prikazuje zahteve za transport, ako je parametar "sve"=True
	prikazuje sve zahteve, ako je False, prikaz samo od ulogovanog potrazitelja
	'''
	def prikazZahteva(self,sve=False):
		lines = util.readFile("files/zahteviZaTransport.txt")
		for line in lines:
			l = line.strip().split("|")
			if sve == True:
				print(l)
			else:
				if l[4] == self.ID:
					print(l)


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
			
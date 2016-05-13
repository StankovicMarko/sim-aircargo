import klase.util_klase as util

class User(object):

	def __init__(self,ID,ime,prezime):
		self.ID = ID
		self.ime = ime
		self.prezime = prezime
	


class Potrazitelj(User):
	def __init__(self,ID,ime,prezime,brojTelefona,email):
		User.__init__(self,ID,ime,prezime)
		self.ID = ID
		self.ime = ime
		self.prezime = prezime
		self.brojTelefona = brojTelefona
		self.email = email


	def prikazZahteva(self):
		lines = util.readFile("files/zahteviZaTransport.txt")
		for line in lines:
			l = line.strip().split("|")
			if l[4] == self.ID:
				print(l)

class ManagerTransport(User):
		def __init__(self,ID,ime,prezime,username,password):
			User.__init__(self,ID,ime,prezime)
			self.username = username
			self.password = password
			
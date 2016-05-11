class User(object):

	def __init__(self,ID,ime,prezime):
		self.ID = ID
		self.ime = ime
		self.prezime = prezime
	


class Potrazitelj(User):
	def __init__(self,brojTelefona,email):
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
			
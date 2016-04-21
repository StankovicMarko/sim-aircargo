class Aerodrom(object):

	def __init__(self):
		self.naziv = "Nikola Tesla"
		self.adresa = "Aerodrom Nikola Tesla bb "
		self.mesto = "Beograd"
		self.hangari = []



class Hangar(object):

	def __init__(self,oznaka,naziv,duzina,sirina,visina):
		self.oznaka = oznaka
		self.naziv = naziv
		self.duzina = duzina
		self.sirina = sirina
		self.visina = visina



class Avion(object):

	def __init__(self, oznaka,naziv,godiste,duzina,raspon_krila,visina,ukupna_nosivost,relacija):
		self.oznaka = oznaka
		self.naziv = naziv
		self.godiste = godiste
		self.duzina = duzina
		self.raspon_krila = raspon_krila
		self.visina = visina
		self.ukupna_nosivost = ukupna_nosivost
		self.relacija = relacija



class TeretniProstor(object):
	def __init__(self, naziv,duzina,sirina,visina):
		self.naziv = naziv
		self.duzina = duzina
		self.sirina = sirina
		self.visina = visina
		


class Roba(object):
	def __init__(self, oznaka,naziv,opis,duzina,sirina,visina):
		self.oznaka = oznaka
		self.naziv = naziv
		self.opis = opis
		self.duzina = duzina
		self.sirina = sirina
		self.visina = visina
		
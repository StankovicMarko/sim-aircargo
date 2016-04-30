class Zahtev(object):
	def __init__(self, IDZahteva,datumKreiranja,oznakaAviona):
		super(Zahtev, self).__init__()
		self.IDZahteva = IDZahteva
		self.datumKreiranja = datumKreiranja
		self.oznakaAviona = oznakaAviona
		


class ZahtevZaTransport(Zahtev):
	def __init__(self, IDZahteva,datumKreiranja,datumTransporta,odrediste,IDPotrazitelja,oznakaAviona,statusZahteva):
		Zahtev.__init__(self,IDZahteva,datumKreiranja,oznakaAviona)
		self.datumTransporta = datumTransporta
		self.odrediste = odrediste
		self.IDPotrazitelja = IDPotrazitelja
		self.statusZahteva = statusZahteva
		

class ZahtevZaSmestanjeAviona(Zahtev):
	def __init__(self,IDZahteva,datumKreiranja,vremeSmestanjaUHangar,vremeNapustanjaHangara,oznakaHangara,oznakaAviona,IDMenadzeraHangara):
		Zahtev.__init__(self,IDZahteva,datumKreiranja,oznakaAviona)
		self.vremeSmestanjaUHangar = vremeSmestanjaUHangar
		self.vremeNapustanjaHangara = vremeNapustanjaHangara
		self.oznakaHangara = oznakaHangara
		self.IDMenadzeraHangara = IDMenadzeraHangara
		
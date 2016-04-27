from klase.login import *
from klase.korisnik import *

def main():
	
	korisnik = Login("admin","admin")
	if korisnik.username == None:
		print("Pogresan username/password!")
	else:
		print("Dobro dosao",korisnik.username,"\nUlogovani ste kao",korisnik.uloga)


if __name__ == "__main__":
	main()
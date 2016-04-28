from klase.login import *
from klase.korisnik import *
from GUI.LoginWindow import *

def main():

	root = tk.Tk()
	application = LoginWindow(root)
	application.mainloop()

if __name__ == "__main__":
	main()
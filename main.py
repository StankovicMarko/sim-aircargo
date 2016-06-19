from klase import aplikacija
from gui.windows import Glavna
if __name__ == "__main__":
    aplikacija.ucitaj_sve_entitete()
    application = Glavna()
    application.protocol('WM_DELETE_WINDOW', lambda: aplikacija.snimi_sve_entitete(application))
    application.mainloop()



import klase.util_funk as util

class Login(object):

    def __init__(self,username,password):
        self.ID, self.username, self.ime, self.prezime, self.uloga = self.__checkCreds(username,password)

    def __checkCreds(self,username,password):
        lines = util.readFile("korisnici.txt")
        for line in lines:
            l = line.strip().split("|")
            ID = l[0]
            ime = l[1]
            prezime = l[2]
            uloga = l[5]

            if username == l[3] and password == l[4]:
                return ID, username, ime, prezime, uloga
            else:
                x = 1

        if x != 0:
            return None,None,None,None,None

    def checkID(self,ID):
        lines = util.readFile("korisnici.txt")
        for line in lines:
            l = line.strip().split("|")

            if ID == l[0] and l[5] == "potrazitelj":
                return True,l

        return False,None



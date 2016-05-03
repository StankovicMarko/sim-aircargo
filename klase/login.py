class Login(object):

    def __init__(self,username,password):
        self.ID, self.username, self.imePrezime, self.uloga = self.__checkCreds(username,password)

    def readFile(self):
        fileName = "files/korisnici.txt"
        f = open(fileName,"r")
        lines = f.readlines()
        f.close()
        return lines

    def __checkCreds(self,username,password):
        lines = self.readFile()
        for line in lines:
            l = line.strip().split("|")
            ID = l[0]
            imePrezime = l[1]
            uloga = l[4]

            if username == l[2] and password == l[3]:
                return ID, username, imePrezime, uloga
            else:
                x = 1

        if x != 0:
            return None,None,None,None

    def checkID(self,ID):
        print("hello from klasa LOGIN!")
        lines = self.readFile()
        for line in lines:
            l = line.strip().split("|")

            if ID == l[0] and l[4] == "potrazitelj":
                return True

        return False



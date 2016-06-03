import klase.util_funk as util

class Roba(object):
    def __init__(self,naziv,opis,duzina,sirina,visina,tezina,IDZahteva):
        self.oznaka = self.odrediIDRobe()
        self.naziv = naziv
        self.opis = opis
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina
        self.tezina = tezina
        self.IDZahteva = IDZahteva

        # util.saveFile("roba.txt",self.oznaka+"|"+self.naziv+"|"+self.opis+"|"+
        #     self.duzina+"|"+self.sirina+"|"+self.visina+"|"+self.tezina+"|"+self.IDZahteva+"\n")


    def odrediIDRobe(self):
        lines = util.readFile("roba.txt")
        lastLine = lines[-1].split("|")
        l = lastLine[0].split("#")
        return "R#"+str(int(l[1])+1)
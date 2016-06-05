import klase.util_funk as util

class Roba(object):
    def __init__(self,naziv,opis,duzina,sirina,visina,tezina,IDZahteva,oznaka=None):
        if oznaka == None:
            self.oznaka = self.odrediIDRobe()
        else:
            self.oznaka = oznaka
        self.naziv = naziv
        self.opis = opis
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina
        self.tezina = tezina
        self.IDZahteva = IDZahteva

    def sacuvaj(self):
        util.saveFile("roba.txt",self.oznaka+"|"+self.naziv+"|"+self.opis+"|"+
            self.duzina+"|"+self.sirina+"|"+self.visina+"|"+self.tezina+"|"+self.IDZahteva+"\n")


    def odrediIDRobe(self):
        lines = util.readFile("roba.txt")
        lastLine = lines[-1].split("|")
        l = lastLine[0].split("#")
        return "R#"+str(int(l[1])+1)

    def __str__(self):
        return "Roba - {}, Naziv {}, Opis - {}, Duzina:{},Sirina:{},Visina:{},Tezina:{}".format(self.oznaka,self.naziv,self.opis,self.duzina,self.sirina,self.visina,self.tezina)
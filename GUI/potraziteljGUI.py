import tkinter as tk
from tkinter import messagebox
from klase.login import *
from klase.zahtevi import *
import klase.korisnik
import klase.roba
import klase.util_klase as util

class PotraziteljPanel(tk.Frame):
    def __init__(self,parent,controler):
        tk.Frame.__init__(self,parent)
        self.controler = controler
        self.proveriIDFrameWidgets()
        self.podaciFrameWidgets()
        self.dodajRobuFrameWidgets()
        self.odredisteFrameWidgets()
        self.podnesiZahtevButtonFrameWidgets()

    def proveriIDFrameWidgets(self):
        self.checkIDFrame = tk.Frame(self)
        self.checkIDFrame.grid(row=0,column=0,sticky="nw")
        self.IDLabel = tk.Label(self.checkIDFrame,text="Unesite ID:")
        self.IDInput = tk.Entry(self.checkIDFrame)
        self.ProveriIDButton = tk.Button(self.checkIDFrame,text="Proveri",command=self.proveriID)
        self.CheckBoxNemamIDState = tk.IntVar()
        self.CheckBoxNemamID = tk.Checkbutton(self.checkIDFrame,text="Nemam ID",command=self.disableIDInput,variable=self.CheckBoxNemamIDState)
        self.IDLabel.grid(row=0,column=0)
        self.IDInput.grid(row=1,column=0)
        self.ProveriIDButton.grid(row=1,column=2)
        self.CheckBoxNemamID.grid(row=2,columnspan=2)

    def podaciFrameWidgets(self):
        self.PodaciFrame = tk.Frame(self)
        self.PodaciFrame.grid(row=0,column=0)
        self.ImeLabel = tk.Label(self.PodaciFrame,text="Ime:")
        self.ImeInput = tk.Entry(self.PodaciFrame,state="disabled")
        self.PrezimeLabel = tk.Label(self.PodaciFrame,text="Prezime:")
        self.PrezimeInput = tk.Entry(self.PodaciFrame,state="disabled")
        self.BrojTelefonaLabel = tk.Label(self.PodaciFrame,text="Broj Telefona:")
        self.BrojTelefonaInput = tk.Entry(self.PodaciFrame,state="disabled")
        self.EmailLabel = tk.Label(self.PodaciFrame,text="Email:")
        self.EmailInput = tk.Entry(self.PodaciFrame,state="disabled")

        self.ImeLabel.grid(row=3,column=0)
        self.ImeInput.grid(row=3,column=1)
        self.PrezimeLabel.grid(row=4,column=0)
        self.PrezimeInput.grid(row=4,column=1)
        self.BrojTelefonaLabel.grid(row=5,column=0)
        self.BrojTelefonaInput.grid(row=5,column=1)
        self.EmailLabel.grid(row=6,column=0)
        self.EmailInput.grid(row=6,column=1)


    def podnesiZahtevButtonFrameWidgets(self):
        self.PodnesiZahtevButtonFrame = tk.Frame(self)
        self.PodnesiZahtevButtonFrame.grid(row=3,columnspan=10)
        self.PodnesiZahtevButton = tk.Button(self.PodnesiZahtevButtonFrame,state="disabled",text="Podnesi Zahtev",height=2,width=10,command=self.podnesiZahtev)
        self.PrikazIstorijuButton = tk.Button(self.PodnesiZahtevButtonFrame,state="disabled",text="Prikaz Istorije",height=2,width=10,command=self.prikaziIstoriju)        
        self.PodnesiZahtevButton.grid(row=0,column=0)
        self.PrikazIstorijuButton.grid(row=0,column=1)


    def dodajRobuFrameWidgets(self):
        self.DodajRobuFrame = tk.Frame(self)
        self.DodajRobuFrame.grid(row=0,column=3)

        self.robaLabel = tk.Label(self.DodajRobuFrame,text="Roba:")
        self.opisRobaLabel = tk.Label(self.DodajRobuFrame,text="Opis:")
        self.robaInput = tk.Entry(self.DodajRobuFrame,width=15)
        self.opisRobeInput = tk.Entry(self.DodajRobuFrame,width=15)

        self.duzinaRobeLabel = tk.Label(self.DodajRobuFrame,text="Duzina:")
        self.duzinaRobeInput = tk.Entry(self.DodajRobuFrame,width=5)
        self.sirinaRobeLabel = tk.Label(self.DodajRobuFrame,text="Sirina:")
        self.sirinaRobeInput = tk.Entry(self.DodajRobuFrame,width=5)
        self.visinaRobeLabel = tk.Label(self.DodajRobuFrame,text="Visina:")
        self.visinaRobeInput = tk.Entry(self.DodajRobuFrame,width=5)
        self.tezinaRobeLabel = tk.Label(self.DodajRobuFrame,text="Tezina:")
        self.tezinaRobeInput = tk.Entry(self.DodajRobuFrame,width=5)

        self.dodajRobuButton = tk.Button(self.DodajRobuFrame,text="+",width=1,height=1,command=self.dodajRobu)
        self.ocistiRobuButton = tk.Button(self.DodajRobuFrame,text="X",width=1,height=1,command=self.ocistiRobu)

        self.robaLabel.grid(row=0,column=0)
        self.robaInput.grid(row=1,column=0)
        self.opisRobaLabel.grid(row=0,column=1)
        self.opisRobeInput.grid(row=1,column=1)

        self.duzinaRobeLabel.grid(row=2,column=0)
        self.duzinaRobeInput.grid(row=3,column=0)
        self.sirinaRobeLabel.grid(row=2,column=1)
        self.sirinaRobeInput.grid(row=3,column=1)
        self.visinaRobeLabel.grid(row=4,column=0)
        self.visinaRobeInput.grid(row=5,column=0)
        self.tezinaRobeLabel.grid(row=4,column=1)
        self.tezinaRobeInput.grid(row=5,column=1)

        self.RobaListBox = tk.Listbox(self.DodajRobuFrame,height=10,width=25)
        self.RobaListBox.grid(row=6,columnspan=2)

        self.dodajRobuButton.grid(row=7,column=0)
        self.ocistiRobuButton.grid(row=7,column=1)

    def odredisteFrameWidgets(self):
        self.odresiteFrame = tk.Frame(self)
        self.odresiteFrame.grid(row=0,column=0,sticky="s")

        self.odredisteLabel = tk.Label(self.odresiteFrame,text="Odredista:")
        self.odredisteListBox = tk.Listbox(self.odresiteFrame,height=5)

        self.odredisteLabel.grid(row=0,columnspan=2)
        self.odredisteListBox.grid(row=1,columnspan=2)

        odredistaLista = util.readFile("files/odredista.txt")
        for odrediste in odredistaLista:
            self.odredisteListBox.insert("end",odrediste.strip())

    def proveriID(self):
        ID = self.IDInput.get()
        if ID != "":
            status,lista = Login(None,None).checkID(ID)
            if status == True:
                self.PodnesiZahtevButton.configure(state="normal")
                self.PrikazIstorijuButton.configure(state="normal")
                self.IDPotrazitelja = ID
                self.CheckBoxNemamID.configure(state="disabled")
                messagebox.showinfo("OK!","ID Pronadjen!")
                self.controler.p = klase.korisnik.Potrazitelj(lista[0],lista[1],lista[2],lista[3],lista[4])
            elif status == False:
                self.IDPotrazitelja = ID
                self.PodnesiZahtevButton.configure(state="disabled")
                self.PrikazIstorijuButton.configure(state="disabled")
                messagebox.showerror("Error!","Nepostoji ID!")
        else:
            pass

    def dodajRobu(self):
        imeRobe = self.robaInput.get()
        opisRobe = self.opisRobeInput.get()
        duzinaRobe = self.duzinaRobeInput.get()
        sirinaRobe = self.sirinaRobeInput.get()
        visinaRobe = self.visinaRobeInput.get()
        tezinaRobe = self.tezinaRobeInput.get()

        if imeRobe == "" or opisRobe == "" or duzinaRobe == "" or sirinaRobe == "" or visinaRobe == "" or tezinaRobe == "":
            pass
        else:
            linija = imeRobe+"|"+opisRobe+"|"+duzinaRobe+"|"+sirinaRobe+"|"+visinaRobe+"|"+tezinaRobe
            self.RobaListBox.insert("end",linija)   

            # ciscenje input box-ova
            self.robaInput.delete(0,len(imeRobe))
            self.opisRobeInput.delete(0,len(opisRobe))
            self.duzinaRobeInput.delete(0,len(duzinaRobe))
            self.sirinaRobeInput.delete(0,len(sirinaRobe))
            self.visinaRobeInput.delete(0,len(visinaRobe))
            self.tezinaRobeInput.delete(0,len(tezinaRobe))


    def ocistiRobu(self):
        self.selektovanaRoba = self.RobaListBox.curselection()
        if self.selektovanaRoba == ():
            self.velicinaListBoxa = self.RobaListBox.size()
            self.RobaListBox.delete(0,self.velicinaListBoxa)
        else:
            self.RobaListBox.delete(self.selektovanaRoba)

    def disableIDInput(self):
        if self.CheckBoxNemamIDState.get() == 1:
            self.IDInput.configure(state="disabled")
            self.ProveriIDButton.configure(state="disabled")
            self.ImeInput.configure(state="normal")
            self.PrezimeInput.configure(state="normal")
            self.BrojTelefonaInput.configure(state="normal")
            self.EmailInput.configure(state="normal")
            self.PodnesiZahtevButton.configure(state="normal")
            self.PrikazIstorijuButton.configure(state="disabled")
            self.IDPotrazitelja = self.odrediIDPotrazitelja()
        elif self.CheckBoxNemamIDState.get() == 0:
            self.IDInput.configure(state="normal")
            self.ProveriIDButton.configure(state="normal")
            self.ImeInput.configure(state="disabled")
            self.PrezimeInput.configure(state="disabled")
            self.BrojTelefonaInput.configure(state="disabled")
            self.EmailInput.configure(state="disabled")
            self.PodnesiZahtevButton.configure(state="disabled")
            self.PrikazIstorijuButton.configure(state="disabled")
            self.IDPotrazitelja = None

    def odrediIDPotrazitelja(self):
        lines = util.readFile("files/korisnici.txt")
        lastLine = lines[-1].split("|")
        l = lastLine[0].split("#")
        return "K#"+str(int(l[1])+1)


    def podnesiZahtev(self):
        self.selektovanoOdrediste = self.odredisteListBox.curselection() # Vraca tuple od selektovanog elementa
        ime = self.ImeInput.get()
        prezime = self.PrezimeInput.get()
        brojtelefona = self.BrojTelefonaInput.get()
        email = self.EmailInput.get()

        if self.selektovanoOdrediste == ():
            messagebox.showerror("Error!","Niste izabrali odrediste!")
        elif self.RobaListBox.size() == 0:
            messagebox.showerror("Error!","Niste dodali robu!")
        else:
            if self.CheckBoxNemamIDState.get() == 1: # Ako je 'nemam ID' obelezeno
                if ime == "" or prezime == "" or brojtelefona == "" or email == "":
                    messagebox.showerror("Error!","Niste uneli podatke!")
                else:
                    line = self.IDPotrazitelja+"|"+ime+" "+prezime+"|"+brojtelefona+"|"+email+"|potrazitelj"+"\n"
                    util.saveFile("files/korisnici.txt",line)
            
            a = ZahtevZaTransport(self.odredisteListBox.get(self.selektovanoOdrediste[0]),self.IDPotrazitelja)
            messagebox.showinfo("OK!","Zahtev uspesno kreiran!")

            

            for i in range(self.RobaListBox.size()):
                l = self.RobaListBox.get(i).split("|")

                klase.roba.Roba(l[0],l[1],l[2],l[3],l[4],l[5],a.IDZahteva)

    def prikaziIstoriju(self):
        '''
        Prikaz 'Istorije Panel' i poziv inicijalizacije tabele
        '''
        self.controler.show_frame(PrikazIstorijePanel)
        self.controler.frames[PrikazIstorijePanel].tabelaFrameWidgets() # Inicijalizacija tabele tek kad se klikne dugme





class PrikazIstorijePanel(tk.Frame):
    def __init__(self,parent,controler):
        tk.Frame.__init__(self,parent)
        self.controler = controler
        self.createWidgets()

    def createWidgets(self):
        self.textL = tk.Label(self,text="Hello to prikaz istorije")
        self.textL.grid()

        self.nazadButton = tk.Button(self,text="Nazad",command=self.nazad)
        self.nazadButton.grid(row=3,columnspan=5)

    def tabelaFrameWidgets(self):
        '''
        Inicijalizacija tabela frejma, widget-sa na njoj i poziv header-a
        '''
        self.tabela = tk.Frame(self)
        self.tabela.grid(row=1,column=0,sticky="nsew")
        self.tabelaHeaderWidgets()

        self.expandImage = tk.PhotoImage(file="files/expand.png")
        self.collapseImage = tk.PhotoImage(file="files/collapse.png")

        self.recnik_frejmsa = {} # ovde se cuvaju 'buttonId':'frejm', tako da znamo kad koji frejm da se prikaze i sakrije
        self.lista_buttona = [] # ovde se cuvaju sva kreirani buttoni
        counter = -1 # a preko ove promenljive posle znamo koji je button pritisnut
        r = -1
        for i in self.controler.p.prikazZahteva(): # za svaki zahtev
            r+=2
            counter+=1
            lblIDZahteva = tk.Label(self.tabela,text=i[0]).grid(row=r,column=0) # pravi se labela na 'tabela' frejmu
            spliter = tk.Label(self.tabela,text="|").grid(row=r,column=1)
            lblDatumKreiranja = tk.Label(self.tabela,text=i[1]).grid(row=r,column=2)
            spliter = tk.Label(self.tabela,text="|").grid(row=r,column=3)
            lblDatumTransporta = tk.Label(self.tabela,text=i[2]).grid(row=r,column=4)
            spliter = tk.Label(self.tabela,text="|").grid(row=r,column=5)
            lblOdrediste = tk.Label(self.tabela,text=i[3]).grid(row=r,column=6)
            spliter = tk.Label(self.tabela,text="|").grid(row=r,column=7)
            lblIDPotrazitelja = tk.Label(self.tabela,text=i[4]).grid(row=r,column=8)
            spliter = tk.Label(self.tabela,text="|").grid(row=r,column=9)
            lblOznakaAviona = tk.Label(self.tabela,text=i[5]).grid(row=r,column=10)
            spliter = tk.Label(self.tabela,text="|").grid(row=r,column=11)
            lblStatus = tk.Label(self.tabela,text=i[6]).grid(row=r,column=12)
            self.b = tk.Button(self.tabela,image=self.expandImage,command= lambda i=i,counter=counter: self.expand(i,counter))
            self.b.grid(row=r,column=13)
            self.b.row = r # saljemo vrednost r da bi mogao frejm da se iscrta na dobrom mestu
            self.b.state = 0 # Ako je 0 = expand / 1 = collapse

            self.lista_buttona.append(self.b) # dodajemo button u listu


    def expand(self,zahtev,buttonId):
        '''
        Mogucnost prosirenja linije u zahtevu tako da se prikazu sve robe tog zahteva
        '''
        self.lista_buttona[buttonId].configure(image=self.collapseImage)
        r = self.lista_buttona[buttonId].row

        lines = util.readFile("files/roba.txt")

        # Ako je state = 0, onda je extend / ako je state = 1 onda je collapse
        if self.lista_buttona[buttonId].state == 0:
            self.lista_buttona[buttonId].state = 1

            self.robeFrejm = tk.Frame(self.tabela,width=100,height=50,bd=1,relief="solid")
            self.robeFrejm.grid(row=r+1,columnspan=10)

            self.recnik_frejmsa[buttonId] = self.robeFrejm # za buttonId dodeljuje odgovarajuci frejm


            self.prikazRobaHeaderWidgets()

            red = 0
            # nalazi sve robe koje imaju odgovarajuci id zahteva
            for line in lines:
                red+=1
                l = line.strip().split("|")
                if l[7] == zahtev[0]:
                    tk.Label(self.robeFrejm,text=l[0]).grid(row=red,column=0,sticky="w")
                    tk.Label(self.robeFrejm,text=l[1]).grid(row=red,column=1,sticky="w")
                    tk.Label(self.robeFrejm,text=l[2]).grid(row=red,column=2,sticky="w")
                    tk.Label(self.robeFrejm,text=l[3]).grid(row=red,column=3,sticky="s")
                    tk.Label(self.robeFrejm,text=l[4]).grid(row=red,column=4,sticky="s")
                    tk.Label(self.robeFrejm,text=l[5]).grid(row=red,column=5,sticky="s")
                    tk.Label(self.robeFrejm,text=l[6]).grid(row=red,column=6,sticky="s")
                    tk.Label(self.robeFrejm,text=l[7]).grid(row=red,column=7,sticky="w")

        elif self.lista_buttona[buttonId].state == 1:
            self.lista_buttona[buttonId].state = 0
            self.lista_buttona[buttonId].configure(image=self.expandImage)
            self.recnik_frejmsa[buttonId].destroy() # brise(krije) odgovarajuci frejm

    def tabelaHeaderWidgets(self):
        '''
        Inicijalizacija headera tabele
        ID | Datum Kreiranja | Datum Transporta | Odrediste | Potrazitelj | Avion | Status
        '''
        r = 0
        hID = tk.Label(self.tabela,text="ID").grid(row=r,column=0)
        spliter = tk.Label(self.tabela,text="|").grid(row=r,column=1)
        hDatumKreiranja = tk.Label(self.tabela,text="Daum Kreiranja").grid(row=r,column=2)
        spliter = tk.Label(self.tabela,text="|").grid(row=r,column=3)
        hDatumTransporta = tk.Label(self.tabela,text="Datum Transporta").grid(row=r,column=4)
        spliter = tk.Label(self.tabela,text="|").grid(row=r,column=5)
        hOdrediste = tk.Label(self.tabela,text="Odrediste").grid(row=r,column=6)
        spliter = tk.Label(self.tabela,text="|").grid(row=r,column=7)
        hIDPotrazitelja = tk.Label(self.tabela,text="Potrazitelj").grid(row=r,column=8)
        spliter = tk.Label(self.tabela,text="|").grid(row=r,column=9)
        hOznakaAviona = tk.Label(self.tabela,text="Avion").grid(row=r,column=10)
        spliter = tk.Label(self.tabela,text="|").grid(row=r,column=11)
        hStatus = tk.Label(self.tabela,text="Status").grid(row=r,column=12)


    def prikazRobaHeaderWidgets(self):
        tk.Label(self.robeFrejm,text="ID").grid(row=0,column=0)
        tk.Label(self.robeFrejm,text="Naziv").grid(row=0,column=1)
        tk.Label(self.robeFrejm,text="Opis").grid(row=0,column=2)
        tk.Label(self.robeFrejm,text="D").grid(row=0,column=3)
        tk.Label(self.robeFrejm,text="S").grid(row=0,column=4)
        tk.Label(self.robeFrejm,text="V").grid(row=0,column=5)
        tk.Label(self.robeFrejm,text="T").grid(row=0,column=6)
        tk.Label(self.robeFrejm,text="Zahtev").grid(row=0,column=7)

    def nazad(self):
        '''
        Vraca se nazad na 'Potrazitelj Panel' i brise 'tabela' frejm.
        Samim brisanjem 'tabela' frejma, brisu se svi widgeti na njemu,
        pa ne dolazi do dupliranja prikaza prilikom poziva tabele iznova i iznova
        '''
        self.controler.show_frame(PotraziteljPanel)
        self.tabela.destroy()

        
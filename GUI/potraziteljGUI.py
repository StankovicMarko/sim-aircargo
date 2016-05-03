import tkinter as tk
from klase.login import *
from klase.zahtevi import *

class PotraziteljPanel(tk.Frame):
    def __init__(self,parent,controler):
        tk.Frame.__init__(self,parent)
        self.proveriIDFrameWidgets()
        self.podaciFrameWidgets()
        self.dodajRobuFrameWidgets()
        self.podnesiZahtevButtonFrameWidgets()

    def proveriIDFrameWidgets(self):
        self.checkIDFrame = tk.Frame(self)
        self.checkIDFrame.grid(row=0,column=0)
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
        self.PodaciFrame.grid(row=1,column=0)
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
        self.PodnesiZahtevButtonFrame.grid(row=1,column=3)
        self.PodnesiZahtevButton = tk.Button(self.PodnesiZahtevButtonFrame,state="disabled",text="Podnesi Zahtev",height=2,width=10,command=self.podnesiZahtev)
        self.PrikazIstorijuButton = tk.Button(self.PodnesiZahtevButtonFrame,state="disabled",text="Prikaz Istorije",height=2,width=10,command=self.prikaziIstoriju)        
        self.PodnesiZahtevButton.grid(row=0,column=0)
        self.PrikazIstorijuButton.grid(row=1,column=0)


    def dodajRobuFrameWidgets(self):
        self.DodajRobuFrame = tk.Frame(self)
        self.DodajRobuFrame.grid(row=0,column=3)

        self.robaLabel = tk.Label(self.DodajRobuFrame,text="Roba:")
        self.kolicinaRobeLabel = tk.Label(self.DodajRobuFrame,text="Kolicina:")
        self.robaInput = tk.Entry(self.DodajRobuFrame,width=15)
        self.kolicinaRobeInput = tk.Entry(self.DodajRobuFrame,width=5)
        self.dodajRobuButton = tk.Button(self.DodajRobuFrame,text="+",width=1,height=1,command=self.dodajRobu)
        self.ocistiRobuButton = tk.Button(self.DodajRobuFrame,text="X",width=1,height=1,command=self.ocistiRobu)

        self.robaLabel.grid(row=0,column=0)
        self.kolicinaRobeLabel.grid(row=0,column=1)
        self.robaInput.grid(row=1,column=0)
        self.kolicinaRobeInput.grid(row=1,column=1)
        self.dodajRobuButton.grid(row=1,column=2)


        self.RobaListBox = tk.Listbox(self.DodajRobuFrame,height=5)
        self.RobaListBox.grid(row=2,columnspan=2)
        self.ocistiRobuButton.grid(row=3,column=2)

    def proveriID(self):
        ID = self.IDInput.get()
        if ID != "":
            print(ID)
            status = Login(None,None).checkID(ID)
            if status == True:
                self.PodnesiZahtevButton.configure(state="normal")
                self.PrikazIstorijuButton.configure(state="normal")
                self.IDPotrazitelja = ID
            elif status == False:
                self.IDPotrazitelja = ID
                self.PodnesiZahtevButton.configure(state="disabled")
                self.PrikazIstorijuButton.configure(state="disabled")
        else:
            pass

    def dodajRobu(self):
        if self.robaInput.get() == "" or self.kolicinaRobeInput.get() == "":
            pass
        else:
            self.robaIKolicina = self.robaInput.get() + ":" + self.kolicinaRobeInput.get()
            self.RobaListBox.insert("end",self.robaIKolicina)
            self.robaInput.delete(0,len(self.robaInput.get()))
            self.kolicinaRobeInput.delete(0,self.kolicinaRobeInput.get())

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
        lines = Login(None,None).readFile()
        l = lines[-1].split("|")
        return str(int(l[0])+1)



    def podnesiZahtev(self):
        print("click...")
        a = ZahtevZaTransport("London",self.IDPotrazitelja)
        print(a.datumKreiranja,a.IDZahteva)
        print(a.IDPotrazitelja)

    def prikaziIstoriju(self):
        print("click")
import tkinter as tk
from tkinter import messagebox
from klase.login import *
from klase.zahtevi import *
import klase.roba

class PotraziteljPanel(tk.Frame):
    def __init__(self,parent,controler):
        tk.Frame.__init__(self,parent)
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

        odredistaLista = self.ucitajOdredista()
        for odrediste in odredistaLista:
            self.odredisteListBox.insert("end",odrediste.strip())

    def ucitajOdredista(self):
        filename = "files/odredista.txt"
        f = open(filename,"r")
        lines = f.readlines()
        f.close()
        return lines

    def proveriID(self):
        ID = self.IDInput.get()
        if ID != "":
            print(ID)
            status = Login(None,None).checkID(ID)
            if status == True:
                self.PodnesiZahtevButton.configure(state="normal")
                self.PrikazIstorijuButton.configure(state="normal")
                self.IDPotrazitelja = ID
                self.CheckBoxNemamID.configure(state="disabled")
                messagebox.showinfo("OK!","ID Pronadjen!")
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
            linija = imeRobe+"|"+opisRobe+"|"+duzinaRobe+":"+sirinaRobe+":"+visinaRobe+"|"+tezinaRobe
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
        lines = Login(None,None).readFile()
        l = lines[-1].split("|")
        return str(int(l[0])+1)

    def sacuvajPodatkePotrazitelj(self,line):
        filename = "files/korisnici.txt"
        f = open(filename,"a")
        f.write(line+"\n")
        f.close()

    def podnesiZahtev(self):
        self.selektovanoOdrediste = self.odredisteListBox.curselection() # Vraca tuple od selektovanog elementa
        ime = self.ImeInput.get()
        prezime = self.PrezimeInput.get()
        brojtelefona = self.BrojTelefonaInput.get()
        email = self.EmailInput.get()

        if self.selektovanoOdrediste == ():
            messagebox.showerror("Error!","Niste izabrali odrediste!")
        else:
            if self.CheckBoxNemamIDState.get() == 1:
                if ime == "" or prezime == "" or brojtelefona == "" or email == "":
                    messagebox.showerror("Error!","Niste uneli podatke!")
                else:
                    line = self.IDPotrazitelja+"|"+ime+" "+prezime+"|"+brojtelefona+"|"+email+"|potrazitelj"
                    self.sacuvajPodatkePotrazitelj(line)


            a = ZahtevZaTransport(self.odredisteListBox.get(self.selektovanoOdrediste[0]),self.IDPotrazitelja)
            messagebox.showinfo("OK!","Zahtev uspesno kreiran!")
            print(a.datumKreiranja,a.IDZahteva)
            print(a.IDPotrazitelja)
            print(a.odrediste)

            for i in range(self.RobaListBox.size()):
                print(self.RobaListBox.get(i)+"|"+self.IDPotrazitelja)

    def prikaziIstoriju(self):
        print("click")
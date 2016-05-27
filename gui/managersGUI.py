import tkinter as tk
import klase.korisnici
import gui.windows
import klase.util_funk as util

class ManagerTransportaPanel(tk.Frame):
    def __init__(self, parent,controler):
        tk.Frame.__init__(self,parent)
        self.controler = controler
        self.createWidgets()
        # self.prikaZahtevaHeaderWidgets()

    def createWidgets(self):
        welcomeLabel = tk.Label(self, text="Ulogavani ste kao manager transporta")
        welcomeLabel.grid(row=0,column=1)

        self.prikazTransportButton = tk.Button(self,text="Transport Robe",command=self.prikazZahtevaTransportWidgets)
        self.prikazSmestanjeButton = tk.Button(self,text="Smestanje Aviona",command=self.prikazZahtevaSmestanjeWidgets)

        self.prikazTransportButton.grid(row=1,column=0)
        self.prikazSmestanjeButton.grid(row=1,column=2)

        self.frejmZahtevi = tk.Frame(self,bd=1,relief="solid")
        self.frejmZahtevi.grid(columnspan=3)
        self.logoutButton = tk.Button(self,text="Log Out!",command=self.logout)
        self.logoutButton.grid(column=1)


    def function(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    def prikaZahtevaHeaderWidgets(self):
        self.headerFrame = tk.Frame(self.frejmZahtevi)
        self.headerFrame.grid(row=0,column=0)
        self.zahtevID = tk.Label(self.headerFrame,text="ID").grid(row=0,column=0)
        tk.Label(self.headerFrame,text="      ").grid(row=0,column=1)
        self.datumkreiranja = tk.Button(self.headerFrame,text="Datum Kreiranja",relief="flat",command=lambda:self.sortedPrikaz(1)).grid(row=0,column=2)
        self.datumTransporta = tk.Button(self.headerFrame,text="Datum Transpota",relief="flat",command=lambda:self.sortedPrikaz(2)).grid(row=0,column=3)
        self.odredite = tk.Label(self.headerFrame,text="  Odrediste  ").grid(row=0,column=4)
        self.idPotrazitelja = tk.Label(self.headerFrame,text="Potrazitelj").grid(row=0,column=5)
        self.oznakaAviona = tk.Label(self.headerFrame,text="  Avion  ").grid(row=0,column=6)
        self.status = tk.Button(self.headerFrame,text="Status",relief="flat",command=lambda:self.sortedPrikaz(3)).grid(row=0,column=7)
        self.odobirZahtev = tk.Label(self.headerFrame,text="Odobri").grid(row=0,column=8)

    def prikazZahtevaTransportWidgets(self):
        try:
            self.znj1.destroy()
        except:
            pass

        self.prikaZahtevaHeaderWidgets()
        self.canvas = tk.Canvas(self.frejmZahtevi,bg="red",width=619)
        self.scrollbar = tk.Scrollbar(self.frejmZahtevi,orient="vertical",command=self.canvas.yview)
        self.newFrejm = tk.Frame(self.canvas,bd=1,relief="solid")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.grid(row=0,rowspan=2,column=9,sticky="ns")
        self.canvas.grid(row=1,columnspan=9,sticky="nsew")
        self.canvas.create_window((0,0),window=self.newFrejm,anchor='n')
        self.newFrejm.bind("<Configure>",self.function)

        self.prikazTransportButton.config(state="disabled")
        self.prikazSmestanjeButton.config(state="normal")

        self.prikaz(self.controler.m.prikazZahteva())

        
    def prikaz(self,lista):
        self.priv = []
        r = -1
        for i in lista:
            r+=1
            a =tk.Label(self.newFrejm,text=i[0])
            a.grid(row=r,column=0,sticky="w")
            self.priv.append(a) # Dodaje svaki objekat u listu da bi kasnije znao sta da obrise
            a1= tk.Label(self.newFrejm,text="   ")
            a1.grid(row=r,column=1)
            self.priv.append(a1)
            a2=tk.Label(self.newFrejm,text=i[1])
            a2.grid(row=r,column=2)
            self.priv.append(a2)
            a3=tk.Label(self.newFrejm,text="              ")
            a3.grid(row=r,column=3)
            self.priv.append(a3)
            a4=tk.Label(self.newFrejm,text=i[2])
            a4.grid(row=r,column=4)
            self.priv.append(a4)
            a5=tk.Label(self.newFrejm,text="           ")
            a5.grid(row=r,column=5)
            self.priv.append(a5)
            a6=tk.Label(self.newFrejm,text=i[3])
            a6.grid(row=r,column=6)
            self.priv.append(a6)
            a7=tk.Label(self.newFrejm,text="      ")
            a7.grid(row=r,column=7)
            self.priv.append(a7)
            a8=tk.Label(self.newFrejm,text=i[4])
            a8.grid(row=r,column=8,sticky="w")
            self.priv.append(a8)
            a9=tk.Label(self.newFrejm,text="  ")
            a9.grid(row=r,column=9)
            self.priv.append(a9)
            a10=tk.Label(self.newFrejm,text=i[5])
            a10.grid(row=r,column=10)
            self.priv.append(a10)
            a14=tk.Label(self.newFrejm,text="   ")
            a14.grid(row=r,column=11)
            self.priv.append(a14)
            a11=tk.Label(self.newFrejm,text=i[6])
            a11.grid(row=r,column=12)
            self.priv.append(a11)
            a12=tk.Label(self.newFrejm,text="   ")
            a12.grid(row=r,column=13)
            self.priv.append(a12)
            a13=tk.Checkbutton(self.newFrejm,text="")
            a13.grid(row=r,column=14)
            self.priv.append(a13)
            a15=tk.Label(self.newFrejm,text=" ")
            a15.grid(row=r,column=15)
            self.priv.append(a15)



    def sortedPrikaz(self,broj):
        for p in self.priv:
            p.destroy()

        if broj == 1:
            self.prikaz(util.sortPoDatumuKreiranja(self.controler.m.prikazZahteva()))
        elif broj == 2:
            self.prikaz(util.sortPoDatumuRealizacije(self.controler.m.prikazZahteva()))
        elif broj == 3:
            self.prikaz(util.sortPoStatusu(self.controler.m.prikazZahteva()))




    def prikazZahtevaSmestanjeWidgets(self):
        self.headerFrame.destroy()
        self.canvas.destroy()
        self.prikazTransportButton.config(state="normal")
        self.prikazSmestanjeButton.config(state="disabled")
        self.znj1 = tk.Label(self.frejmZahtevi,text="hello1")
        self.znj1.grid(sticky="nsew")

    def logout(self):
        self.headerFrame.destroy()
        self.canvas.destroy()
        self.controler.meni.destroy()
        self.controler.show_frame(gui.windows.LoginWindow)


class ManagerHangaraPanel(tk.Frame):
    def __init__(self, parent,controler):
        tk.Frame.__init__(self,parent)
        nekiLabel = tk.Label(self, text="Ulogovani ste kao manager hangara")
        nekiLabel.grid()
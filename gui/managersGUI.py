import tkinter as tk
import klase.korisnici
import gui.windows

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
        self.datumkreiranja = tk.Label(self.headerFrame,text="Datum Kreiranja").grid(row=0,column=2)
        self.datumTransporta = tk.Label(self.headerFrame,text="Datum Transpota").grid(row=0,column=3)
        self.odredite = tk.Label(self.headerFrame,text="  Odrediste  ").grid(row=0,column=4)
        self.idPotrazitelja = tk.Label(self.headerFrame,text="Potrazitelj").grid(row=0,column=5)
        self.oznakaAviona = tk.Label(self.headerFrame,text="  Avion  ").grid(row=0,column=6)
        self.status = tk.Label(self.headerFrame,text="Status").grid(row=0,column=7)
        self.odobirZahtev = tk.Label(self.headerFrame,text="Odobri").grid(row=0,column=8)

    def prikazZahtevaTransportWidgets(self):
        try:
            self.znj1.destroy()
        except:
            pass

        self.prikaZahtevaHeaderWidgets()
#
        self.canvas = tk.Canvas(self.frejmZahtevi)
        self.scrollbar = tk.Scrollbar(self.frejmZahtevi,orient="vertical",command=self.canvas.yview)
        self.newFrejm = tk.Frame(self.canvas,bd=1,relief="solid")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.grid(row=0,rowspan=2,column=9,sticky="ns")
        self.canvas.grid(row=1,columnspan=9,sticky="nsew")
        self.canvas.create_window((0,0),window=self.newFrejm,anchor='n')
        self.newFrejm.bind("<Configure>",self.function)
#
        self.prikazTransportButton.config(state="disabled")
        self.prikazSmestanjeButton.config(state="normal")
        
        r = -1
        for i in self.controler.m.prikazZahteva(sve=True):
            r+=1
            tk.Label(self.newFrejm,text=i[0]).grid(row=r,column=0,sticky="w")
            tk.Label(self.newFrejm,text="   ").grid(row=r,column=1)
            tk.Label(self.newFrejm,text=i[1]).grid(row=r,column=2)
            tk.Label(self.newFrejm,text="   ").grid(row=r,column=3)
            tk.Label(self.newFrejm,text=i[2]).grid(row=r,column=4)
            tk.Label(self.newFrejm,text="         ").grid(row=r,column=5)
            tk.Label(self.newFrejm,text=i[3]).grid(row=r,column=6)
            tk.Label(self.newFrejm,text="      ").grid(row=r,column=7)
            tk.Label(self.newFrejm,text=i[4]).grid(row=r,column=8,sticky="w")
            tk.Label(self.newFrejm,text="   ").grid(row=r,column=9)
            tk.Label(self.newFrejm,text=i[5]).grid(row=r,column=10)
            tk.Label(self.newFrejm,text=i[6]).grid(row=r,column=11)
            tk.Label(self.newFrejm,text="   ").grid(row=r,column=12)
            tk.Checkbutton(self.newFrejm,text="").grid(row=r,column=13)


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
        self.controler.show_frame(gui.windows.LoginWindow)


class ManagerHangaraPanel(tk.Frame):
    def __init__(self, parent,controler):
        tk.Frame.__init__(self,parent)
        nekiLabel = tk.Label(self, text="Ulogovani ste kao manager hangara")
        nekiLabel.grid()
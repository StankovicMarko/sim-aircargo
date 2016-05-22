import tkinter as tk
import klase.korisnici
import gui.windows

class ManagerTransportaPanel(tk.Frame):
    def __init__(self, parent,controler):
        tk.Frame.__init__(self,parent)
        self.controler = controler
        self.controler.resizable(0,0)

        welcomeLabel = tk.Label(self, text="Ulogavani ste kao manager transporta")
        welcomeLabel.grid(row=0,column=1)

        self.prikazTransportButton = tk.Button(self,text="Transport Robe",command=self.prikazZahtevaTransportWidgets)
        self.prikazSmestanjeButton = tk.Button(self,text="Smestanje Aviona",command=self.prikazZahtevaSmestanjeWidgets)

        self.prikazTransportButton.grid(row=1,column=0)
        self.prikazSmestanjeButton.grid(row=1,column=2)

        self.frejmZahtevi = tk.Frame(self,bd=1,relief="solid")
        self.frejmZahtevi.grid(columnspan=3,sticky="nsew")

        self.logoutButton = tk.Button(self,text="Log Out!",command=self.logout)
        self.logoutButton.grid(column=1)

    def prikazZahtevaTransportWidgets(self):
    	self.prikazTransportButton.config(state="disabled")
    	self.prikazSmestanjeButton.config(state="normal")
    	self.znj = tk.Label(self.frejmZahtevi,text="hello")
    	self.znj.grid(sticky="nsew")



    def prikazZahtevaSmestanjeWidgets(self):
    	self.prikazTransportButton.config(state="normal")
    	self.prikazSmestanjeButton.config(state="disabled")
    	self.znj1 = tk.Label(self.frejmZahtevi,text="hello1")
    	self.znj1.grid(sticky="nsew")


    def logout(self):
    	self.controler.show_frame(gui.windows.LoginWindow)


class ManagerHangaraPanel(tk.Frame):
    def __init__(self, parent,controler):
        tk.Frame.__init__(self,parent)
        nekiLabel = tk.Label(self, text="Ulogovani ste kao manager hangara")
        nekiLabel.grid()
import tkinter as tk
import klase.korisnici
import gui.windows

class ManagerTransportaPanel(tk.Frame):
    def __init__(self, parent,controler):
        tk.Frame.__init__(self,parent)
        self.controler = controler

        nekiLabel = tk.Label(self, text="Ulogavani ste kao manager transporta")
        nekiLabel.grid(row=0,columnspan=3)

        self.prikazTransport = tk.Button(self,text="Transport Robe")
        self.prikazSmestanje = tk.Button(self,text="Smestanje Aviona")

        self.prikazTransport.grid(row=1,column=0)
        self.prikazSmestanje.grid(row=1,column=2)

        self.frejm = tk.Frame(self,bd=1,relief="solid",width=500,height=200)
        self.frejm.grid(columnspan=3,sticky="nsew")

        self.logoutButton = tk.Button(self,text="Log Out!",command=self.logout)
        self.logoutButton.grid(column=1)



    def logout(self):
    	self.controler.show_frame(gui.windows.LoginWindow)


class ManagerHangaraPanel(tk.Frame):
    def __init__(self, parent,controler):
        tk.Frame.__init__(self,parent)
        nekiLabel = tk.Label(self, text="Ulogovani ste kao manager hangara")
        nekiLabel.grid()
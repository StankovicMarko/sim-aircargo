import tkinter as tk
from klase.login import *

class Glavna(tk.Tk):
    def __init__(self, *args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        container= tk.Frame(self)
        container.grid()

        self.frames = {}

        for i in (ManagerTransportaPanel, ManagerHangaraPanel, RadnikPanel, PotraziteljPanel, LoginWindow):
            frame = i(container,self)
            self.frames[i] = frame
            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(LoginWindow)


    def show_frame(self,page):
        frame = self.frames[page]
        frame.tkraise()



class LoginWindow(tk.Frame):
    def __init__(self, parent, controler):
        tk.Frame.__init__(self,parent)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid()
        self.createWidgets()
        self.controler = controler
        self.controler.title("Aplikacija")

    def createWidgets(self):
        self.loginFrame = tk.Frame(self)
        self.loginFrame.grid()
        self.usernameLabel = tk.Label(self.loginFrame,text="Username:")
        self.passwordLabel = tk.Label(self.loginFrame,text="Password:")

        self.usernameInput = tk.Entry(self.loginFrame)
        self.passwordInput = tk.Entry(self.loginFrame,show="*")

        self.loginButton = tk.Button(self.loginFrame,text="Login",command=self.login)

        self.checkBoxState = tk.IntVar()
        self.checkBox = tk.Checkbutton(self.loginFrame,text="Ulogujte se kao potrazitelj.",command=self.disableUsernamePasswordInputs,variable=self.checkBoxState)

        self.usernameLabel.grid(row=1,column=0)
        self.passwordLabel.grid(row=1,column=1)
        self.usernameInput.grid(row=2,column=0)
        self.passwordInput.grid(row=2,column=1)
        self.checkBox.grid(row=3,columnspan=2)
        self.loginButton.grid(row=4,columnspan=2)

    def disableUsernamePasswordInputs(self):
        if self.checkBoxState.get() == 1:
            self.usernameInput.configure(state="disabled")
            self.passwordInput.configure(state="disabled")
        elif self.checkBoxState.get() == 0:
            self.usernameInput.configure(state="normal")
            self.passwordInput.configure(state="normal")


    def login(self):
        uname = self.usernameInput.get()
        passw = self.passwordInput.get()

        if self.checkBoxState.get() == 0:
            print(uname,passw)
            a = Login(uname,passw)

            if a.uloga == None:
                print("Pogresan Username/Password")
            else:
                print("Uspesno ste se ulogovali!")
                print("Vi ste",a.imePrezime,"a uloga",a.uloga)

                if a.uloga == "mhangar":
                    self.controler.show_frame(ManagerHangaraPanel)
                elif a.uloga == "mtransport":
                    self.controler.show_frame(ManagerTransportaPanel)
                elif a.uloga == "radnik":
                    self.controler.show_frame(RadnikPanel)
        elif self.checkBoxState.get() == 1:
            self.controler.show_frame(PotraziteljPanel)


class ManagerTransportaPanel(tk.Frame):
    def __init__(self, parent,controler):
        tk.Frame.__init__(self,parent)
        nekiLabel = tk.Label(self, text="Ulogavani ste kao manager transporta")
        nekiLabel.grid()

class ManagerHangaraPanel(tk.Frame):
    def __init__(self, parent,controler):
        tk.Frame.__init__(self,parent)
        nekiLabel = tk.Label(self, text="Ulogovani ste kao manager hangara")
        nekiLabel.grid()

class RadnikPanel(tk.Frame):
    def __init__(self, parent,controler):
        tk.Frame.__init__(self,parent)
        nekiLabel = tk.Label(self, text="Ulogovani ste kao radnik")
        nekiLabel.grid()

class PotraziteljPanel(tk.Frame):
    def __init__(self,parent,controler):
        tk.Frame.__init__(self,parent)
        self.proveriIDFrameWidgets()
        self.podaciFrameWidgets()
        self.dodajRobuFrameWidgets()

    def proveriIDFrameWidgets(self):
        self.checkIDFrame = tk.Frame(self)
        self.checkIDFrame.grid(row=0,column=0)
        self.IDLabel = tk.Label(self.checkIDFrame,text="Unesite ID:")
        self.IDInput = tk.Entry(self.checkIDFrame)
        self.ProveriIDButton = tk.Button(self.checkIDFrame,text="Proveri")
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
        self.ImeInput = tk.Entry(self.PodaciFrame)
        self.PrezimeLabel = tk.Label(self.PodaciFrame,text="Prezime:")
        self.PrezimeInput = tk.Entry(self.PodaciFrame)
        self.BrojTelefonaLabel = tk.Label(self.PodaciFrame,text="Broj Telefona:")
        self.BrojTelefonaInput = tk.Entry(self.PodaciFrame)
        self.EmailLabel = tk.Label(self.PodaciFrame,text="Email:")
        self.EmailInput = tk.Entry(self.PodaciFrame)
        self.ImeLabel.grid(row=3,column=0)
        self.ImeInput.grid(row=3,column=1)
        self.PrezimeLabel.grid(row=4,column=0)
        self.PrezimeInput.grid(row=4,column=1)
        self.BrojTelefonaLabel.grid(row=5,column=0)
        self.BrojTelefonaInput.grid(row=5,column=1)
        self.EmailLabel.grid(row=6,column=0)
        self.EmailInput.grid(row=6,column=1)


    def dodajRobuFrameWidgets(self):
        self.DodajRobuFrame = tk.Frame(self)
        self.DodajRobuFrame.grid(row=0,column=3)

        self.robaLabel = tk.Label(self.DodajRobuFrame,text="Roba:")
        self.kolicinaRobeLabel = tk.Label(self.DodajRobuFrame,text="Kolicina:")
        self.robaInput = tk.Entry(self.DodajRobuFrame,width=15)
        self.kolicinaRobeInput = tk.Entry(self.DodajRobuFrame,width=5)
        self.dodajRobuButton = tk.Button(self.DodajRobuFrame,text="+",width=1,height=1,command=self.dodajRobu)

        self.robaLabel.grid(row=0,column=0)
        self.kolicinaRobeLabel.grid(row=0,column=1)
        self.robaInput.grid(row=1,column=0)
        self.kolicinaRobeInput.grid(row=1,column=1)
        self.dodajRobuButton.grid(row=1,column=2)



        self.RobaListBox = tk.Listbox(self.DodajRobuFrame,height=5)
        self.RobaListBox.grid(row=2,columnspan=2)

    def dodajRobu(self):
        if self.robaInput.get() == "" or self.kolicinaRobeInput.get() == "":
            pass
        else:
            self.robaIKolicina = self.robaInput.get() + ":" + self.kolicinaRobeInput.get()
            self.RobaListBox.insert("end",self.robaIKolicina)

    def disableIDInput(self):
        if self.CheckBoxNemamIDState.get() == 1:
            self.IDInput.configure(state="disabled")
            self.ProveriIDButton.configure(state="disabled")
        elif self.CheckBoxNemamIDState.get() == 0:
            self.IDInput.configure(state="normal")
            self.ProveriIDButton.configure(state="normal")
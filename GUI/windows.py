import tkinter as tk
from klase.login import *
from GUI.potraziteljGUI import *

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


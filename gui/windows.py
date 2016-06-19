import tkinter as tk
from tkinter import messagebox
import klase.login
from klase.korisnici import MenadzerHangara
from gui.potraziteljGUI import *
from gui.managersGUI import *
import gui.menibar


class Glavna(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.grid()

        self.frames = {}

        allFrames = [ManagerTransportaPanel, ManagerHangaraPanel, RadnikPanel, PotraziteljPanel, LoginWindow,
                     PrikazIstorijePanel]

        for i in allFrames:
            frame = i(container, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginWindow)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class LoginWindow(tk.Frame):
    def __init__(self, parent, controler):
        tk.Frame.__init__(self, parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid()
        self.createWidgets()
        self.controler = controler
        self.controler.title("Aplikacija")
        self.controler.bind("<Return>", lambda x: self.login())

    def createWidgets(self):
        self.loginFrame = tk.Frame(self)
        self.loginFrame.grid()
        self.usernameLabel = tk.Label(self.loginFrame, text="Username:")
        self.passwordLabel = tk.Label(self.loginFrame, text="Password:")

        self.usernameInput = tk.Entry(self.loginFrame)
        self.passwordInput = tk.Entry(self.loginFrame, show="*")

        self.loginButton = tk.Button(self.loginFrame, text="Login", command=self.login)

        self.checkBoxState = tk.IntVar()
        self.checkBox = tk.Checkbutton(self.loginFrame, text="Ulogujte se kao potrazitelj.",
                                       command=self.disableUsernamePasswordInputs, variable=self.checkBoxState)

        self.usernameLabel.grid(row=1, column=0)
        self.passwordLabel.grid(row=1, column=1)
        self.usernameInput.grid(row=2, column=0)
        self.passwordInput.grid(row=2, column=1)
        self.checkBox.grid(row=3, columnspan=2)
        self.loginButton.grid(row=4, columnspan=2)

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

        self.usernameInput.delete(0, len(self.usernameInput.get()))  # brise sve iz username box-a
        self.passwordInput.delete(0, len(self.passwordInput.get()))  # brise sve iz password box-a

        if self.checkBoxState.get() == 0:
            a = klase.login.Login(uname, passw)

            if a.uloga is None:
                messagebox.showerror("Error!", "Pogresan Username/Password")
            else:
                self.controler.meni = gui.menibar.Menibar(self.controler)
                if a.uloga == "mhangar":
                    self.controler.show_frame(ManagerHangaraPanel)
                    self.controler.frames[ManagerHangaraPanel].create_widgets()
                    m = MenadzerHangara(int(a.ID[2:]), a.ime, a.prezime, a.username)
                    self.controler.m = m
                    self.controler.meni.grid()

                elif a.uloga == "mtransport":
                    m = klase.korisnici.ManagerTransport(a.ID, a.ime, a.prezime)
                    self.controler.m = m
                    self.controler.show_frame(ManagerTransportaPanel)
                    self.controler.frames[ManagerTransportaPanel].prikazZahtevaTransportWidgets()
                    self.controler.meni.grid()

                elif a.uloga == "radnik":
                    self.controler.show_frame(RadnikPanel)
                    self.controler.frames[RadnikPanel].create_widgets()
                    self.controler.meni.grid()




        elif self.checkBoxState.get() == 1:
            self.controler.show_frame(PotraziteljPanel)


class RadnikPanel(tk.Frame):
    def __init__(self, parent, controler):
        tk.Frame.__init__(self, parent)
        # self.frejm = tk.Frame(self)
        # self.frejm.grid()
        self.controler = controler
        nekiLabel = tk.Label(self, text="Ulogovani ste kao radnik")
        nekiLabel.grid()

        #self.create_widgets()

    def logout(self):
        self.frejm.destroy()
        self.controler.meni.destroy()
        self.controler.show_frame(gui.windows.LoginWindow)

    def create_widgets(self):
        self.frejm = tk.Frame(self)
        self.frejm.grid()
        self.listbox = tk.Listbox(self.frejm, width=50)
        self.listbox.grid(row=2, columnspan=10, sticky='nsew')
        scrollbary = tk.Scrollbar(self.frejm)
        scrollbarx = tk.Scrollbar(self.frejm, orient='horizontal')
        self.listbox.config(yscrollcommand=scrollbary.set)
        scrollbary.config(command=self.listbox.yview)
        self.listbox.config(xscrollcommand=scrollbarx.set)
        scrollbarx.config(command=self.listbox.xview)
        scrollbarx.grid(row=3, columnspan=10, sticky='nsew')
        scrollbary.grid(row=2, column=10, sticky='nse')

        self.dug_smestanje = tk.Button(self.frejm, text="Odobreni zahtevi", command=self.odobreni_zahtevi)
        self.dug_smestanje.grid(row=1, column=0)

        self.dug_utovari_robu = tk.Button(self.frejm, text='Utovari Robu')
        self.dug_utovari_robu.grid(row=1, column=2)

        self.logout_button = tk.Button(self.frejm, text="Log Out!", command=self.logout)
        self.logout_button.grid(sticky='w')

    def odobreni_zahtevi(self):
        zahtevi = aplikacija.prikazi_zahteve_za_transport_odobrene_robe()
        self.dug_utovari_robu.config(command=lambda: self._utovari_robu(zahtevi))
        self.listbox.delete(0, 'end')
        for i, zahtev in enumerate(zahtevi):
            self.listbox.insert(i, zahtev)

    def _utovari_robu(self, zahtevi):
        try:
            odabran_zahtev = zahtevi[self.listbox.curselection()[0]]
            aplikacija.utovari_robu(odabran_zahtev)
            tk.messagebox.showinfo('', 'Roba uspesno utovarena')
            self.listbox.delete(0, 'end')
        except:
            tk.messagebox.showinfo('', 'Molimo izaberite zahtev ciju robu zelite da utovarite')

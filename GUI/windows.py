import tkinter as tk
from klase.login import *

class Glavna(tk.Tk):
	def __init__(self, *args,**kwargs):
		tk.Tk.__init__(self,*args,**kwargs)

		container= tk.Frame(self)
		container.grid()

		self.frames = {}

		for i in (ManagerTransportaPanel, ManagerHangaraPanel, RadnikPanel, LoginWindow):
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
		self.grid()
		self.createWidgets()
		self.controler = controler

	def createWidgets(self):
		self.usernameLabel = tk.Label(self,text="Username:")
		self.passwordLabel = tk.Label(self,text="Password:")

		self.usernameInput = tk.Entry(self)
		self.passwordInput = tk.Entry(self,show="*")

		self.loginButton = tk.Button(self,text="Login",command=self.login)

		self.usernameLabel.grid(row=1,column=0)
		self.passwordLabel.grid(row=1,column=1)
		self.usernameInput.grid(row=2,column=0)
		self.passwordInput.grid(row=2,column=1)
		self.loginButton.grid(row=3,columnspan=2)


	def login(self):
		uname = self.usernameInput.get()
		passw = self.passwordInput.get()
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
		
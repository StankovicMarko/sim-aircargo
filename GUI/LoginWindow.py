import tkinter as tk
from klase.login import *

class LoginWindow(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self,master)
		self.master.title("Login")
		self.master.resizable(height=False,width=False)
		self.grid()
		self.createWidgets()

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

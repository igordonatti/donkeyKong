from customtkinter import *

class App(CTk):
  def __init__(self):
    super().__init__()
    self.geometry("600x500")
    self.title("Donkey Kong - Menu")
    
    self.button = CTkButton(self, text="Jogar")
    self.button.pack(padx = 50, pady=50)

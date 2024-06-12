from customtkinter import *

class App(CTk): 
  def __init__(self,  start_game_callback):
    super().__init__()
    self.geometry("600x500")
    self.title("Donkey Kong - Menu")
    
    self.button = CTkButton(self, text="Jogar", command=start_game_callback)
    self.button.pack(padx = 50, pady=50)
    self.contador = 0
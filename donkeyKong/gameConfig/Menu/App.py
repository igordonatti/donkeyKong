from customtkinter import *

class App(CTk):
  def __init__(self):
    super().__init__()
    self.geometry("600x500")
    self.title("Donkey Kong - Menu")
    
    self.button = CTkButton(self, text="Jogar", command=self.playButton())
    self.button.pack(padx = 50, pady=50)

  def playButton(self):
    print("Button Clicked")
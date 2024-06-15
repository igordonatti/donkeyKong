# Importa todas as classes e funções do módulo customtkinter
from customtkinter import *

# Define a classe App, que herda de CTk, uma classe do customtkinter para criar janelas personalizadas
class App(CTk): 
  # Método construtor da classe App
  def __init__(self, start_game_callback):
    super().__init__()  # Chama o construtor da classe base CTk
    self.geometry("600x500")  # Define as dimensões da janela para 600x500 pixels
    self.title("Donkey Kong - Menu")  # Define o título da janela
    
    # Cria um botão com o texto "Jogar", que chama a função start_game_callback quando clicado
    self.button = CTkButton(self, text="Jogar", command=start_game_callback)
    self.button.pack(padx=50, pady=50)  # Posiciona o botão na janela com um padding de 50 pixels
    
    self.contador = 0  # Inicializa um contador como 0, possivelmente para uso futuro
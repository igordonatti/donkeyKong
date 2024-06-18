from game.main import main  # Importa a função principal do jogo
import pygame
from utils.constants import *  # Importa todas as constantes definidas no módulo constants
from menu import main_menu  # Importa a função do menu principal

# Configurações iniciais da janela do jogo
pygame.display.set_caption('Classic Donkey Kong Rebuild!')  # Define o título da janela
screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])  # Define o tamanho da janela do jogo

# Bloco principal
if __name__ == "__main__":
    action = main_menu(screen)  # Exibe o menu principal e espera pela ação do usuário
    if action == "start":
        main(screen)  # Inicia o jogo se a ação selecionada for "start"

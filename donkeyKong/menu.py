import pygame
import sys
from utils.constants import *

def main_menu(screen):
    selected = "start"  # Inicializa a opção selecionada como "start"

    while True:
        # Loop para eventos do Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Se o evento for de sair
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # Se uma tecla for pressionada
                if event.key == pygame.K_UP:  # Se a tecla for para cima
                    selected = "start"
                elif event.key == pygame.K_DOWN:  # Se a tecla for para baixo
                    selected = "quit"
                if event.key == pygame.K_RETURN:  # Se a tecla for Enter
                    if selected == "start":
                        return "start"  # Retorna "start" para iniciar o jogo
                    if selected == "quit":
                        pygame.quit()
                        sys.exit()  # Sai do jogo

        screen.fill((0, 0, 0))  # Preenche a tela com a cor preta

        # Renderiza o título do menu
        title = FONT2.render("Donkey Kong", True, (255, 255, 255))
        screen.blit(title, (WINDOW_WIDTH // 2 - title.get_width() // 2, 150))

        # Renderiza a opção "Start Game" com cor amarela se selecionada, branca se não
        if selected == "start":
            start = FONT2.render("Start Game", True, (255, 255, 0))
        else:
            start = FONT2.render("Start Game", True, (255, 255, 255))
        screen.blit(start, (WINDOW_WIDTH // 2 - start.get_width() // 2, 300))

        # Renderiza a opção "Quit" com cor amarela se selecionada, branca se não
        if selected == "quit":
            quit = FONT2.render("Quit", True, (255, 255, 0))
        else:
            quit = FONT2.render("Quit", True, (255, 255, 255))
        screen.blit(quit, (WINDOW_WIDTH // 2 - quit.get_width() // 2, 400))

        pygame.display.flip()  # Atualiza a tela para mostrar as mudanças

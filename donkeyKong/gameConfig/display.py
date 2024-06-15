# Importa o módulo pygame para criar interfaces gráficas e jogos
import pygame
# Importa o módulo os para interagir com o sistema operacional

import os

# Define a classe Display, responsável pela configuração da janela do jogo
class Display():
    # Método construtor da classe
    def __init__(self):
        # Configura a variável de ambiente SDL_VIDEO_CENTERED para centralizar a janela do jogo
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # Deve ser chamado antes de pygame.init()
        pygame.init()  # Inicializa todos os módulos importados do pygame
        self.info = pygame.display.Info()  # Obtém informações da tela atual
        # Define a largura e altura da tela com base nas informações obtidas, subtraindo valores para ajuste
        self.screen_width, self.screen_height = self.info.current_w, self.info.current_h
        self.WIDTH, self.HEIGHT = self.screen_width - 800, self.screen_height - 150
        # Calcula a largura e altura de cada seção da tela para o jogo
        self.section_width = self.WIDTH // 32
        self.section_height = self.HEIGHT // 32
        self.slope = self.section_height // 8  # Define a inclinação usada em elementos do jogo
        self._setup_display()  # Chama o método para configurar a janela do jogo

    # Método privado para configurar a janela do jogo
    def _setup_display(self):
        pygame.init()  # Reinicializa os módulos do pygame (redundante, considerar remover)
        pygame.display.set_caption('Donkey Kong - 1981')  # Define o título da janela do jogo

    # Propriedade para obter a largura da janela do jogo
    @property
    def width(self):
        return self.WIDTH  # Retorna a largura ajustada da janela
  
    # Propriedade para obter a altura da janela do jogo
    @property
    def height(self):
        return self.HEIGHT  # Retorna a altura ajustada da janela
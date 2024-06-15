# Importa o módulo pygame para criar jogos e interfaces gráficas
import pygame
# Importa a classe InitialMap do pacote maps para definir o mapa inicial do jogo
from ..maps.initialmap import InitialMap
# Importa a classe Display do pacote atual para gerenciar a exibição do jogo
from .display import Display
# Importa a classe Mario do pacote sprites para criar e gerenciar o personagem Mario
from ..sprites.mario import Mario
# Importa o módulo customtkinter para criar interfaces gráficas personalizadas
from customtkinter import *
# Importa a classe App do pacote Menu para gerenciar o menu do jogo
from .Menu.App import App

# Define a classe Game, que é a classe principal para executar o jogo
class Game():
    # Método construtor da classe Game
    def __init__(self):
        self.fps = 60  # Define a taxa de quadros por segundo do jogo
        self.display = Display()  # Cria uma instância de Display para gerenciar a exibição
        
        self.menu = None  # Inicializa o menu como None, será definido posteriormente
        
        # Define a tela do jogo com as dimensões especificadas em Display
        self.screen = pygame.display.set_mode((self.display.width, self.display.height))
        # Cria uma instância de InitialMap, que define o mapa inicial do jogo
        self.map = InitialMap(self.screen, self.display.section_width, self.display.section_height, self.display.slope)
      
        # Obtém a posição inicial de Mario no mapa
        start_x, start_y = self.map.get_initial_mario_position()
        # Cria uma instância de Mario na posição inicial obtida
        self.mario = Mario(start_x, start_y, self.map.platforms)
        
        self.clock = pygame.time.Clock()  # Cria um relógio para controlar o tempo do jogo
        self.keys = pygame.key.get_pressed()  # Obtém o estado atual das teclas pressionadas
        
    # Método para iniciar o jogo, destruindo o menu se existir e chamando o método run
    def start_game(self):
      if self.menu:
        self.menu.destroy()  # Destrói o menu se ele existir
      self.run()  # Inicia o loop principal do jogo

    # Método run contém o loop principal do jogo
    def run(self):        
        while True:  # Loop infinito para manter o jogo rodando
            for event in pygame.event.get():  # Itera sobre todos os eventos do pygame
                if event.type == pygame.QUIT:  # Se o evento for de saída, fecha o jogo
                    pygame.quit()
                    exit()

            self.screen.fill((0, 0, 0))  # Limpa a tela preenchendo-a com preto
            self.map.draw()  # Desenha o mapa na tela
            self.mario.movement()  # Atualiza o movimento de Mario
            self.mario.drawMario(self.screen)  # Desenha Mario na tela
            pygame.display.update()  # Atualiza a tela com o que foi desenhado
            self.clock.tick(60)  # Controla o FPS para que seja constante
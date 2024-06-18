import pygame
from utils.constants import *

class Ladder:
    def __init__(self, x_pos, y_pos, length):
        # Inicializa a posição e o comprimento da escada
        self.x_pos = x_pos * SECTION_WIDTH
        self.y_pos = y_pos
        self.length = length
        # Inicializa o atributo body como None
        self.body = None

    def draw(self, screen):
        # Define a largura das linhas e a cor da escada
        line_width = 3
        lad_color = 'light blue'
        lad_height = 0.6  # Define a altura de cada degrau como 60% da altura da seção
        
        # Desenha cada degrau da escada
        for i in range(self.length):
            # Coordenada superior do degrau atual
            top_coord = self.y_pos + lad_height * SECTION_HEIGHT * i
            # Coordenada inferior do degrau atual
            bot_coord = top_coord + lad_height * SECTION_HEIGHT
            # Coordenada do meio do degrau atual
            mid_coord = (lad_height / 2) * SECTION_HEIGHT + top_coord
            # Coordenada esquerda da escada
            left_coord = self.x_pos
            # Coordenada direita da escada
            right_coord = left_coord + SECTION_WIDTH
            
            # Desenha as linhas do degrau
            pygame.draw.line(screen, lad_color, (left_coord, top_coord), (left_coord, bot_coord), line_width)  # Linha esquerda
            pygame.draw.line(screen, lad_color, (right_coord, top_coord), (right_coord, bot_coord), line_width)  # Linha direita
            pygame.draw.line(screen, lad_color, (left_coord, mid_coord), (right_coord, mid_coord), line_width)  # Linha do meio
        
        # Define a área de colisão da escada
        self.body = pygame.rect.Rect((self.x_pos, self.y_pos - SECTION_HEIGHT), (SECTION_WIDTH, (lad_height * self.length * SECTION_HEIGHT + SECTION_HEIGHT)))

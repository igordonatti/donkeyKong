import pygame
from utils.constants import *

class Bridge:
    def __init__(self, x_pos, y_pos, length):
        # Inicializa a posição e o comprimento da ponte
        self.x_pos = x_pos * SECTION_WIDTH
        self.y_pos = y_pos
        self.length = length
        # Inicializa o atributo top como None
        self.top = None

    def draw(self, screen):
        # Define a largura das linhas e a cor da plataforma
        line_width = 7
        platform_color = (225, 51, 129)
        
        # Desenha cada seção da ponte
        for i in range(self.length):
            # Coordenadas para a parte inferior da ponte
            bot_coord = self.y_pos + SECTION_HEIGHT
            # Coordenada esquerda da seção atual
            left_coord = self.x_pos + (SECTION_WIDTH * i)
            # Coordenada do meio da seção atual
            mid_coord = left_coord + (SECTION_WIDTH * 0.5)
            # Coordenada direita da seção atual
            right_coord = left_coord + SECTION_WIDTH
            # Coordenada superior da ponte
            top_coord = self.y_pos
            
            # Desenha as linhas da ponte
            pygame.draw.line(screen, platform_color, (left_coord, top_coord), (right_coord, top_coord), line_width)  # Linha superior
            pygame.draw.line(screen, platform_color, (left_coord, bot_coord), (right_coord, bot_coord), line_width)  # Linha inferior
            pygame.draw.line(screen, platform_color, (left_coord, bot_coord), (mid_coord, top_coord), line_width)  # Linha diagonal esquerda
            pygame.draw.line(screen, platform_color, (mid_coord, top_coord), (right_coord, bot_coord), line_width)  # Linha diagonal direita
        
        # Define a área de colisão superior da ponte
        self.top = pygame.rect.Rect((self.x_pos, self.y_pos), (self.length * SECTION_WIDTH, 2))

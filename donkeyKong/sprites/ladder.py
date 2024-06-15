# Importa o módulo pygame para usar suas funcionalidades
import pygame

# Define a classe Ladder, que é uma subclasse de pygame.sprite.Sprite
class Ladder(pygame.sprite.Sprite):
    # Método construtor da classe
    def __init__(self, x_pos, y_pos, length, section_width, section_height):
        # Chama o construtor da superclasse
        super().__init__()
        # Inicializa as variáveis de instância com os valores passados
        self.x_pos = x_pos  # Posição X da escada
        self.y_pos = y_pos  # Posição Y da escada
        self.length = length  # Número de degraus da escada
        self.section_width = section_width  # Largura de cada seção da escada
        self.section_height = section_height  # Altura de cada seção da escada
        self.lad_height = 0.6 * section_height  # Altura de cada degrau, definida como 60% da altura da seção

        # Cria um retângulo que representa o corpo da escada, ajustando a posição Y para incluir o degrau superior
        self.body = pygame.Rect(self.x_pos, self.y_pos - self.lad_height, self.section_width,
                                self.lad_height * self.length + self.lad_height)

    # Método para desenhar a escada na tela
    def draw(self, screen):
        line_width = 3  # Define a largura das linhas
        lad_color = (173, 216, 230)  # Define a cor da escada (azul claro) em formato RGB
        # Loop para desenhar cada degrau da escada
        for i in range(self.length):
            # Calcula as coordenadas do topo, base e meio de cada degrau
            top_coord = self.y_pos + self.lad_height * i
            bot_coord = top_coord + self.lad_height
            mid_coord = (self.lad_height / 2) + top_coord
            # Calcula as coordenadas esquerda e direita da escada
            left_coord = self.x_pos
            right_coord = left_coord + self.section_width
            
            # Desenha as linhas laterais e do meio de cada degrau
            pygame.draw.line(screen, lad_color, (left_coord, top_coord), (left_coord, bot_coord), line_width)
            pygame.draw.line(screen, lad_color, (right_coord, top_coord), (right_coord, bot_coord), line_width)
            pygame.draw.line(screen, lad_color, (left_coord, mid_coord), (right_coord, mid_coord), line_width)
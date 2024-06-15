# Importa o módulo pygame para usar suas funcionalidades
import pygame

# Define a classe Bridge, que é uma subclasse de pygame.sprite.Sprite
class Bridge(pygame.sprite.Sprite):
    # Método construtor da classe
    def __init__(self, x_pos, y_pos, length, section_width, section_height):
        # Chama o construtor da superclasse
        super().__init__()
        # Inicializa as variáveis de instância com os valores passados
        self.x_pos = x_pos  # Posição X da ponte
        self.y_pos = y_pos  # Posição Y da ponte
        self.length = length  # Número de seções da ponte
        self.section_width = section_width  # Largura de cada seção da ponte
        self.section_height = section_height  # Altura de cada seção da ponte
        # Cria um retângulo que representa a parte superior da ponte
        self.top = pygame.Rect(x_pos, y_pos, length * section_width, section_height)
        
    # Método para desenhar a ponte na tela
    def draw(self, screen):
        line_width = 7  # Define a largura das linhas
        platform_color = (255, 51, 129)  # Define a cor da ponte (rosa) em formato RGB
        # Loop para desenhar cada seção da ponte
        for i in range(self.length):
            # Calcula as coordenadas esquerda e direita de cada seção
            left_coord = self.x_pos + (self.section_width * i)
            right_coord = left_coord + self.section_width
            # Calcula as coordenadas superior e inferior de cada seção
            top_coord = self.y_pos
            bot_coord = self.y_pos + self.section_height
            # Desenha as linhas superior e inferior de cada seção
            pygame.draw.line(screen, platform_color, (left_coord, top_coord), (right_coord, top_coord), line_width)
            pygame.draw.line(screen, platform_color, (left_coord, bot_coord), (right_coord, bot_coord), line_width)
            # Desenha as linhas diagonais que conectam as linhas superior e inferior em cada seção
            pygame.draw.line(screen, platform_color, (left_coord, bot_coord), (left_coord + (self.section_width / 2), top_coord), line_width)
            pygame.draw.line(screen, platform_color, (left_coord + (self.section_width / 2), top_coord), (right_coord, bot_coord), line_width)
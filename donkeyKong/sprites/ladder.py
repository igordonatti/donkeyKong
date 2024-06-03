import pygame

class Ladder(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, length, section_width, section_height):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.length = length
        self.section_width = section_width
        self.section_height = section_height
        self.lad_height = 0.6 * section_height  # Define a altura de cada degrau

        # Corrige a criação do retângulo 'body' para incluir toda a altura da escada
        self.body = pygame.Rect(self.x_pos, self.y_pos - self.lad_height, self.section_width,
                                self.lad_height * self.length + self.lad_height)

    def draw(self, screen):
        line_width = 3
        lad_color = (173, 216, 230)  # Cor azul claro em formato RGB
        for i in range(self.length):
            top_coord = self.y_pos + self.lad_height * i
            bot_coord = top_coord + self.lad_height
            mid_coord = (self.lad_height / 2) + top_coord
            left_coord = self.x_pos
            right_coord = left_coord + self.section_width
            
            pygame.draw.line(screen, lad_color, (left_coord, top_coord), (left_coord, bot_coord), line_width)
            pygame.draw.line(screen, lad_color, (right_coord, top_coord), (right_coord, bot_coord), line_width)
            pygame.draw.line(screen, lad_color, (left_coord, mid_coord), (right_coord, mid_coord), line_width)

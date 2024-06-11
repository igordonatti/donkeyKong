import pygame

class Bridge(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, length, section_width, section_height):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.length = length
        self.section_width = section_width
        self.section_height = section_height
        # Adiciona a criação do retângulo 'top'
        self.top = pygame.Rect(x_pos, y_pos, length * section_width, section_height)
        
    def draw(self, screen):
        line_width = 7
        platform_color = (255, 51, 129)  # Rosa
        for i in range(self.length):
            left_coord = self.x_pos + (self.section_width * i)
            right_coord = left_coord + self.section_width
            top_coord = self.y_pos
            bot_coord = self.y_pos + self.section_height
            pygame.draw.line(screen, platform_color, (left_coord, top_coord), (right_coord, top_coord), line_width)
            pygame.draw.line(screen, platform_color, (left_coord, bot_coord), (right_coord, bot_coord), line_width)
            pygame.draw.line(screen, platform_color, (left_coord, bot_coord), (left_coord + (self.section_width / 2), top_coord), line_width)
            pygame.draw.line(screen, platform_color, (left_coord + (self.section_width / 2), top_coord), (right_coord, bot_coord), line_width)

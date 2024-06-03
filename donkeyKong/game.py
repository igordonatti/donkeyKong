import pygame
from .maps.initialmap import InitialMap
from .display import Display
from .sprites.mario import Mario

class DonkeyKong():
    def __init__(self):
        self.fps = 60
        self.display = Display()
        self.mario = Mario()
        self.screen = pygame.display.set_mode((self.display.width, self.display.height))
        self.map = InitialMap(self.screen, self.display.section_width, self.display.section_height, self.display.slope)
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.screen.fill((0, 0, 0))
            self.map.draw()  # Chama draw aqui, passando self.screen
            self.mario.movement()
            self.mario.drawMario(self.screen)
            pygame.display.update()
            self.clock.tick(60)

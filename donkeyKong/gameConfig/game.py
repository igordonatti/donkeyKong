import pygame
from ..maps.initialmap import InitialMap
from .display import Display
from ..sprites.mario import Mario
from customtkinter import *
from .Menu.App import App

# O jogo se inicia aqui
class Game():
    def __init__(self):
        self.fps = 60
        self.display = Display()
        
        self.menu = None
        
        self.screen = pygame.display.set_mode((self.display.width, self.display.height))
        self.map = InitialMap(self.screen, self.display.section_width, self.display.section_height, self.display.slope)
      
        start_x, start_y = self.map.get_initial_mario_position()
        self.mario = Mario(start_x, start_y, self.map.platforms)
        
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()
        
    def start_game(self):
      if self.menu:
        self.menu.destroy()
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

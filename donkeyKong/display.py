import pygame
import os

class Display():
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # call before pygame.init()
        pygame.init()
        self.info = pygame.display.Info()
        self.screen_width, self.screen_height = self.info.current_w, self.info.current_h
        self.WIDTH, self.HEIGHT = self.screen_width - 800, self.screen_height - 150
        self.section_width = self.WIDTH // 32
        self.section_height = self.HEIGHT // 32
        self.slope = self.section_height // 8
        self._setup_display()

    def _setup_display(self):
        pygame.init()
        pygame.display.set_caption('Donkey Kong - 1981')

    @property
    def width(self):
        return self.WIDTH
  
    @property
    def height(self):
        return self.HEIGHT

import pygame

class Display():
  def __init__(self):
    self.WIDTH = 500
    self.HEIGHT = 700

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


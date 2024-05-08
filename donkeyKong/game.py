import pygame
from .display import Display
from .sprites.mario import Mario


class DonkeyKong():
  def __init__(self):
    self.fps = 60
    self.display = Display()
    self.mario = Mario()

    self.screen = pygame.display.set_mode((self.display.WIDTH, self.display.HEIGHT))

    self.clock = pygame.time.Clock()
    self.draw_mario()
    self.run()
  
  def run(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        
        if event.type == pygame.K_LEFT:
          self.mario.plat_move(-1)


      pygame.display.update()
      
      self.clock.tick(60)

  def draw_mario(self):
    self.mario_surface = pygame.image.load('./assets/shapes/pngs/mario_static.png')
    self.mario_surface = pygame.transform.scale(self.mario_surface, (45, 36))
    self.mario_rect = self.mario_surface.get_rect(midbottom = (self.mario.posX, self.mario.posY))

    self.screen.blit(self.mario_surface, self.mario_rect)
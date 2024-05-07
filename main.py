import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption('Donkey Kong - 1981')
clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  # draw all our elements
  # upddate everything
  pygame.display.update()
  # not to run more that 60s per minute
  clock.tick(60)
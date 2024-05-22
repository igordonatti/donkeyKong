import pygame

class Mario(pygame.sprite.Sprite):
  def __init__(self):
    self.__posX = 50
    self.__posY = 700
    self.__velocity = 3
    self.__gravity = 1
    self.__isJumping = False
    self.__jumpSpeed = 10
    self.__yVelocity = 5
    self.__groundLevel = 700
    
  def plat_move(self):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
      self.__posX += self.__velocity
    if keys[pygame.K_LEFT]:
      self.__posX -= self.__velocity
    if keys[pygame.K_SPACE] and not self.__isJumping:
      self.__isJumping = True
      self.__yVelocity = -self.__jumpSpeed
      
    self.applyGravity()
      
  def drawMario(self):
    self.mario_surface = pygame.image.load('./assets/shapes/pngs/mario_static.png')
    self.mario_surface = pygame.transform.scale(self.mario_surface, (45, 36))
    self.mario_rect = self.mario_surface.get_rect(midbottom = (self.mario.posX, self.mario.posY))
    self.screen.blit(self.mario_surface, self.mario_rect)
      
  def applyGravity(self):
    if self.__isJumping:
      self.__posY += self.__yVelocity
      self.__yVelocity += self.__gravity
      
      if self.__posY >= self.__groundLevel:
        self.__posY = self.__groundLevel
        self.__isJumping = False
        self.__yVelocity = 0
      
  @property
  def posX(self):
    return self.__posX
  
  @property
  def posY(self):
    return self.__posY
  
  @property
  def gravity(self):
    return self.__gravity


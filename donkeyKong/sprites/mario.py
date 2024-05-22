import pygame

mario_live = './assets/shapes/svgs/mario_static.svg'
mario_running = './assets/shapes/svgs/mario_running_1.svg'
mario_jump = './assets/shapes/svgs/mario_jump.svg'

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
    self.__direction = 'R'
    
    self.__isRunning = False
    
    self.mario_surface = pygame.image.load(mario_live)
    self.mario_surface = pygame.transform.scale(self.mario_surface, (45, 36))
  def movement(self):
    keys = pygame.key.get_pressed()
    
    
    # Movimentacoes em X
    if keys[pygame.K_RIGHT]:
      self.__isRunning = True
      self.__direction = 'R'
      self.__posX += self.__velocity      
    elif keys[pygame.K_LEFT]:
      self.__isRunning = True
      self.__direction = 'L'
      self.__posX -= self.__velocity
    else: 
      self.__isRunning = False 
      
    
    # Movimentacoes em Y
    if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and not self.__isJumping:
      self.__isJumping = True
      self.__yVelocity = -self.__jumpSpeed
    
    self.applyGravity()
      
  def drawMario(self, screen):
    
    # Desenhos em X
    if(self.__isRunning and self.__direction == 'R' and not self.__isJumping):
      self.mario_surface = pygame.image.load(mario_running) 
      self.mario_surface = pygame.transform.scale(self.mario_surface, (45, 36))
      
    elif (self.__isRunning and self.__direction == 'L' and not self.__isJumping):
      self.mario_surface = pygame.image.load(mario_running)
      self.mario_surface = pygame.transform.scale(self.mario_surface, (45, 36))
      self.mario_surface = pygame.transform.flip(self.mario_surface, True, False)
      
    elif (self.__direction == 'L' and not self.__isJumping):
      self.mario_surface = pygame.image.load(mario_live)
      self.mario_surface = pygame.transform.scale(self.mario_surface, (45, 36))
      self.mario_surface = pygame.transform.flip(self.mario_surface, True, False)
      
    elif(self.__direction == 'R' and not self.__isJumping): 
      self.mario_surface = pygame.image.load(mario_live)
      self.mario_surface = pygame.transform.scale(self.mario_surface, (45, 36))
      
    # Desenhos em Y
    if(self.__isJumping and self.__direction == 'R'):
      self.mario_surface = pygame.image.load(mario_jump)
      self.mario_surface = pygame.transform.scale(self.mario_surface, (45, 36))
      
    elif(self.__isJumping and self.__direction == 'L'):
      self.mario_surface = pygame.image.load(mario_jump)
      self.mario_surface = pygame.transform.scale(self.mario_surface, (45, 36))
      self.mario_surface = pygame.transform.flip(self.mario_surface, True, False)
      
    self.mario_rect = self.mario_surface.get_rect(midbottom = (self.__posX, self.__posY))
    screen.blit(self.mario_surface, self.mario_rect)
      
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


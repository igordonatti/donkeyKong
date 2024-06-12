import pygame

mario_live = './assets/shapes/svgs/mario_static.svg'
mario_running = './assets/shapes/svgs/mario_running_1.svg'
mario_running2 = './assets/shapes/svgs/mario_running_2.svg'
mario_jump = './assets/shapes/svgs/mario_jump.svg'

class Mario(pygame.sprite.Sprite):
  def __init__(self, start_x, start_y, platforms):
    self.__posX = start_x # Posição Inicial em X
    self.__posY = start_y # Posição Inicial em Y
    self.__velocity = 3 # Velocidade de movimentação
    self.__gravity = 1 # Variável para aplicar a gravidade ao pulo
    self.__isJumping = False # Controla para saber se está pulando ou não
    self.__jumpSpeed = 10 # Altura do pulo
    self.__yVelocity = 5 # Velocidade em Y
    self.__groundLevel = start_y # Controla o terreno em que o Mario está (Plataformas)
    self.__direction = 'R' # Controla a direção do Mario (Direita ou Esquerda)
    self.__frame_counter = 0  # Contador para alternar entre as imagens de corrida
    self.__isRunning = False # Mario está se movendo para os lados ou não
    
    self.platforms = platforms # Adiciona as plataformas
    
    self.mario_surface = pygame.image.load(mario_live) # Carrega a primeira imagem do Mario 
    self.mario_surface = pygame.transform.scale(self.mario_surface, (45, 36)) # Aumenta a escala do Mario
  def movement(self): # Método de movimentação em X e Y
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
        # Atualiza o contador de frames
        self.__frame_counter = (self.__frame_counter + 1) % 12  # Ciclo a cada 12 frames

        # Escolhe a imagem de corrida correta
        if self.__isRunning and not self.__isJumping:
            if self.__frame_counter < 6:
                run_surface = pygame.image.load(mario_running)
            else:
                run_surface = pygame.image.load(mario_running2)
                
            run_surface = pygame.transform.scale(run_surface, (45, 36))
            
            if self.__direction == 'L':
              run_surface = pygame.transform.flip(run_surface, True, False)
              
            self.mario_surface = run_surface
            
        elif not self.__isJumping:
            self.mario_surface = pygame.image.load(mario_live)
            self.mario_surface = pygame.transform.scale(self.mario_surface, (45, 36))
            if self.__direction == 'L':
                self.mario_surface = pygame.transform.flip(self.mario_surface, True, False)
        
        # Desenhos em Y
        if self.__isJumping:
            jump_surface = pygame.image.load(mario_jump)
            jump_surface = pygame.transform.scale(jump_surface, (45, 36))
            if self.__direction == 'L':
                jump_surface = pygame.transform.flip(jump_surface, True, False)
            self.mario_surface = jump_surface

        self.mario_rect = self.mario_surface.get_rect(midbottom=(self.__posX, self.__posY))
        screen.blit(self.mario_surface, self.mario_rect)

      
  def applyGravity(self):
    if self.__isJumping:
      self.__posY += self.__yVelocity
      self.__yVelocity += self.__gravity
      
    if not self.__isJumping or self.__yVelocity >= 0:
      on_platform = False
      for platform in self.platforms:
        if platform.collidepoint(self.__posX, self.__posY):
          self.__posY = platform.top
          self.__groundLevel = platform.top
          self.__isJumping = False
          self.__yVelocity = 0
          on_platform = True
          break
        
        if not on_platform:
          self.__isJumping = True
          
        self.mario_rect.midbottom = (self.__posX, self.__posY)
     
      
  @property
  def posX(self):
    return self.__posX
  
  @property
  def posY(self):
    return self.__posY
  
  @property
  def gravity(self):
    return self.__gravity


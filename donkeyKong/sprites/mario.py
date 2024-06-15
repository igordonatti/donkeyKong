import pygame

# Caminhos para os arquivos de imagem do Mario
mario_live = './assets/shapes/svgs/mario_static.svg'
mario_running = './assets/shapes/svgs/mario_running_1.svg'
mario_running2 = './assets/shapes/svgs/mario_running_2.svg'
mario_jump = './assets/shapes/svgs/mario_jump.svg'

# Classe Mario, herda de pygame.sprite.Sprite
class Mario(pygame.sprite.Sprite):
  def __init__(self, start_x, start_y, platforms):
    # Inicializa as variáveis de posição, velocidade, gravidade, etc.
    self.__posX = start_x # Posição inicial em X
    self.__posY = start_y # Posição inicial em Y
    self.__velocity = 3 # Velocidade de movimento
    self.__gravity = 1 # Gravidade aplicada ao pular
    self.__isJumping = False # Indica se o Mario está pulando
    self.__jumpSpeed = 10 # Velocidade inicial do pulo
    self.__yVelocity = 5 # Velocidade vertical
    self.__groundLevel = start_y # Nível do chão (para plataformas)
    self.__direction = 'R' # Direção do Mario (Direita ou Esquerda)
    self.__frame_counter = 0  # Contador para alternância das imagens de corrida
    self.__isRunning = False # Indica se o Mario está correndo
    
    self.platforms = platforms # Lista de plataformas no jogo
    
    # Carrega e redimensiona a imagem estática do Mario
    self.mario_surface = pygame.image.load(mario_live) 
    self.mario_surface = pygame.transform.scale(self.mario_surface, (45, 36)) 

  def movement(self): # Método para controlar o movimento
    keys = pygame.key.get_pressed()
    
    # Movimento horizontal
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
    
    # Inicia o pulo
    if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and not self.__isJumping:
      self.__isJumping = True
      self.__yVelocity = -self.__jumpSpeed
    
    self.applyGravity() # Aplica a gravidade ao Mario
      
  def drawMario(self, screen):
        # Atualiza o contador de frames para animação
        self.__frame_counter = (self.__frame_counter + 1) % 12  

        # Escolhe a imagem correta baseada no estado do Mario
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
        
        # Se estiver pulando, carrega a imagem de pulo
        if self.__isJumping:
            jump_surface = pygame.image.load(mario_jump)
            jump_surface = pygame.transform.scale(jump_surface, (45, 36))
            if self.__direction == 'L':
                jump_surface = pygame.transform.flip(jump_surface, True, False)
            self.mario_surface = jump_surface

        # Atualiza a posição do retângulo do Mario e desenha na tela
        self.mario_rect = self.mario_surface.get_rect(midbottom=(self.__posX, self.__posY))
        screen.blit(self.mario_surface, self.mario_rect)

      
  def applyGravity(self):
    # Aplica a gravidade ao Mario, ajustando sua posição vertical
    if self.__isJumping:
      self.__posY += self.__yVelocity
      self.__yVelocity += self.__gravity
      
    # Verifica colisões com plataformas para parar o pulo
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
     
  # Propriedades para acessar as variáveis privadas
  @property
  def posX(self):
    return self.__posX
  
  @property
  def posY(self):
    return self.__posY
  
  @property
  def gravity(self):
    return self.__gravity
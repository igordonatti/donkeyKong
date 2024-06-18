import pygame
from utils.constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        
        # Inicializa as variáveis de movimento do jogador
        self.y_change = 0
        self.x_speed = 3
        self.x_change = 0
        self.landed = False
        self.pos = 0
        self.dir = 1
        self.count = 0
        self.climbing = False
        
        # Define a imagem inicial do jogador
        self.image = STANDING
        self.hammer = False
        self.max_hammer = 450
        self.hammer_len = self.max_hammer
        self.hammer_pos = 1
        
        # Define a posição e a área de colisão do jogador
        self.rect = self.image.get_rect()
        self.hitbox = self.rect
        self.hammer_box = self.rect
        self.rect.center = (x_pos, y_pos)
        self.over_barrel = False
        
        # Define a área de colisão inferior do jogador
        self.bottom = pygame.rect.Rect(self.rect.left, self.rect.bottom - 20, self.rect.width, 20)

    def update(self, plats):
        self.landed = False
        # Verifica colisão com plataformas para determinar se o jogador está no chão
        for i in range(len(plats)):
            if self.bottom.colliderect(plats[i]):
                self.landed = True
                if not self.climbing:
                    self.rect.centery = plats[i].top - self.rect.height / 2 + 1
        # Aplica gravidade se o jogador não estiver no chão nem subindo escadas
        if not self.landed and not self.climbing:
            self.y_change += 0.25
        # Move o jogador
        self.rect.move_ip(self.x_change * self.x_speed, self.y_change)
        # Atualiza a área de colisão inferior do jogador
        self.bottom = pygame.rect.Rect(self.rect.left, self.rect.bottom - 20, self.rect.width, 20)
        # Atualiza a animação de movimento do jogador
        if self.x_change != 0 or (self.climbing and self.y_change != 0):
            if self.count < 3:
                self.count += 1
            else:
                self.count = 0
                if self.pos == 0:
                    self.pos += 1
                else:
                    self.pos = 0
        else:
            self.pos = 0
        # Atualiza o estado do martelo
        if self.hammer:
            self.hammer_pos = (self.hammer_len // 30) % 2
            self.hammer_len -= 1
            if self.hammer_len == 0:
                self.hammer = False
                self.hammer_len = self.max_hammer

    def draw(self, screen):
        # Define a imagem do jogador com base no estado atual (martelo, subindo, no chão, etc.)
        if not self.hammer:
            if not self.climbing and self.landed:
                if self.pos == 0:
                    self.image = STANDING
                else:
                    self.image = RUNNING
            if not self.landed and not self.climbing:
                self.image = JUMPING
            if self.climbing:
                if self.pos == 0:
                    self.image = CLIMBING1
                else:
                    self.image = CLIMBING2
        else:
            if self.hammer_pos == 0:
                self.image = HAMMER_JUMP
            else:
                self.image = HAMMER_OVERHEAD
        # Inverte a imagem do jogador se estiver virado para a esquerda
        if self.dir == -1:
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.image = self.image
        # Calcula a área de colisão do jogador
        self.calc_hitbox()
        # Desenha a imagem do jogador na tela
        if self.hammer_pos == 1 and self.hammer:
            screen.blit(self.image, (self.rect.left, self.rect.top - SECTION_HEIGHT))
        else:
            screen.blit(self.image, self.rect.topleft)

    def calc_hitbox(self):
        # Calcula a área de colisão do jogador com base no estado atual (com ou sem martelo)
        if not self.hammer:
            self.hitbox = pygame.rect.Rect((self.rect[0] + 15, self.rect[1] + 5), (self.rect[2] - 30, self.rect[3] - 10))
        elif self.hammer_pos == 0:
            if self.dir == 1:
                self.hitbox = pygame.rect.Rect((self.rect[0], self.rect[1] + 5), (self.rect[2] - 30, self.rect[3] - 10))
                self.hammer_box = pygame.rect.Rect((self.hitbox[0] + self.hitbox[2], self.rect[1] + 5), (self.hitbox[2], self.rect[3] - 10))
            else:
                self.hitbox = pygame.rect.Rect((self.rect[0] + 40, self.rect[1] + 5), (self.rect[2] - 30, self.rect[3] - 10))
                self.hammer_box = pygame.rect.Rect((self.hitbox[0] - self.hitbox[2], self.rect[1] + 5), (self.hitbox[2], self.rect[3] - 10))
        else:
            self.hitbox = pygame.rect.Rect((self.rect[0] + 15, self.rect[1] + 5), (self.rect[2] - 30, self.rect[3] - 10))
            self.hammer_box = pygame.rect.Rect((self.hitbox[0], self.hitbox[1] - SECTION_HEIGHT), (self.hitbox[2], SECTION_HEIGHT))

import pygame
import random
from utils.constants import *

class Barrel(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        # Define a imagem do barril e sua posição inicial
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        # Inicializa variáveis para movimento e estado
        self.y_change = 0
        self.x_change = 1
        self.pos = 0  # Posição para animação
        self.count = 0  # Contador para controle de animação
        self.oil_collision = False  # Flag para colisão com óleo
        self.falling = False  # Flag para queda
        self.check_lad = False  # Flag para verificar escadas
        self.bottom = self.rect  # Parte inferior do barril para detecção de colisão

    def update(self, fire_trig, plats, oil_drum):
        # Aplica gravidade ao barril se não estiver caindo
        if self.y_change < 8 and not self.falling:
            self.y_change += 2
        # Verifica colisão com plataformas para parar a queda
        for i in range(len(plats)):
            if self.bottom.colliderect(plats[i]):
                self.y_change = 0
                self.falling = False
        # Verifica colisão com o tambor de óleo e possivelmente ativa fogo
        if self.rect.colliderect(oil_drum):
            if not self.oil_collision:
                self.oil_collision = True
                if random.randint(0, 4) == 4:
                    fire_trig = True
        # Altera a direção do movimento horizontal baseado na posição vertical
        if not self.falling:
            if ROW5_TOP >= self.rect.bottom or ROW3_TOP >= self.rect.bottom >= ROW4_TOP or ROW1_TOP > self.rect.bottom >= ROW2_TOP:
                self.x_change = 3
            else:
                self.x_change = -3
        else:
            self.x_change = 0
        # Move o barril
        self.rect.move_ip(self.x_change, self.y_change)
        # Remove o barril se sair da tela
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
        # Controle de animação do barril
        if self.count < 15:
            self.count += 1
        else:
            self.count = 0
            if self.x_change > 0:
                if self.pos < 3:
                    self.pos += 1
                else:
                    self.pos = 0
            else:
                if self.pos > 0:
                    self.pos -= 1
                else:
                    self.pos = 3
        # Atualiza a parte inferior do barril para detecção de colisão
        self.bottom = pygame.rect.Rect((self.rect[0], self.rect.bottom), (self.rect[2], 3))
        return fire_trig

    def check_fall(self, lads):
        # Verifica se o barril deve cair por uma escada
        already_collided = False
        below = pygame.rect.Rect((self.rect[0], self.rect[1] + SECTION_HEIGHT), (self.rect[2], SECTION_HEIGHT))
        for lad in lads:
            if below.colliderect(lad) and not self.falling and not self.check_lad:
                self.check_lad = True
                already_collided = True
                if random.randint(0, 60) == 60:
                    self.falling = True
                    self.y_change = 4
        if not already_collided:
            self.check_lad = False

    def draw(self, screen):
        # Desenha o barril na tela, rotacionando com base na posição para animação
        screen.blit(pygame.transform.rotate(BARREL_IMG, 90 * self.pos), self.rect.topleft)
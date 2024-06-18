# Importa as bibliotecas necessárias
import pygame
import random
from utils.constants import *  # Importa constantes definidas em outro arquivo

class Flame(pygame.sprite.Sprite):  # Define a classe Flame, que herda de pygame.sprite.Sprite
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)  # Inicializa a classe base
        self.image = FIREBALL  # Define a imagem inicial da chama
        self.rect = self.image.get_rect()  # Obtém o retângulo que representa a imagem
        self.rect.center = (x_pos, y_pos)  # Define a posição inicial da chama
        # Inicializa variáveis para controle de movimento e animação
        self.pos = 1
        self.count = 0
        self.x_count = 0
        self.x_change = 2
        self.x_max = 4
        self.y_change = 0
        self.row = 1
        self.check_lad = False  # Flag para verificar escadas
        self.climbing = False  # Flag para indicar se está subindo uma escada

    def update(self, plats):
        # Aplica gravidade suave se não estiver subindo
        if self.y_change < 3 and not self.climbing:
            self.y_change += 0.25
        # Verifica colisão com plataformas para simular pulo
        for i in range(len(plats)):
            if self.rect.colliderect(plats[i]):
                self.climbing = False
                self.y_change = -4
        # Controla a animação e movimento horizontal
        if self.count < 15:
            self.count += 1
        else:
            self.count = 0
            self.pos *= -1  # Alterna a direção da animação
            if self.x_count < self.x_max:
                self.x_count += 1
            else:
                # Alterna a direção do movimento e ajusta a distância máxima de movimento
                self.x_count = 0
                self.x_change *= -1
                if self.x_change > 0:
                    self.x_max = random.randint(3, 6) if self.row in [1, 3, 5] else random.randint(6, 10)
                else:
                    self.x_max = random.randint(6, 10) if self.row in [1, 3, 5] else random.randint(3, 6)
        # Atualiza a imagem com base na direção do movimento
        if self.pos == 1:
            self.image = FIREBALL if self.x_change > 0 else pygame.transform.flip(FIREBALL, True, False)
        else:
            self.image = FIREBALL2 if self.x_change > 0 else pygame.transform.flip(FIREBALL2, True, False)
        # Move a chama
        self.rect.move_ip(self.x_change, self.y_change)
        # Remove a chama se sair da tela
        if self.rect.top > SCREEN_HEIGHT or self.rect.top < 0:
            self.kill()

    def check_climb(self, lads):
        # Verifica se a chama deve subir uma escada
        already_collided = False
        for lad in lads:
            if self.rect.colliderect(lad) and not self.climbing and not self.check_lad:
                self.check_lad = True
                already_collided = True
                if random.randint(0, 120) == 120:
                    self.climbing = True
                    self.y_change = -4
        if not already_collided:
            self.check_lad = False
        # Atualiza a linha atual com base na posição vertical
        if self.rect.bottom < ROW6_Y:
            self.row = 6
        elif self.rect.bottom < ROW5_Y:
            self.row = 5
        elif self.rect.bottom < ROW4_Y:
            self.row = 4
        elif self.rect.bottom < ROW3_Y:
            self.row = 3
        elif self.rect.bottom < ROW2_Y:
            self.row = 2
        else:
            self.row = 1
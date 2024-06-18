# Importa a biblioteca pygame e constantes definidas em outro arquivo
import pygame
from utils.constants import *

# Define a classe Hammer, que herda de pygame.sprite.Sprite
class Hammer(pygame.sprite.Sprite):
    # Método construtor da classe
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)  # Inicializa a classe base
        self.image = HAMMER  # Define a imagem do martelo usando uma constante
        self.rect = self.image.get_rect()  # Obtém o retângulo que representa a imagem
        self.rect.top = y_pos  # Define a posição vertical do martelo
        self.rect.left = x_pos * SECTION_WIDTH  # Define a posição horizontal do martelo
        self.used = False  # Flag para verificar se o martelo já foi usado

    # Método para desenhar o martelo na tela e verificar colisão com o jogador
    def draw(self, screen, player):
        if not self.used:  # Se o martelo não foi usado
            screen.blit(self.image, (self.rect[0], self.rect[1]))  # Desenha o martelo na tela
            # Verifica se o retângulo do martelo colide com a hitbox do jogador
            if self.rect.colliderect(player.hitbox):
                self.kill()  # Remove o martelo do grupo de sprites
                player.hammer = True  # Ativa o estado de martelo do jogador
                player.hammer_len = player.max_hammer  # Define a duração do martelo para o jogador
                self.used = True  # Marca o martelo como usado
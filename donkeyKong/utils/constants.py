import pygame

# Inicialização das constantes
pygame.init()  # Inicializa o Pygame
info = pygame.display.Info()  # Obtém informações da tela
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h  # Largura e altura da tela
WINDOW_WIDTH, WINDOW_HEIGHT = SCREEN_WIDTH - 800, SCREEN_HEIGHT - 150  # Dimensões da janela do jogo
SECTION_WIDTH = WINDOW_WIDTH // 32  # Largura de cada seção
SECTION_HEIGHT = WINDOW_HEIGHT // 32  # Altura de cada seção
SLOPE = SECTION_HEIGHT // 8  # Inclinação para as plataformas

FPS = 60  # Frames por segundo
BARREL_SPAWN_TIME = 360  # Tempo de spawn dos barris

# Carregando os recursos
BARREL_IMG = pygame.transform.scale(pygame.image.load('assets/images/barrels/barrel.png'), (SECTION_WIDTH * 1.5, SECTION_HEIGHT * 2))
FLAMES_IMG = pygame.transform.scale(pygame.image.load('assets/images/fire.png'), (SECTION_WIDTH * 2, SECTION_HEIGHT))
BARREL_SIDE = pygame.transform.scale(pygame.image.load('assets/images/barrels/barrel2.png'), (SECTION_WIDTH * 2, SECTION_HEIGHT * 2.5))
DK1 = pygame.transform.scale(pygame.image.load('assets/images/dk/dk1.png'), (SECTION_WIDTH * 5, SECTION_HEIGHT * 5))
DK2 = pygame.transform.scale(pygame.image.load('assets/images/dk/dk2.png'), (SECTION_WIDTH * 5, SECTION_HEIGHT * 5))
DK3 = pygame.transform.scale(pygame.image.load('assets/images/dk/dk3.png'), (SECTION_WIDTH * 5, SECTION_HEIGHT * 5))
PEACH1 = pygame.transform.scale(pygame.image.load('assets/images/peach/peach1.png'), (2 * SECTION_WIDTH, 3 * SECTION_HEIGHT))
PEACH2 = pygame.transform.scale(pygame.image.load('assets/images/peach/peach2.png'), (2 * SECTION_WIDTH, 3 * SECTION_HEIGHT))
FIREBALL = pygame.transform.scale(pygame.image.load('assets/images/fireball.png'), (1.5 * SECTION_WIDTH, 2 * SECTION_HEIGHT))
FIREBALL2 = pygame.transform.scale(pygame.image.load('assets/images/fireball2.png'), (1.5 * SECTION_WIDTH, 2 * SECTION_HEIGHT))
HAMMER = pygame.transform.scale(pygame.image.load('assets/images/hammer.png'), (2 * SECTION_WIDTH, 2 * SECTION_HEIGHT))
STANDING = pygame.transform.scale(pygame.image.load('assets/images/mario/standing.png'), (2 * SECTION_WIDTH, 2.5 * SECTION_HEIGHT))
JUMPING = pygame.transform.scale(pygame.image.load('assets/images/mario/jumping.png'), (2 * SECTION_WIDTH, 2.5 * SECTION_HEIGHT))
RUNNING = pygame.transform.scale(pygame.image.load('assets/images/mario/running.png'), (2 * SECTION_WIDTH, 2.5 * SECTION_HEIGHT))
CLIMBING1 = pygame.transform.scale(pygame.image.load('assets/images/mario/climbing1.png'), (2 * SECTION_WIDTH, 2.5 * SECTION_HEIGHT))
CLIMBING2 = pygame.transform.scale(pygame.image.load('assets/images/mario/climbing2.png'), (2 * SECTION_WIDTH, 2.5 * SECTION_HEIGHT))
HAMMER_STAND = pygame.transform.scale(pygame.image.load('assets/images/mario/hammer_stand.png'), (2.5 * SECTION_WIDTH, 2.5 * SECTION_HEIGHT))
HAMMER_JUMP = pygame.transform.scale(pygame.image.load('assets/images/mario/hammer_jump.png'), (2.5 * SECTION_WIDTH, 2.5 * SECTION_HEIGHT))
HAMMER_OVERHEAD = pygame.transform.scale(pygame.image.load('assets/images/mario/hammer_overhead.png'), (2.5 * SECTION_WIDTH, 3.5 * SECTION_HEIGHT))

# Carregando as fontes
FONT = pygame.font.Font('assets/fonts/Nintendo-DS-BIOS.TTF', 50)
FONT2 = pygame.font.Font('assets/fonts/ARCADECLASSIC.TTF', 30)

# Definindo coordenadas y para as linhas do jogo
START_Y = WINDOW_HEIGHT - 2 * SECTION_HEIGHT
ROW2_Y = START_Y - 4 * SECTION_HEIGHT
ROW3_Y = ROW2_Y - 7 * SLOPE - 3 * SECTION_HEIGHT
ROW4_Y = ROW3_Y - 4 * SECTION_HEIGHT
ROW5_Y = ROW4_Y - 7 * SLOPE - 3 * SECTION_HEIGHT
ROW6_Y = ROW5_Y - 4 * SECTION_HEIGHT
ROW6_TOP = ROW6_Y - 4 * SLOPE
ROW5_TOP = ROW5_Y - 8 * SLOPE
ROW4_TOP = ROW4_Y - 8 * SLOPE
ROW3_TOP = ROW3_Y - 8 * SLOPE
ROW2_TOP = ROW2_Y - 8 * SLOPE
ROW1_TOP = START_Y - 5 * SLOPE

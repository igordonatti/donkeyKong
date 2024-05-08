from donkeyKong import game

# screen = pygame.display.set_mode((500, 700))
# clock = pygame.time.Clock()

# mario_surf = pygame.image.load('assets/shapes/pngs/mario_static.png').convert_alpha()
# mario_surf = pygame.transform.scale(mario_surf, (45, 36))
# # ajuda na hora que tiver os mapas construidos pois consiguiremos "colar"
# # o mario no chao ja que saberemos onde estarao as plataformas.
# player_rect = mario_surf.get_rect(topleft = (0, 600))


if __name__ == '__main__':
  '''inicialização do jogo'''
  
  # normal run
  game.DonkeyKong()
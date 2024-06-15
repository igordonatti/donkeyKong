# Importa a classe Game do pacote donkeyKong.gameConfig
from donkeyKong.gameConfig.game import Game
# Importa a classe App do pacote donkeyKong.gameConfig.Menu
from donkeyKong.gameConfig.Menu.App import App

# As seguintes linhas estão comentadas e parecem ser parte de um teste inicial para configurar a tela e carregar uma imagem de Mario.
# screen = pygame.display.set_mode((500, 700))
# clock = pygame.time.Clock()

# mario_surf = pygame.image.load('assets/shapes/pngs/mario_static.png').convert_alpha()
# mario_surf = pygame.transform.scale(mario_surf, (45, 36))
# player_rect = mario_surf.get_rect(topleft = (0, 600))
# Estas linhas carregam uma imagem estática de Mario, ajustam seu tamanho e definem sua posição inicial.

# Verifica se este script é o ponto de entrada principal do programa.
if __name__ == '__main__':
  # Bloco de código para inicializar o jogo.
  
  # Cria uma instância do jogo.
  game = Game()
  # Cria uma instância do menu e passa a função start_game do jogo como callback para ser chamada quando o jogo for iniciado a partir do menu.
  game.menu = App(game.start_game)
  # Inicia o loop principal do menu, aguardando ações do usuário.
  game.menu.mainloop()
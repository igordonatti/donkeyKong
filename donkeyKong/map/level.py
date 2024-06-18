from map.bridge import Bridge
from map.ladder import Ladder

class Level:
    def __init__(self, level_data):
        # Inicializa os dados do nível
        self.level_data = level_data

    def create_level(self, screen):
        platforms = []  # Lista para armazenar as plataformas desenhadas
        climbers = []  # Lista para armazenar as áreas de colisão das escadas
        ladder_objs = []  # Lista para armazenar os objetos Ladder
        bridge_objs = []  # Lista para armazenar os objetos Bridge

        # Obtém as listas de escadas e pontes dos dados do nível
        ladders = self.level_data['ladders']
        bridges = self.level_data['bridges']

        # Cria e desenha as escadas
        for ladder in ladders:
            ladder_obj = Ladder(*ladder)  # Cria um objeto Ladder com os dados fornecidos
            ladder_obj.draw(screen)  # Desenha a escada na tela
            ladder_objs.append(ladder_obj)  # Adiciona a escada à lista de objetos Ladder
            if ladder[2] >= 3:  # Se a escada tiver 3 ou mais degraus
                climbers.append(ladder_objs[-1].body)  # Adiciona a área de colisão da escada à lista de áreas de colisão

        # Cria e desenha as pontes
        for bridge in bridges:
            bridge_obj = Bridge(*bridge)  # Cria um objeto Bridge com os dados fornecidos
            bridge_obj.draw(screen)  # Desenha a ponte na tela
            bridge_objs.append(bridge_obj)  # Adiciona a ponte à lista de objetos Bridge
            platforms.append(bridge_objs[-1].top)  # Adiciona a área de colisão da ponte à lista de plataformas

        # Retorna as listas de plataformas e áreas de colisão das escadas
        return platforms, climbers

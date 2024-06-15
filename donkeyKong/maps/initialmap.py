from ..sprites.ladder import Ladder
from ..sprites.bridge import Bridge

# Definição da classe InitialMap.
class InitialMap():
    # Método construtor da classe, inicializa uma instância de InitialMap.
    def __init__(self, screen, section_width, section_height, slope):
        # Atribuição dos parâmetros do construtor às variáveis de instância.
        self.screen = screen
        self.section_width = section_width
        self.section_height = section_height
        self.slope = slope
        
        # Inicialização de listas para armazenar objetos de pontes, plataformas, escadas e corpos de escada.
        self.bridge_objs = []
        self.platforms = []
        self.climbers = []
        self.ladder_objs = []
        
        # Criação dos níveis do jogo, pontes e escadas.
        self.levels = self.create_levels()
        self.create_bridges() 
        self.create_ladders()

    # Método para criar os níveis do jogo, definindo a posição das pontes e escadas.
    def create_levels(self):
        # Cálculo das posições iniciais para cada linha de pontes e escadas.
        start_y = self.screen.get_height() - 2 * self.section_height
        row2_y = start_y - 4 * self.section_height
        row3_y = row2_y - 7 * self.slope - 3 * self.section_height
        row4_y = row3_y - 4 * self.section_height
        row5_y = row4_y - 7 * self.slope - 3 * self.section_height
        row6_y = row5_y - 4 * self.section_height
        # Retorna uma lista de dicionários contendo as posições das pontes e escadas.
        return [{'bridges': [
            (1, start_y, 15), 
            (16, start_y - self.slope, 3),
            (19, start_y - 2 * self.slope, 3),
            (22, start_y - 3 * self.slope, 3),
            (25, start_y - 4 * self.slope, 3),
            (28, start_y - 5 * self.slope, 3),
            (25, row2_y, 3),
            (22, row2_y - self.slope, 3),
            (19, row2_y - 2 * self.slope, 3),
            (16, row2_y - 3 * self.slope, 3),
            (13, row2_y - 4 * self.slope, 3),
            (10, row2_y - 5 * self.slope, 3),
            (7, row2_y - 6 * self.slope, 3),
            (4, row2_y - 7 * self.slope, 3),
            (2, row2_y - 8 * self.slope, 2),
            (4, row3_y, 3),
            (7, row3_y - self.slope, 3),
            (10, row3_y - 2 * self.slope, 3),
            (13, row3_y - 3 * self.slope, 3),
            (16, row3_y - 4 * self.slope, 3),
            (19, row3_y - 5 * self.slope, 3),
            (22, row3_y - 6 * self.slope, 3),
            (25, row3_y - 7 * self.slope, 3),
            (28, row3_y - 8 * self.slope, 2),
            (25, row4_y, 3),
            (22, row4_y - self.slope, 3),
            (19, row4_y - 2 * self.slope, 3),
            (16, row4_y - 3 * self.slope, 3),
            (13, row4_y - 4 * self.slope, 3),
            (10, row4_y - 5 * self.slope, 3),
            (7, row4_y - 6 * self.slope, 3),
            (4, row4_y - 7 * self.slope, 3),
            (2, row4_y - 8 * self.slope, 2),
            (4, row5_y, 3),
            (7, row5_y - self.slope, 3),
            (10, row5_y - 2 * self.slope, 3),
            (13, row5_y - 3 * self.slope, 3),
            (16, row5_y - 4 * self.slope, 3),
            (19, row5_y - 5 * self.slope, 3),
            (22, row5_y - 6 * self.slope, 3),
            (25, row5_y - 7 * self.slope, 3),
            (28, row5_y - 8 * self.slope, 2),
            (25, row6_y, 3),
            (22, row6_y - self.slope, 3),
            (19, row6_y - 2 * self.slope, 3),
            (16, row6_y - 3 * self.slope, 3),
            (2, row6_y - 4 * self.slope, 14),
            (13, row6_y - 4 * self.section_height, 6),
            (10, row6_y - 3 * self.section_height, 3),
        ],
        'ladders': [(12, row2_y + 6 * self.slope, 2), (12, row2_y + 26 * self.slope, 2),
                       (25, row2_y + 11 * self.slope, 4), (6, row3_y + 11 * self.slope, 3),
                       (14, row3_y + 8 * self.slope, 4), (10, row4_y + 6 * self.slope, 1),
                       (10, row4_y + 24 * self.slope, 2), (16, row4_y + 6 * self.slope, 5),
                       (25, row4_y + 9 * self.slope, 4), (6, row5_y + 11 * self.slope, 3),
                       (11, row5_y + 8 * self.slope, 4), (23, row5_y + 4 * self.slope, 1),
                       (23, row5_y + 24 * self.slope, 2), (25, row6_y + 9 * self.slope, 4),
                       (13, row6_y + 5 * self.slope, 2), (13, row6_y + 25 * self.slope, 2),
                       (18, row6_y - 27 * self.slope, 4), (12, row6_y - 17 * self.slope, 2),
                       (10, row6_y - 17 * self.slope, 2), (12, -5, 13), (10, -5, 13)]
        }]

    # Método para criar objetos de ponte a partir das informações dos níveis.
    def create_bridges(self):
        bridges = self.levels[0]['bridges']
        for bridge in bridges:
            x, y, length = bridge
            # Criação de um novo objeto Bridge e adição às listas de objetos de ponte e plataformas.
            new_bridge = Bridge(x * self.section_width, y, length, self.section_width, self.section_height)
            self.bridge_objs.append(new_bridge)
            self.platforms.append(new_bridge.top)

    # Método para criar objetos de escada a partir das informações dos níveis.
    def create_ladders(self):
        ladders = self.levels[0]['ladders']
        for ladder in ladders:
            x, y, length = ladder
            # Criação de um novo objeto Ladder e adição às listas de objetos de escada e corpos de escada.
            new_ladder = Ladder(x * self.section_width, y, length, self.section_width, self.section_height)
            self.ladder_objs.append(new_ladder)
            if length >= 3:
                self.climbers.append(new_ladder.body)

    # Método para desenhar as pontes e escadas na tela.
    def draw(self):
        for bridge in self.bridge_objs:
            bridge.draw(self.screen)
        for ladder in self.ladder_objs:
            ladder.draw(self.screen)

    # Método para obter a posição inicial de Mario no jogo.
    def get_initial_mario_position(self):
        first_bridge = self.levels[0]['bridges'][0]
        x, y, _ = first_bridge
        return x * self.section_width, y

        
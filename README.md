# Releitura de Donkey Kong

## Introdução
Este repositório contém uma releitura do jogo Donkey Kong, desenvolvido originalmente pela Nintendo em 1981. O projeto foi criado como parte da avaliação para a matéria de Tópicos Avançados em Computação II, utilizando a linguagem Python e a biblioteca Pygame.

## Autores
- Igor Donatti
- João Vitor Moitinho

## Bibliotecas Utilizadas
- **Pygame**: Usada para criar a interface gráfica e controlar a lógica de interação do jogo.
- **CustomTkinter**: Utilizada para criar menus e interfaces gráficas personalizadas.
- **OS**: Usada para gerenciar funções do sistema operacional, como caminhos de arquivos.

## Como Clonar o Repositório
Para clonar este projeto, execute o seguinte comando no terminal:
```bash
git clone https://github.com/igordonatti/donkeyKong.git
cd donkeyKong
```

## Estrutura do Projeto

donkeyKong/
│
├── assets/                 # Recursos gráficos e sonoros.
│   ├── fonts/              # Fontes usadas no jogo.
│   ├── shapes/             # Arquivos SVG de elementos gráficos.
│   ├── sounds/             # Arquivos de som.
│
├── donkeyKong/             # Código fonte do jogo.
│   ├── gameConfig/         # Configurações centrais do jogo, incluindo a inicialização.
│   │   ├── Menu/           # Menu do jogo.
│   ├── maps/               # Mapas e layouts de níveis.
│   ├── sprites/            # Sprites do jogo, incluindo personagens e objetos.
│
├── main.py                 # Script principal para iniciar o jogo.
├── README.md               # Documentação do projeto.

## Explicação dos Arquivos
main.py: Script principal que executa o jogo.
gameConfig/game.py: Contém a lógica principal do jogo, incluindo inicialização e gerenciamento de estados.
gameConfig/display.py: Gerencia a configuração de exibição, como resolução e tela cheia.
gameConfig/Menu/App.py: Gerencia o menu do jogo.
maps/initialmap.py: Define o layout inicial do mapa do jogo.
sprites/mario.py, sprites/ladder.py, sprites/bridge.py: Definem os sprites e suas interações no jogo.


## Como Executar
Instale as dependências necessárias e execute o jogo com os comandos:

```bash
pip install pygame customtkinter
python main.py
```
## Licença
Este projeto é distribuído sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## Agradecimentos
Agradecemos ao professor e colegas pela orientação e apoio durante o desenvolvimento deste projeto.
# Releitura de Donkey Kong

## Introdução
Este repositório contém uma releitura do jogo Donkey Kong, desenvolvido originalmente pela Nintendo em 1981. O projeto foi criado como parte da avaliação para a matéria de Tópicos Avançados em Computação II, utilizando a linguagem Python e a biblioteca Pygame.

## Autores
- Igor Donatti
- João Vitor Moitinho

## Bibliotecas Utilizadas
- **Pygame**: Usada para criar a interface gráfica e controlar a lógica de interação do jogo.

## Como Clonar o Repositório
Para clonar este projeto, execute o seguinte comando no terminal:
```bash
git clone https://github.com/igordonatti/donkeyKong.git
cd donkeyKong
```

## Estrutura do Projeto



├── assets/                 # Recursos gráficos e sonoros.
│   ├── fonts/              # Fontes usadas no jogo.
│   ├── images/             # Imagens dos elementos gráficos do jogo.
│   ├── shapes/             # Svgs dos elementos gráficos do jogo.
│   ├── sounds/             # Sons do jogo.

donkeyKong/
    ├── game/                   # Código fonte do jogo.
    │   ├── __init__.py         # Inicialização do pacote game.
    │   ├── main.py             # Lógica principal do jogo, incluindo inicialização e gerenciamento de estados.
    │   ├── player.py           # Lógica e interações do jogador.
    │   ├── barrel.py           # Lógica e interações dos barris.
    │   ├── flame.py            # Lógica e interações das chamas.
    │   ├── hammer.py           # Lógica e interações do martelo.
    │
    ├── map/                    # Mapas e layouts de níveis.
    │   ├── level.py            # Lógica para a criação e gerenciamento dos níveis.
    │   ├── ladder.py           # Lógica e desenho das escadas.
    │   ├── bridge.py           # Lógica e desenho das pontes.
    │
    ├── utils/                  # Utilitários e constantes.
    │   ├── __init__.py         # Inicialização do pacote utils.
    │   ├── constants.py        # Definição das constantes usadas no jogo.
    │
    ├── main.py                 # Script principal para iniciar o jogo.
    ├── menu.py                 # Lógica e interações do menu principal do jogo.
    ├── README.md               # Você está aqui =D


## Documentação do projeto.

Explicação dos Arquivos

```bash
main.py: Script principal que executa o jogo.
game/main.py: Contém a lógica principal do jogo, incluindo inicialização e gerenciamento de estados.
game/player.py: Contém a lógica e interações do jogador.
game/barrel.py: Contém a lógica e interações dos barris.
game/flame.py: Contém a lógica e interações das chamas.
game/hammer.py: Contém a lógica e interações do martelo.
map/level.py: Define a lógica para a criação e gerenciamento dos níveis.
map/ladder.py: Define a lógica e desenho das escadas.
map/bridge.py: Define a lógica e desenho das pontes.
utils/constants.py: Define as constantes usadas no jogo.
menu.py: Gerencia o menu principal do jogo.
```
## Como Executar
Instale as dependências necessárias e execute o jogo com os comandos:

```bash
Copiar código
pip install pygame
python main.py
```
## Licença
Este projeto é distribuído sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## Créditos
Este projeto foi inspirado e baseado no PythonDonkeyKong de plemaster01. Agradecemos pela disponibilização do código e pela inspiração fornecida.

## Agradecimentos
Agradecemos ao professor e colegas pela orientação e apoio durante o desenvolvimento deste projeto.
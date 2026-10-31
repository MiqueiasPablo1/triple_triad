"""Classes do jogo (paradigma orientado a objetos): Carta, Jogador e Tabuleiro."""


class Carta:
    def __init__(self, nome, cima, direita, baixo, esquerda):
        self.nome = nome
        self.lados = (cima, direita, baixo, esquerda)
        self.dono = None

    def capturar(self, novo_dono):
        """Troca o dono da carta: quem perde tira 1 ponto e quem ganha soma 1."""
        self.dono.pontos -= 1
        novo_dono.pontos += 1
        self.dono = novo_dono


class Jogador:
    def __init__(self, numero):
        self.numero = numero
        self.nome = f"Jogador {numero}"
        self.mao = []
        self.pontos = 5

    def receber(self, carta):
        carta.dono = self
        self.mao.append(carta)

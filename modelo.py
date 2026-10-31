"""Classes do jogo (paradigma orientado a objetos): Carta, Jogador e Tabuleiro."""

# deslocamento (linha, coluna) de cada lado da carta: cima, direita, baixo, esquerda
DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)]


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


class Tabuleiro:
    def __init__(self):
        self.celulas = [None] * 9  # posições 0 a 8, linha por linha

    def livres(self):
        return [p for p, carta in enumerate(self.celulas) if carta is None]

    def vizinhos(self, pos):
        """Gera (lado, posição) de cada casa vizinha que já tem carta."""
        linha, coluna = divmod(pos, 3)
        for lado, (dl, dc) in enumerate(DIRECOES):
            nl, nc = linha + dl, coluna + dc
            if 0 <= nl < 3 and 0 <= nc < 3 and self.celulas[3 * nl + nc] is not None:
                yield lado, 3 * nl + nc

    def colocar(self, carta, pos):
        """Coloca a carta e captura os vizinhos inimigos com lado menor. Devolve quantas capturou."""
        self.celulas[pos] = carta
        capturadas = 0
        for lado, q in self.vizinhos(pos):
            alvo = self.celulas[q]
            oposto = (lado + 2) % 4  # lado da carta vizinha que encosta nesta
            if alvo.dono is not carta.dono and carta.lados[lado] > alvo.lados[oposto]:
                alvo.capturar(carta.dono)
                capturadas += 1
        return capturadas

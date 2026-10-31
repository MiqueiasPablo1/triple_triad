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

    def colocar(self, carta, pos, combo=False):
        """Coloca a carta e captura os vizinhos inimigos com lado menor.

        Com combo, cada carta capturada também ataca os seus vizinhos (reação em cadeia).
        Devolve (capturas feitas pela carta jogada, capturas feitas em cadeia).
        """
        self.celulas[pos] = carta
        fila, diretas, em_cadeia = [pos], 0, 0
        while fila:
            p = fila.pop(0)
            atacante = self.celulas[p]
            for lado, q in self.vizinhos(p):
                alvo = self.celulas[q]
                oposto = (lado + 2) % 4  # lado da carta vizinha que encosta nesta
                if alvo.dono is not atacante.dono and atacante.lados[lado] > alvo.lados[oposto]:
                    alvo.capturar(atacante.dono)
                    if p == pos:
                        diretas += 1
                    else:
                        em_cadeia += 1
                    if combo:
                        fila.append(q)
        return diretas, em_cadeia

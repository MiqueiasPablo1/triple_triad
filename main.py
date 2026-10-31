"""Triple Triad no terminal. Aqui fica o fluxo do jogo (paradigma procedural)."""
import random

from cartas import CARTAS
from modelo import Carta, Jogador, Tabuleiro
from tela import limpar_tela, mostrar_mao, mostrar_tabuleiro, perguntar

REGRAS = set()  # regras extras ativas


def distribuir(jogadores):
    """Sorteia 5 cartas diferentes para cada jogador."""
    sorteadas = random.sample(CARTAS, 10)
    for k, jogador in enumerate(jogadores):
        for dados in sorteadas[5 * k:5 * k + 5]:
            jogador.receber(Carta(*dados))


def jogar_turno(jogador, tab):
    """Mostra a mão, lê a jogada e a aplica no tabuleiro. Devolve o texto da jogada."""
    mostrar_mao(jogador)
    i = perguntar("Escolha a carta: ", range(1, len(jogador.mao) + 1)) - 1
    pos = perguntar("Escolha a casa: ", [p + 1 for p in tab.livres()]) - 1
    carta = jogador.mao.pop(i)
    capturadas = tab.colocar(carta, pos)
    return f"{jogador.nome} jogou {carta.nome} na casa {pos + 1} e capturou {capturadas} carta(s)."


def partida(jogadores):
    """Joga os 9 turnos. A tela é limpa a cada jogada para a mão do anterior não ficar visível."""
    tab = Tabuleiro()
    atual = random.randrange(2)  # sorteio de quem começa
    aviso = f"{jogadores[atual].nome} começa."
    for _ in range(9):
        jogador = jogadores[atual]
        limpar_tela()
        mostrar_tabuleiro(tab)
        print(aviso)
        input(f"Vez do {jogador.nome}. Pressione Enter para continuar...")
        aviso = jogar_turno(jogador, tab)
        atual = 1 - atual
    limpar_tela()
    mostrar_tabuleiro(tab)
    print(aviso)
    return tab


def main():
    jogadores = [Jogador(1), Jogador(2)]
    j1, j2 = jogadores
    limpar_tela()
    print("=== TRIPLE TRIAD ===")
    print("Regras extras:", ", ".join(sorted(REGRAS)) or "nenhuma")
    distribuir(jogadores)
    input("Pressione Enter para começar...")
    partida(jogadores)
    print(f"Placar: {j1.nome} {j1.pontos} x {j2.pontos} {j2.nome} (cartas no tabuleiro + mão)")
    if j1.pontos == j2.pontos:
        print("Empate!")
    else:
        print(f"{max(jogadores, key=lambda j: j.pontos).nome} venceu!")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nJogo encerrado.")

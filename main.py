"""Triple Triad no terminal. Aqui fica o fluxo do jogo (paradigma procedural)."""
import random

from cartas import CARTAS
from modelo import Carta, Jogador, Tabuleiro
from tela import limpar_tela, mostrar_mao, mostrar_tabuleiro, perguntar

REGRAS = {"Swap", "Order", "Combo", "Sudden Death"}  # regras extras ativas (para desativar uma, é só tirá-la do conjunto)


def distribuir(jogadores):
    """Sorteia 5 cartas diferentes para cada jogador."""
    sorteadas = random.sample(CARTAS, 10)
    for k, jogador in enumerate(jogadores):
        for dados in sorteadas[5 * k:5 * k + 5]:
            jogador.receber(Carta(*dados))


def trocar_cartas(j1, j2):
    """Regra Swap: cada jogador entrega uma carta sorteada da mão ao outro."""
    de_j1 = j1.mao.pop(random.randrange(len(j1.mao)))
    de_j2 = j2.mao.pop(random.randrange(len(j2.mao)))
    j1.receber(de_j2)
    j2.receber(de_j1)
    print(f"Swap: {j1.nome} entregou {de_j1.nome} e recebeu {de_j2.nome} do {j2.nome}.")


def jogar_turno(jogador, tab):
    """Mostra a mão, lê a jogada e a aplica no tabuleiro. Devolve o texto da jogada."""
    mostrar_mao(jogador)
    if "Order" in REGRAS:
        i = 0  # Order: só a primeira carta da mão pode ser jogada
        print(f"Regra Order: você joga a carta 1 ({jogador.mao[0].nome}).")
    else:
        i = perguntar("Escolha a carta: ", range(1, len(jogador.mao) + 1)) - 1
    pos = perguntar("Escolha a casa: ", [p + 1 for p in tab.livres()]) - 1
    carta = jogador.mao.pop(i)
    diretas, em_cadeia = tab.colocar(carta, pos, combo="Combo" in REGRAS)
    texto = f"{jogador.nome} jogou {carta.nome} na casa {pos + 1} e capturou {diretas} carta(s)"
    if em_cadeia:
        texto += f" + {em_cadeia} em combo"
    return texto + "."


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


def morte_subita(jogadores, tab):
    """Regra Sudden Death: cada jogador volta com as cartas que possui (tabuleiro + mão) e 5 pontos."""
    for jogador in jogadores:
        jogador.mao = [c for c in tab.celulas if c.dono is jogador] + jogador.mao
        jogador.pontos = 5


def main():
    jogadores = [Jogador(1), Jogador(2)]
    j1, j2 = jogadores
    limpar_tela()
    print("=== TRIPLE TRIAD ===")
    print("Regras extras:", ", ".join(sorted(REGRAS)) or "nenhuma")
    distribuir(jogadores)
    if "Swap" in REGRAS:
        trocar_cartas(j1, j2)
    input("Pressione Enter para começar...")
    while True:
        tab = partida(jogadores)
        print(f"Placar: {j1.nome} {j1.pontos} x {j2.pontos} {j2.nome} (cartas no tabuleiro + mão)")
        if j1.pontos != j2.pontos:
            print(f"{max(jogadores, key=lambda j: j.pontos).nome} venceu!")
            return
        if "Sudden Death" not in REGRAS:
            print("Empate!")
            return
        input("Empate! Sudden Death: nova partida com as cartas de cada um. Enter para continuar...")
        morte_subita(jogadores, tab)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nJogo encerrado.")

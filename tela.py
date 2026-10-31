"""Interface de texto (paradigma procedural): funções que desenham e leem no terminal."""
import os

os.system("")  # ativa as cores ANSI no terminal do Windows

RESET = "\033[0m"
COR = {1: "\033[94m", 2: "\033[92m"}  # Jogador 1 = azul, Jogador 2 = verde


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def perguntar(texto, validos):
    """Repete a pergunta até o jogador digitar um dos números válidos."""
    while True:
        resposta = input(texto).strip()
        if resposta.isdecimal() and int(resposta) in validos:
            return int(resposta)
        print("Opção inválida.")


def linha_carta(carta, i):
    """Linha i (0 a 2) da carta, com 8 colunas; casa vazia fica em branco."""
    if carta is None:
        return " " * 8
    cima, direita, baixo, esquerda = ["A" if v == 10 else str(v) for v in carta.lados]
    texto = [
        cima.center(8),
        f"{esquerda} J{carta.dono.numero} {direita}".center(8),
        baixo.center(8),
    ][i]
    return COR[carta.dono.numero] + texto + RESET


def desenhar_fileira(cartas, primeiro):
    """Desenha uma fileira de cartas; a borda de cima mostra o número de cada casa."""
    print("".join(f"+--[{primeiro + k}]---" for k in range(len(cartas))) + "+")
    for i in range(3):
        print("|" + "|".join(linha_carta(c, i) for c in cartas) + "|")


def fechar(n):
    print("+--------" * n + "+")


def mostrar_tabuleiro(tab):
    for linha in range(3):
        desenhar_fileira(tab.celulas[3 * linha:3 * linha + 3], 3 * linha + 1)
    fechar(3)


def mostrar_mao(jogador):
    print(f"Mão do {jogador.nome}:")
    desenhar_fileira(jogador.mao, 1)
    fechar(len(jogador.mao))
    print("  ".join(f"[{n}] {c.nome}" for n, c in enumerate(jogador.mao, 1)))

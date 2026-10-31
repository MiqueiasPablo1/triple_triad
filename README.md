# Triple Triad (terminal)

Versão em Python 3 do jogo de cartas Triple Triad, para dois jogadores no mesmo terminal. Não precisa instalar nada.

```bash
python main.py
```

## Como jogar

- Tabuleiro 3x3 e 5 cartas sorteadas para cada jogador. Cada carta tem 4 valores (cima, direita, baixo, esquerda); o 10 aparece como `A`.
- Na sua vez, escolha a casa livre (o número de cada casa aparece na borda de cima dela). Se um lado da sua carta for maior que o lado encostado de uma carta do adversário, você captura essa carta.
- Pontuação: cada jogador começa com 5 pontos; capturar uma carta dá +1 e perder uma tira 1. O jogo acaba com o tabuleiro cheio e vence quem tiver mais pontos.
  Os pontos contam as cartas do tabuleiro **mais a carta que sobra na mão de quem joga em segundo** (como no jogo original), por isso o placar pode ser 5 x 5 mesmo com 5 casas contra 4 no tabuleiro.
- As mãos ficam escondidas: a tela é limpa a cada jogada e o próximo jogador confirma com Enter antes de ver a própria mão.
- Cores: Jogador 1 azul, Jogador 2 verde (e `J1`/`J2` escrito no meio da carta).

## Regras extras escolhidas

| Regra | Como ficou |
| --- | --- |
| Swap | No início, cada jogador entrega ao outro uma carta sorteada da própria mão. |
| Order | Só dá para jogar a primeira carta da mão (o jogador escolhe apenas a casa). |
| Combo | Toda carta capturada também ataca as vizinhas (se o lado dela for maior), em cadeia. O jogo avisa quantas capturas vieram do combo. |
| Sudden Death | Se terminar empatado, nova partida com as cartas que cada jogador possui (tabuleiro + mão), até alguém vencer. |

Para desligar uma regra, tire o nome dela de `REGRAS` no `main.py`.

## Organização do código

| Arquivo | Paradigma | Conteúdo |
| --- | --- | --- |
| `modelo.py` | Orientado a objetos | Classes `Carta`, `Jogador` e `Tabuleiro`, cada uma com seu estado e comportamento (ex.: `Tabuleiro.colocar` faz a captura). |
| `tela.py` | Procedural | Funções que desenham o tabuleiro e a mão e leem as respostas. |
| `main.py` | Procedural | Fluxo da partida e regras extras (`partida`, `jogar_turno`, `trocar_cartas`, `morte_subita`). |
| `cartas.py` | Dados | As 15 cartas, com valores próprios. |

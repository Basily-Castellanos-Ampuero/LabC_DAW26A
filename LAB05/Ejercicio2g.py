from interpreter import draw
from chessPictures import *

# Ejercicio 2g: Tablero de ajedrez 8x8 vacío.
#
# Estrategia:
#   - fila_clara: empieza en casilla clara → patrón LDLDLDLD (L=light, D=dark)
#   - fila_oscura: empieza en casilla oscura → patrón DLDLDLDL
#   - Se alternan 4 veces para obtener el tablero completo de 8 filas.
#
# El rank 8 (top) comienza en casilla clara (a8 es clara en ajedrez estándar).

fila_clara  = square.join(square.negative()).horizontalRepeat(4)   # LDLDLDLD
fila_oscura = square.negative().join(square).horizontalRepeat(4)   # DLDLDLDL

# Construimos de abajo (rank 1) hacia arriba (rank 8).
# Rank 1 (display row 7): a1 es oscura → fila_oscura
board = fila_oscura
for rango in range(2, 9):
    # Filas pares (2,4,6,8) empiezan con casilla clara; impares (1,3,5,7) con oscura
    if rango % 2 == 0:
        board = board.up(fila_clara)
    else:
        board = board.up(fila_oscura)

draw(board)

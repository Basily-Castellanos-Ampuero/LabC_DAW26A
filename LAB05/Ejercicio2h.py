from interpreter import draw
from chessPictures import *

# ============================================================
# Ejercicio 2h – Apertura Italiana: 1.e4 e5 2.Cf3 Cc6 3.Ac4
# ============================================================
# Con 3.Ac4 las blancas desarrollan el alfil hacia c4 para presionar
# el peón de f7 y controlar el centro, con amenazas al flanco de rey.
#
# Estado del tablero después de 3.Ac4:
#   Rank 8: Ra8  --  Ac8  Dd8  Re8  Af8  Cg8  Rh8   (b8 vacío, Cc6 se movió)
#   Rank 7: pa7  pb7  pc7  pd7  ---  pf7  pg7  ph7   (e7 vacío, peón a e5)
#   Rank 6: ---  ---  Cc6  ---  ---  ---  ---  ---
#   Rank 5: ---  ---  ---  ---  pe5  ---  ---  ---
#   Rank 4: ---  ---  Ac4  ---  Pe4  ---  ---  ---   (alfil blanco c4, peón blanco e4)
#   Rank 3: ---  ---  ---  ---  ---  Cf3  ---  ---   (caballo blanco f3)
#   Rank 2: Pa2  Pb2  Pc2  Pd2  ---  Pf2  Pg2  Ph2   (e2 vacío, peón movido a e4)
#   Rank 1: Ra1  Cb1  Ac1  Dd1  Re1  ---  ---  Rh1   (f1 vacío Ac4, g1 vacío Cf3)
#
# Convención de colores:
#   Piezas blancas = pieza original
#   Piezas negras  = pieza.negative()
#   Casilla clara  = square               (i+j) % 2 == 0  →  a8(0,0) es clara ✓
#   Casilla oscura = square.negative()

# ── Alias cortos ────────────────────────────────────────────
W = True   # blanca
B = False  # negra

def celda(pieza, es_blanca, es_clara):
    """Retorna una Picture: fondo de casilla con la pieza encima (o vacía)."""
    fondo = square if es_clara else square.negative()
    if pieza is None:
        return fondo
    p = pieza if es_blanca else pieza.negative()
    return fondo.under(p)

def es_clara(display_row, col):
    """True si la casilla (display_row, col) es clara. a8 = (0,0) es clara."""
    return (display_row + col) % 2 == 0

# ── Definición del tablero ──────────────────────────────────
# board[display_row][col] = (pieza, es_blanca) o None
# display_row 0 = rank 8   display_row 7 = rank 1
# col 0 = archivo a        col 7 = archivo h

board_data = [
    # Rank 8 (display_row=0): Ra Nb Bc Qd Ke Bf Ng Rh
    [(rock,B),(None,B),(bishop,B),(queen,B),(king,B),(bishop,B),(knight,B),(rock,B)],
    # Rank 7 (display_row=1): pawns, e7 vacío
    [(pawn,B),(pawn,B),(pawn,B),(pawn,B), None,      (pawn,B),(pawn,B),(pawn,B)],
    # Rank 6 (display_row=2): Cc6
    [None,    None,    (knight,B),None,   None,      None,    None,    None   ],
    # Rank 5 (display_row=3): pe5
    [None,    None,    None,      None,   (pawn,B),  None,    None,    None   ],
    # Rank 4 (display_row=4): Ac4, Pe4
    [None,    None,    (bishop,W),None,   (pawn,W),  None,    None,    None   ],
    # Rank 3 (display_row=5): Cf3
    [None,    None,    None,      None,   None,      (knight,W),None,  None   ],
    # Rank 2 (display_row=6): pawns, e2 vacío
    [(pawn,W),(pawn,W),(pawn,W),(pawn,W), None,      (pawn,W),(pawn,W),(pawn,W)],
    # Rank 1 (display_row=7): Ra Cb Ac Dd Re -- -- Rh
    [(rock,W),(knight,W),(bishop,W),(queen,W),(king,W),None,  None,   (rock,W)],
]

# ── Construcción de la imagen ────────────────────────────────
def construir_fila(display_row):
    celdas = [
        celda(board_data[display_row][j][0] if board_data[display_row][j] else None,
              board_data[display_row][j][1] if board_data[display_row][j] else True,
              es_clara(display_row, j))
        for j in range(8)
    ]
    fila = celdas[0]
    for c in celdas[1:]:
        fila = fila.join(c)
    return fila

# Construir de abajo hacia arriba (rank 1 → rank 8)
imagen = construir_fila(7)
for i in range(6, -1, -1):
    imagen = imagen.up(construir_fila(i))

draw(imagen)

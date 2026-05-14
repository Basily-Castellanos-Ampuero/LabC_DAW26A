from interpreter import draw
from chessPictures import *

# ============================================================
# Ejercicio 2i – Apertura Escocesa: 1.e4 e5 2.Cf3 Cc6 3.d4
# ============================================================
# Con 3.d4 las blancas buscan abrir el centro y desafiar el control de las
# negras. Este movimiento permite un juego rápido y directo, abriendo
# líneas para las piezas blancas.
#
# Estado del tablero después de 3.d4:
#   Rank 8: Ra8  --   Ac8  Dd8  Re8  Af8  Cg8  Rh8   (b8 vacío, Cc6 se movió)
#   Rank 7: pa7  pb7  pc7  pd7  ---  pf7  pg7  ph7   (e7 vacío, peón a e5)
#   Rank 6: ---  ---  Cc6  ---  ---  ---  ---  ---
#   Rank 5: ---  ---  ---  ---  pe5  ---  ---  ---
#   Rank 4: ---  ---  ---  Pd4  Pe4  ---  ---  ---   (peones blancos en d4 y e4)
#   Rank 3: ---  ---  ---  ---  ---  Cf3  ---  ---   (caballo blanco f3)
#   Rank 2: Pa2  Pb2  Pc2  ---  ---  Pf2  Pg2  Ph2   (d2 y e2 vacíos)
#   Rank 1: Ra1  Cb1  Ac1  Dd1  Re1  Af1  ---  Rh1   (g1 vacío, Cf3)
#
# Convención de colores (igual que en 2h):
#   Piezas blancas = pieza original
#   Piezas negras  = pieza.negative()
#   Casilla clara  = square               (i+j) % 2 == 0
#   Casilla oscura = square.negative()

W = True
B = False

def celda(pieza, es_blanca, es_clara):
    fondo = square if es_clara else square.negative()
    if pieza is None:
        return fondo
    p = pieza if es_blanca else pieza.negative()
    return fondo.under(p)

def es_clara(display_row, col):
    return (display_row + col) % 2 == 0

board_data = [
    # Rank 8 (display_row=0)
    [(rock,B),(None,B),(bishop,B),(queen,B),(king,B),(bishop,B),(knight,B),(rock,B)],
    # Rank 7 (display_row=1): e7 vacío
    [(pawn,B),(pawn,B),(pawn,B),(pawn,B), None,      (pawn,B),(pawn,B),(pawn,B)],
    # Rank 6 (display_row=2): Cc6
    [None,    None,    (knight,B),None,   None,      None,    None,    None   ],
    # Rank 5 (display_row=3): pe5
    [None,    None,    None,      None,   (pawn,B),  None,    None,    None   ],
    # Rank 4 (display_row=4): Pd4 y Pe4
    [None,    None,    None,      (pawn,W),(pawn,W), None,    None,    None   ],
    # Rank 3 (display_row=5): Cf3
    [None,    None,    None,      None,   None,      (knight,W),None,  None   ],
    # Rank 2 (display_row=6): d2 y e2 vacíos
    [(pawn,W),(pawn,W),(pawn,W),  None,   None,      (pawn,W),(pawn,W),(pawn,W)],
    # Rank 1 (display_row=7): g1 vacío (Cf3), f1 con alfil aún
    [(rock,W),(knight,W),(bishop,W),(queen,W),(king,W),(bishop,W),None,(rock,W)],
]

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

imagen = construir_fila(7)
for i in range(6, -1, -1):
    imagen = imagen.up(construir_fila(i))

draw(imagen)

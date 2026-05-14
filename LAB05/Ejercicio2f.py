from interpreter import draw
from chessPictures import *

# Ejercicio 2f: Dos torres (blanca y negra) sobre una fila de 8 casillas alternadas.
# Se construye la fila completa de un tablero y se ubican las torres en las
# posiciones a1 (oscura) y h1 (clara) del lado blanco.
#
# Casilla clara sin pieza
sq_c  = square
# Casilla oscura sin pieza
sq_o  = square.negative()
# Torre blanca sobre casilla oscura (a1 es oscura en ajedrez)
torre_b_osc = sq_o.under(rock)
# Torre blanca sobre casilla clara (h1 es clara)
torre_b_cla = sq_c.under(rock)

# Fila rank-1: a1(osc-torre) b1(cla) c1(osc) d1(cla) e1(osc) f1(cla) g1(osc) h1(cla-torre)
fila = (torre_b_osc
        .join(sq_c)
        .join(sq_o)
        .join(sq_c)
        .join(sq_o)
        .join(sq_c)
        .join(sq_o)
        .join(torre_b_cla))
draw(fila)

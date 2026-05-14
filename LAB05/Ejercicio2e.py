from interpreter import draw
from chessPictures import *

# Ejercicio 2e: Pieza blanca sobre casilla clara y pieza negra sobre casilla oscura.
# square          → casilla clara (gris claro)
# square.negative()  → casilla oscura (gris)
# .under(piece)   → superpone la pieza sobre el fondo de casilla
# pieza negra     = piece.negative()
celda_clara  = square.under(rock)
celda_oscura = square.negative().under(rock.negative())
draw(celda_clara.join(celda_oscura))

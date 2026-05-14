from interpreter import draw
from chessPictures import *

# Ejercicio 2d: Figura 2x2 usando join, up y horizontalMirror.
# Paso 1: fila superior = torre | espejo-vertical
# Paso 2: fila inferior = espejo-horizontal de la fila superior
# Paso 3: se apilan con up (la fila superior queda encima)
top    = rock.join(rock.verticalMirror())
bottom = top.horizontalMirror()
draw(bottom.up(top))

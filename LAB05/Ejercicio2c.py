from interpreter import draw
from chessPictures import *

# Ejercicio 2c: Dibujar la torre unida a su espejo vertical, en negativo.
# Se encadena .negative() sobre el resultado del join para invertir todos
# los colores de la figura resultante.
draw(rock.join(rock.verticalMirror()).negative())

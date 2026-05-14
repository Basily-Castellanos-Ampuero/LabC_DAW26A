from interpreter import draw
from chessPictures import *

# Ejercicio 2b: Dibujar la torre unida a su espejo vertical.
# rock.verticalMirror() invierte cada fila de izquierda a derecha.
# rock.join(...)      coloca la imagen espejo a la derecha de la original.
draw(rock.join(rock.verticalMirror()))

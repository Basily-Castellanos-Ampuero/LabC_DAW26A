from colors import *

class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        """Recibe un color como caracter y devuelve su color negativo."""
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """Devuelve el espejo vertical de la imagen (voltea cada fila de izq a der)."""
        return Picture([row[::-1] for row in self.img])

    def horizontalMirror(self):
        """Devuelve el espejo horizontal de la imagen (voltea el orden de las filas)."""
        return Picture(self.img[::-1])

    def negative(self):
        """Devuelve un negativo de la imagen invirtiendo cada color caracter."""
        return Picture(
            [''.join(self._invColor(c) for c in row) for row in self.img]
        )

    def join(self, p):
        """Devuelve una nueva figura poniendo la figura del argumento
        al lado derecho de la figura actual."""
        return Picture(
            [self.img[i] + p.img[i] for i in range(len(self.img))]
        )

    def up(self, p):
        """Devuelve una nueva figura poniendo la figura recibida como argumento
        encima de la figura actual (p queda arriba, self queda abajo)."""
        return Picture(p.img + self.img)

    def under(self, p):
        """Devuelve una nueva figura poniendo la figura p sobre la figura actual.
        Donde p tiene espacio (' ') se muestra el fondo (self), en el resto se
        muestra p."""
        result = []
        for i in range(len(self.img)):
            row = ''
            for j in range(len(self.img[i])):
                p_char = p.img[i][j] if i < len(p.img) and j < len(p.img[i]) else ' '
                s_char = self.img[i][j]
                row += s_char if p_char == ' ' else p_char
            result.append(row)
        return Picture(result)

    def horizontalRepeat(self, n):
        """Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n."""
        return Picture([row * n for row in self.img])

    def verticalRepeat(self, n):
        """Devuelve una nueva figura repitiendo la figura actual hacia abajo
        la cantidad de veces que indique el valor de n."""
        return Picture(self.img * n)

    def rotate(self):
        """Devuelve una figura rotada 90 grados en sentido horario."""
        rows = len(self.img)
        cols = len(self.img[0]) if rows > 0 else 0
        return Picture(
            [''.join(self.img[rows - 1 - j][i] for j in range(rows))
             for i in range(cols)]
        )

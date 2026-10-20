class Interfaz:
    def __init__(self, logica):
        self.logica = logica
        self.scroll_y = 0
        self.scroll_x = 0
        self.prefijo = "999 | "

    def dibujar(self, stdscr):
        stdscr.erase()
        alto, ancho = stdscr.getmaxyx()
        self.logica.ancho_max = ancho - len(self.prefijo) - 2
        ancho_texto = ancho - len(self.prefijo) - 1
        lineas_visibles = alto - 3

        self._ajustar_texto(ancho_texto)
        self._ajustar_lineas(lineas_visibles)
        self._dibujar_interfaz(stdscr, ancho_texto, lineas_visibles)

    def _dibujar_interfaz(self, stdscr, ancho_texto, lineas_visibles):
        stdscr.addstr(0, 0, f"x deseado : {self.logica.cursor_x_deseado}")
        stdscr.addstr(1, 0, f"cursor x  : {self.logica.cursor_x}")
        stdscr.addstr(2, 0, f"cursor y  : {self.logica.cursor_y}")
        for fila in range(lineas_visibles):
            i = self.scroll_y + fila
            if i >= len(self.logica.matriz):
                break
            texto = "".join(self.logica.matriz[i])
            if i == self.logica.cursor_y:
                texto = texto[:self.logica.cursor_x] + "<" + texto[self.logica.cursor_x:]
            visible = texto[self.scroll_x : self.scroll_x + ancho_texto]
            stdscr.addstr(fila + 3, 0, f"{self._ajustar_numero(i)} | {visible}")
        stdscr.refresh()

    def _ajustar_texto(self, ancho_texto):
        if self.logica.cursor_x < self.scroll_x:
            self.scroll_x = self.logica.cursor_x
        elif self.logica.cursor_x >= self.scroll_x + ancho_texto:
            self.scroll_x = self.logica.cursor_x - ancho_texto + 1

    def _ajustar_lineas(self, lineas_visibles):
        if self.logica.cursor_y < self.scroll_y:
            self.scroll_y = self.logica.cursor_y
        elif self.logica.cursor_y >= self.scroll_y + lineas_visibles:
            self.scroll_y = self.logica.cursor_y - lineas_visibles + 1

    @staticmethod
    def _ajustar_numero(numero, largo=3):
        numero = str(numero)
        largo = largo - len(numero)
        return largo * " " + numero
    
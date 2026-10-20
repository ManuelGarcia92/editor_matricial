class Pantalla:
    def __init__(self, logica):
        self.logica = logica
        self.scroll_y = 0
        self.scroll_x = 0
        self.prefijo = "999 >>> : "

    def dibujar(self, stdscr):
        stdscr.erase()
        alto, ancho = stdscr.getmaxyx()
        self.logica.ancho_max = ancho - len(self.prefijo) - 2
        ancho_texto = ancho - len(self.prefijo) - 1
        filas_visibles = alto - 3

        self._ajustar_texto(ancho_texto)
        self._ajustar_filas(filas_visibles)
        self._dibujar_interfaz(stdscr, ancho_texto, filas_visibles)

    def _dibujar_interfaz(self, stdscr, ancho_texto, filas_visibles):
        stdscr.addstr(0, 0, f"x deseado : {self.logica.cursor_x_deseado}")
        stdscr.addstr(1, 0, f"cursor x  : {self.logica.cursor_x}")
        stdscr.addstr(2, 0, f"cursor y  : {self.logica.cursor_y}")
        for fila in range(filas_visibles):
            i = self.scroll_y + fila
            if i >= len(self.logica.matriz):
                break
            texto = "".join(self.logica.matriz[i])
            if i == self.logica.cursor_y:
                texto = texto[:self.logica.cursor_x] + "<" + texto[self.logica.cursor_x:]
            visible = texto[self.scroll_x : self.scroll_x + ancho_texto]
            stdscr.addstr(fila + 3, 0, f"{i + 1} >>> {visible}")
        stdscr.refresh()

    def _ajustar_texto(self, ancho_texto):
        if self.logica.cursor_x < self.scroll_x:
            self.scroll_x = self.logica.cursor_x
        elif self.logica.cursor_x >= self.scroll_x + ancho_texto:
            self.scroll_x = self.logica.cursor_x - ancho_texto + 1

    def _ajustar_filas(self, filas_visibles):
        if self.logica.cursor_y < self.scroll_y:
            self.scroll_y = self.logica.cursor_y
        elif self.logica.cursor_y >= self.scroll_y + filas_visibles:
            self.scroll_y = self.logica.cursor_y - filas_visibles + 1
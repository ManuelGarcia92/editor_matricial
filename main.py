import readline
import curses

class Editor:
    def __init__(self):
        self.cursor_y = 0
        self.scroll_y = 0
        self.cursor_x = 0
        self.scroll_x = 0
        self.ancho_max = 80
        self.cursor_x_deseado = 0
        self.matriz = [[]]
        
    def editar(self, stdscr):
        curses.curs_set(0)
        while True:
            self.dibujar(stdscr)
            tecla = stdscr.getch()

            if tecla == 27:
                break
            elif tecla == curses.KEY_UP:
                self._arriba()
            elif tecla == curses.KEY_DOWN:
                self._abajo()
            elif tecla == curses.KEY_LEFT:
                self._izquierda()
            elif tecla == curses.KEY_RIGHT:
                self._derecha()
            elif tecla == curses.KEY_HOME:
                self._principio_linea()
            elif tecla == curses.KEY_END:
                self._fin_linea()
            elif tecla == curses.KEY_PPAGE:
                self._primera_linea()
            elif tecla == curses.KEY_NPAGE:
                self._ultima_linea()
            elif tecla in (10, curses.KEY_ENTER):
                self._añadir_linea()
            elif tecla in (curses.KEY_BACKSPACE, 127, 8):
                self._eliminar_caracter()
            elif tecla == 9:
                self._tabulacion()
            elif tecla == curses.KEY_BTAB:
                self._tabulacion_inversa()
            elif 32 <= tecla <= 126:
                self._añadir(chr(tecla))
        return self.matriz
    
    def dibujar(self, stdscr):
        stdscr.erase()
        alto, ancho = stdscr.getmaxyx()
        prefijo = "999 >>> : "
        self.ancho_max = ancho - len(prefijo) - 2
        filas_visibles = alto - 3
        ancho_texto = ancho - len(prefijo) - 1

        if self.cursor_x < self.scroll_x:
            self.scroll_x = self.cursor_x
        elif self.cursor_x >= self.scroll_x + ancho_texto:
            self.scroll_x = self.cursor_x - ancho_texto + 1

        if self.cursor_y < self.scroll_y:
            self.scroll_y = self.cursor_y
        elif self.cursor_y >= self.scroll_y + filas_visibles:
            self.scroll_y = self.cursor_y - filas_visibles + 1

        stdscr.addstr(0, 0, f"x deseado : {self.cursor_x_deseado} \ncursor x : {self.cursor_x} \ncursor y : {self.cursor_y}")

        for fila in range(filas_visibles):
            i = self.scroll_y + fila
            if i >= len(self.matriz):
                break
            texto = "".join(self.matriz[i])
            if i == self.cursor_y:
                texto = texto[:self.cursor_x] + "<" + texto[self.cursor_x:]
            visible = texto[self.scroll_x : self.scroll_x + ancho_texto]
            stdscr.addstr(fila + 3, 0, f"{i + 1} >>> {visible}")
        stdscr.refresh()

    def _arriba(self):
        if self.cursor_y > 0:
            self.cursor_y -= 1
            self.cursor_x = min(self.cursor_x_deseado, len(self.matriz[self.cursor_y]))

    def _abajo(self):
        if self.cursor_y == len(self.matriz) - 1:
            self.matriz.append([])
        self.cursor_y += 1
        self.cursor_x = min(self.cursor_x_deseado, len(self.matriz[self.cursor_y]))
        
    def _izquierda(self):
        if self.cursor_x > 0:
            self.cursor_x -= 1
            self.cursor_x_deseado = self.cursor_x
        elif self.cursor_x == 0 and self.cursor_y > 0:
            self.cursor_y -= 1
            self.cursor_x = len(self.matriz[self.cursor_y])
                    
    def _derecha(self):
        if self.cursor_x < len(self.matriz[self.cursor_y]):
            self.cursor_x += 1
            self.cursor_x_deseado = self.cursor_x
        elif self.cursor_x == len(self.matriz[self.cursor_y]) and self.cursor_y < len(self.matriz) - 1:
            self.cursor_y += 1
            self.cursor_x = 0

    def _principio_linea(self):
        self.cursor_x = 0
        self.cursor_x_deseado = self.cursor_x

    def _fin_linea(self):
        self.cursor_x = len(self.matriz[self.cursor_y])
        self.cursor_x_deseado = self.cursor_x

    def _primera_linea(self):
        self.cursor_y = 0
        self.cursor_x = min(self.cursor_x_deseado, len(self.matriz[self.cursor_y]))

    def _ultima_linea(self):
        self.cursor_y = len(self.matriz) - 1
        self.cursor_x = min(self.cursor_x_deseado, len(self.matriz[self.cursor_y]))

    def _añadir_linea(self):
        linea = self.matriz[self.cursor_y]
        resto = linea[self.cursor_x:]
        del linea[self.cursor_x:]
        self.matriz.insert(self.cursor_y + 1, resto)
        self.cursor_y += 1
        self.cursor_x = 0
        self.cursor_x_deseado = 0

    def _tabulacion(self):
        linea = self.matriz[self.cursor_y]
        n = 4 - (self.cursor_x % 4)
        libre = self.ancho_max - len(linea)
        if libre > 0:
            self._añadir([' '] * min(n, libre))
        else:
            self.cursor_x = min(self.cursor_x + n, len(linea))
            self.cursor_x_deseado = self.cursor_x
            
    def _tabulacion_inversa(self):
        if self.cursor_x == 0:
            return
        n = self.cursor_x % 4 or 4
        self.cursor_x -= n
        self.cursor_x_deseado = self.cursor_x

    def _añadir(self, entrada):
        linea = self.matriz[self.cursor_y]
        if len(linea) + len(entrada) > self.ancho_max:
            return
        self.matriz[self.cursor_y][self.cursor_x:self.cursor_x] = list(entrada)
        self.cursor_x += len(entrada)
        self.cursor_x_deseado = self.cursor_x

    def _eliminar_caracter(self): 
        if  self.cursor_x > 0:
            self.matriz[self.cursor_y].pop(self.cursor_x - 1)
            self.cursor_x -= 1
            self.cursor_x_deseado = self.cursor_x
        elif self.cursor_x == 0 and len(self.matriz) > 1 and len(self.matriz[self.cursor_y]) == 0:
            self.matriz.pop(self.cursor_y)
            self.cursor_y -= 1
            self.cursor_x = len(self.matriz[self.cursor_y])
            
    def _limpiar_linea_actual(self):
        self.matriz[self.cursor_y] = []
        self.cursor_x = 0
        self.cursor_x_deseado = self.cursor_x

    def _eliminar_linea_actual(self):
        if len(self.matriz) > 1:
            self.matriz.pop(self.cursor_y)
            self.cursor_y = min(self.cursor_y, len(self.matriz) - 1)
        else:
            self.matriz[0] = []
        self.cursor_x = min(self.cursor_x_deseado, len(self.matriz[self.cursor_y]))
        
editor = Editor()
resultado = curses.wrapper(editor.editar)
print(resultado)

    
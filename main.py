import readline
import curses

class Editor:
    def __init__(self):
        self.cursor_y = 0
        self.cursor_x = 0
        self.cursor_x_deseado = 0
        self.matriz = [[]]

    def editar(self, stdscr):
        curses.curs_set(0)
        while True:
            self.dibujar(stdscr)
            tecla = stdscr.getch()

            if tecla == 27:
                break
            elif tecla == curses.KEY_UP:    self._arriba()
            elif tecla == curses.KEY_DOWN:  self._abajo()
            elif tecla == curses.KEY_LEFT:  self._izquierda()
            elif tecla == curses.KEY_RIGHT: self._derecha()
            elif tecla == curses.KEY_HOME:  self._principio_linea()
            elif tecla == curses.KEY_END:   self._fin_linea()
            elif tecla == curses.KEY_PPAGE: self._primera_linea()
            elif tecla == curses.KEY_NPAGE: self._ultima_linea()
            elif tecla in (10, curses.KEY_ENTER):
                self._añadir_linea()
            elif tecla in (curses.KEY_BACKSPACE, 127, 8):
                self._eliminar_caracter()
            elif tecla == 9:
                self._tabulacion()
            elif 32 <= tecla <= 126:
                self._añadir(chr(tecla))
        return self.matriz
    
    def dibujar(self, stdscr):
        stdscr.erase()
        stdscr.addstr(0, 0, f"x deseado : {self.cursor_x_deseado} x : {self.cursor_x} y : {self.cursor_y}")
        for i, linea in enumerate(self.matriz):
            texto = "".join(linea)
            if i == self.cursor_y:
                texto = texto[:self.cursor_x] + "<" + texto[self.cursor_x:]
            stdscr.addstr(i + 2, 0, f"{i + 1} >>> : {texto}")
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

    def _derecha(self):
        if self.cursor_x < len(self.matriz[self.cursor_y]) and self.cursor_x < 100:
            self.cursor_x += 1
            self.cursor_x_deseado = self.cursor_x

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
        if self.cursor_y == len(self.matriz) - 1:
            self.matriz.append([])
        self.cursor_y += 1
        self.cursor_x = min(self.cursor_x_deseado, len(self.matriz[self.cursor_y]))

    def _tabulacion(self):
        pass
    
    def _tabulacion_inversa(self):
        pass

    def _añadir(self, entrada):
        self.matriz[self.cursor_y][self.cursor_x:self.cursor_x] = list(entrada)
        self.cursor_x += len(entrada)
        self.cursor_x_deseado = self.cursor_x

    def _eliminar_caracter(self): 
        if  self.cursor_x > 0:
            self.matriz[self.cursor_y].pop(self.cursor_x - 1)
            self.cursor_x -= 1
            self.cursor_x_deseado = self.cursor_x
            
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
        
    def _eliminar_ultima_linea(self):
        if len(self.matriz) > 1:
            self.matriz.pop()
            self.cursor_y = min(self.cursor_y, len(self.matriz) - 1)
        else:
            self.matriz[0] = []
        self.cursor_x = min(self.cursor_x_deseado, len(self.matriz[self.cursor_y]))

    def _info(self):
        self.limpiar_terminal()
        print("======Versión v5.5======")
        print("::::::::COMANDOS::::::::")
        print(":break     : salir")
        print(":info      : ver comandos")
        print("enter      : añadir nueva línea")
        print("espacio    : añadir espacio")
        print("caracteres : añadir caracteres")
        print("+y         : arriba")
        print("-y         : abajo")
        print("-x         : izquierda")
        print("+x         : derecha")
        print("+y+        : primera línea")
        print("-y-        : última línea")
        print("+x+        : principio de línea")
        print("-x-        : fin de la línea")
        print("y--        : eliminar línea actual")
        print("x--        : limpiar línea actual")
        print("--y        : eliminar última línea")
        print("--x        : eliminar caracter")
        input()

editor = Editor()
resultado = curses.wrapper(editor.editar)
print(resultado)

    
from logica import logica
from pantalla import Pantalla
import curses

class Editor:
    def __init__(self):
        self.logica = logica()
        self.pantalla = Pantalla(self.logica)
        
    def _entrada(self, stdscr):
        curses.curs_set(0)
        while True:
            self.pantalla.dibujar(stdscr)
            tecla = stdscr.getch()

            if tecla == 27:
                break
            elif tecla == curses.KEY_UP:
                self.logica.arriba()
            elif tecla == curses.KEY_DOWN:
                self.logica.abajo()
            elif tecla == curses.KEY_LEFT:
                self.logica.izquierda()
            elif tecla == curses.KEY_RIGHT:
                self.logica.derecha()
            elif tecla == curses.KEY_HOME:
                self.logica.principio_linea()
            elif tecla == curses.KEY_END:
                self.logica.fin_linea()
            elif tecla == curses.KEY_PPAGE:
                self.logica.primera_linea()
            elif tecla == curses.KEY_NPAGE:
                self.logica.ultima_linea()
            elif tecla in (10, curses.KEY_ENTER):
                self.logica.añadir_linea()
            elif tecla in (curses.KEY_BACKSPACE, 127, 8):
                self.logica.eliminar_caracter()
            elif tecla == 9:
                self.logica.tabulacion()
            elif tecla == curses.KEY_BTAB:
                self.logica.tabulacion_inversa()
            elif 32 <= tecla <= 126:
                self.logica.añadir(chr(tecla))
        return self.logica.matriz

    def salida(self):
        return curses.wrapper(self._entrada)
from logica import Logica
from interfaz import Interfaz
import curses

class Editor:
    def __init__(self):
        self.logica = Logica()
        self.interfaz = Interfaz(self.logica)
        self.controles = {
            curses.KEY_UP        : self.logica.arriba,
            curses.KEY_DOWN      : self.logica.abajo,
            curses.KEY_LEFT      : self.logica.izquierda,
            curses.KEY_RIGHT     : self.logica.derecha,
            curses.KEY_HOME      : self.logica.principio_linea,
            curses.KEY_END       : self.logica.fin_linea,
            curses.KEY_PPAGE     : self.logica.primera_linea,
            curses.KEY_NPAGE     : self.logica.ultima_linea,
            9                    : self.logica.tabulacion,
            curses.KEY_BTAB      : self.logica.tabulacion_inversa,
            curses.KEY_ENTER     : self.logica.añadir_linea,
            13                   : self.logica.añadir_linea,
            10                   : self.logica.añadir_linea,
            curses.KEY_BACKSPACE : self.logica.eliminar_caracter,
            127                  : self.logica.eliminar_caracter, 
            8                    : self.logica.eliminar_caracter
        }
        
    def _entrada(self, stdscr):
        curses.curs_set(0)
        while True:
            self.interfaz.dibujar(stdscr)
            tecla = stdscr.getch()

            if tecla == 27:
                break

            elif tecla in self.controles:
                self.controles[tecla]()

            elif 32 <= tecla <= 126:
                self.logica.añadir_caracter(chr(tecla))

        return self.logica.matriz

    def salida(self):
        return curses.wrapper(self._entrada) 
    
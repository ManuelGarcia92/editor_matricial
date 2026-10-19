import readline
import curses

class Editor:
    def __init__(self):
        self.cursor_y = 0
        self.cursor_x = 0
        self.cursor_x_deseado = 0
        self.matriz = [[]]

    def editar(self):
        while True:
            self.dibujar()
            entrada = input()  

            if entrada == ":break":
                break

            elif entrada == ":info":
                self._info()

            elif entrada == "+y":
                self._arriba()

            elif entrada == "-y":
                self._abajo()

            elif entrada == "-x":
                self._izquierda()

            elif entrada == "+x": 
                self._derecha()

            elif entrada == "+y+":
                self._primera_linea()

            elif entrada == "-y-":
                self._ultima_linea()

            elif entrada == "+x+":
                self._principio_linea()

            elif entrada == "-x-":
                self._fin_linea()

            elif entrada == "":
                self._añadir_linea()

            elif entrada == "y--": 
                self._eliminar_linea_actual()

            elif entrada == "x--":
                self._limpiar_linea_actual()

            elif entrada == "x++":
                self._tabulacion()

            elif entrada == "--y":
                self._eliminar_ultima_linea()

            elif entrada == "--x": 
                self._eliminar_caracter()

            elif entrada == "x++":
                self._tabulacion_inversa()

            else:
                self._añadir(entrada)

        return self.matriz
    
    @staticmethod
    def limpiar_terminal() -> None:
        import os
        os.system("cls" if os.name == "nt" else "clear")

    def dibujar(self):
        self.limpiar_terminal()
        print(f"Cursor x deseado : {self.cursor_x_deseado}")
        print(f"Cursor x         : {self.cursor_x}")
        print(f"Cursor y         : {self.cursor_y}")
        for i, linea in enumerate(self.matriz):
            texto = "".join(linea)
            if i == self.cursor_y:
                texto = texto[:self.cursor_x] + "<" + texto[self.cursor_x:]
            print(f"{i + 1} >>> : {texto}")

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

    def _añadir_linea(self):
        if self.cursor_y == len(self.matriz) - 1:
            self.matriz.append([])
        self.cursor_y += 1
        self.cursor_x = min(self.cursor_x_deseado, len(self.matriz[self.cursor_y]))

    def _primera_linea(self):
        self.cursor_y = 0
        self.cursor_x = min(self.cursor_x_deseado, len(self.matriz[self.cursor_y]))
    
    def _ultima_linea(self):
        self.cursor_y = len(self.matriz) - 1
        self.cursor_x = min(self.cursor_x_deseado, len(self.matriz[self.cursor_y]))

    def _principio_linea(self):
        self.cursor_x = 0
        self.cursor_x_deseado = self.cursor_x

    def _fin_linea(self):
        self.cursor_x = len(self.matriz[self.cursor_y])
        self.cursor_x_deseado = self.cursor_x

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
resultado = editor.editar()
print(resultado)

    
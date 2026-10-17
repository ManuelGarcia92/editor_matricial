class Editor:
    def __init__(self):
        self.pila_auxiliar = []
        self.cursor_y = 0
        self.cursor_x = 0
        self.matriz = [
            [" "]
        ]

    def editar(self):
        while True:
            self.renderizar()
            entrada = input()  

            if entrada == "break":
                break

            elif entrada == "info":
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

            elif entrada == "--y":
                self._eliminar_ultima_linea()

            elif entrada == "--x": 
                self._eliminar_caracter()

            else:
                self._añadir(entrada)

            self.renderizar()

        return self.matriz
    
    @staticmethod
    def limpiar_terminal() -> None:
        import os
        os.system("cls" if os.name == "nt" else "clear")

    def _info(self):
        self.limpiar_terminal()
        print("======Versión v5.5======")
        print("::::::::COMANDOS::::::::")
        print("break      : salir")
        print("info       : ver comandos")
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

    def renderizar(self):
        self.limpiar_terminal()
        print(f"Cursor x : {self.cursor_x}")
        print(f"Cursor y : {self.cursor_y}")
        for y, fila in enumerate(self.matriz):
            self.pos = y
            linea = f"{self.pos+1} >>> :"
            for x, caracter in enumerate(fila):
                if x == self.cursor_x and y == self.cursor_y:
                    linea += f"{caracter}<"
                else:
                    linea += f"{caracter}"
            print(linea)

    def _arriba(self):
        if self.cursor_y > 0:
            self.cursor_y -= 1
            self.cursor_x = min(self.cursor_x, len(self.matriz[self.cursor_y]) - 1)

    def _abajo(self):
        if self.cursor_y == len(self.matriz) - 1:
            self.matriz.append([" "])
            self.cursor_x = 0
        self.cursor_y += 1
        self.cursor_x = min(self.cursor_x, len(self.matriz[self.cursor_y]) - 1)
        
    def _izquierda(self):
        if self.cursor_x > 0:
            self.cursor_x -= 1

    def _derecha(self):
        if self.cursor_x < len(self.matriz[self.cursor_y]) - 1 and self.cursor_x < 100:
            self.cursor_x += 1

    def _primera_linea(self):
        self.cursor_y = 0

    def _ultima_linea(self):
        self.cursor_y = len(self.matriz) - 1

    def _principio_linea(self):
        self.cursor_x = 0

    def _fin_linea(self):
        self.cursor_x = len(self.matriz[self.cursor_y]) - 1

    def _añadir(self, entrada):
        self.añadir_entrada(entrada)

    def _eliminar_caracter(self): 
        if self.matriz[self.cursor_y] and self.cursor_x > 0:
            self.matriz[self.cursor_y].pop(self.cursor_x)
            self.cursor_x -= 1
            
    def _añadir_linea(self):
        self.matriz.append([" "])
        self.cursor_y += 1
        self.cursor_x = 0

    def _limpiar_linea_actual(self):
        self.matriz[self.cursor_y] = [" "]
        self.cursor_x = 0

    def _eliminar_linea_actual(self):
        if len(self.matriz) > 1:
            self.matriz.pop(self.cursor_y)
            self.cursor_y = min(self.cursor_y, len(self.matriz) - 1)
        else:
            self.matriz[0] = [" "]
        self.cursor_x = 0

    def _eliminar_ultima_linea(self):
        if len(self.matriz) > 1:
            self.matriz.pop()
            self.cursor_y = min(self.cursor_y, len(self.matriz) - 1)
        else:
            self.matriz[0] = [" "]
        self.cursor_x = 0

    def añadir_entrada(self, entrada):
        x = self.cursor_x + 1
        self.matriz[self.cursor_y][x:x] = list(entrada)
        self.cursor_x += len(entrada)
        
editor = Editor()
resultado = editor.editar()
print(resultado)

    
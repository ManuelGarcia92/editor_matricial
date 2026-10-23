from editor import Editor

def main() -> None:
    editor = Editor()
    matriz = editor.salida()
    resultado = editor.formatear_matriz(matriz)
    print(resultado)

if __name__ == "__main__":
    main()

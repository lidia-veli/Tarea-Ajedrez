'''
Modulo para el manejo de movimientos de las piezas del ajedrez
'''
# ---------- IMPORTACIONES ----------
import sys

# ---------- VARIABLES ----------

# ---------- FUNCIONES ----------

def imprimir_tablero(tablero):
    for fila in tablero:
        for casilla in fila:
            print(casilla, end=' ')
        print()

def guardar_tablero(tablero):
    '''
    Guarda el tablero en el archivo log_mov.txt
    '''
    # Redireccionamos la salida estandar a un archivo
    sys.stdout = open("data/log_movimientos.txt", "a", encoding="utf-8") # -- AÑADIR TEXTO (append) en el archivo seleccionado

    # -- esto es lo que se va a imprimir en el archivo .txt
    imprimir_tablero(tablero)
    # -- fin de lo que se va a imprimir en archivo .txt

    # Cerramos el archivo
    sys.stdout.close()


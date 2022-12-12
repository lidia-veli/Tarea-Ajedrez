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


def elegir_pieza_a_mover(tablero):
    '''
    Pide al usuario que elija una pieza del juego que desea mover
    -INPUT-----
    tablero: list -- tablero del juego
    -OUTPUT-----
    (fila, columna): tuple 
        fila: int -- fila donde está la pieza
        columna: int -- columna donde está la pieza
    '''
    while True:
        try:
            fila = int(input("Elige la fila de la pieza: "))
            columna = int(input("Elige la columna de la pieza: "))
            if tablero[fila][columna] != ' ': # si hay una pieza en esa casilla
                return fila, columna # 
            else:
                print("No hay ninguna pieza en esa casilla")
        except:
            print("Error. Introduce un número válido")

def elegir_casilla_donde_mover(tablero):
    '''
    Pide al usuario que elija una casilla donde mover la pieza
    -INPUT-----
    tablero: list -- tablero del juego
    -OUTPUT-----
    (fila, columna): tuple 
        fila: int -- fila de la casilla
        columna: int -- columna de la casilla
    '''
    while True:
        try:
            fila = int(input("Elige la fila de la pieza: "))
            columna = int(input("Elige la columna de la pieza: "))
            if tablero[fila][columna] == ' ': # si la casilla está vacía
                return fila, columna  # nos podemos mover ahí
            else:
                print("En esta casilla ya hay una pieza")
        except:
            print("Error. Introduce un número válido")


def mover_pieza(tablero, fila, columna, fil_nueva, col_nueva):
    '''
    Mueve la pieza de la casilla (fila, columna) a la casilla (fila_nueva, columna_nueva)
    -INPUT-----
    tablero: list -- tablero del juego
    fila: int -- fila de la casilla donde está la pieza
    columna: int -- columna de la casilla donde está la pieza
    fil_nueva: int -- fila de la casilla donde se quiere mover la pieza
    col_nueva: int -- columna de la casilla donde se quiere mover la pieza
    
    -OUTPUT-----
    tablero: list -- tablero actualizado
    '''
    tablero[fil_nueva][col_nueva] = tablero[fila][columna] #movemos la pieza a la nueva casilla
    tablero[fila][columna] = ' ' # y la casilla en la que estaba antes la dejamos vacía
    return tablero

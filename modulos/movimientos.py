'''
Modulo que contiene las funciones relacionadas con el movimientos de las piezas del ajedrez
'''
# ---------- IMPORTACIONES ----------
from data.piezas_ajedrez import *

# ---------- VARIABLES ----------
#diccionario de la coordenadas del tablero a las posiciones en la lista
FILAS = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8} 
COLUMNAS = {'A':2, 'B':4, 'C':6, 'D':8, 'E':10, 'F':12, 'G':14, 'H':16}

# ---------- FUNCIONES ----------

def imprimir_tablero(tablero):
    for fila in tablero:
        for casilla in fila:
            if casilla in lista_piezas:
                print(casilla, end=' ')
            else:
                print(casilla, end='')
        print()

def guardar_tablero(tablero):
    '''
    Guarda el tablero en el archivo log_mov.txt
    '''
    with open("data/partida_ajedrez.txt", "a", encoding="utf-8") as archivo:
        for fila in tablero:
            lista_texto = [] # lista para guardar el texto de cada fila
            for casilla in fila:
                lista_texto.append(casilla)
            archivo.writelines(lista_texto) # escribimos la lista en el archivo
            archivo.writelines('\n') # salto de línea para la siguiente fila de texto
            
        archivo.writelines('\n') # salto de línea para la siguiente fila de texto
        archivo.close()
     

def elegir_pieza_a_mover(tablero):
    '''
    Pide al usuario que elija una pieza del juego que desea mover
    -INPUT-----
    tablero: list -- tablero del juego
    -OUTPUT-----
    (fila, columna): tuple 
        fila: int -- fila donde está la pieza
        columna: int -- columna donde está la pieza
        entrada: str -- entrada del usuario
    '''
    while True:
        entrada = input("Introduce la posición de la pieza que deseas mover: ") #tupla (col, fil)
        if entrada[0] in 'ABCDEFGHabcdefgh' and entrada[1] in '12345678':
            fila = FILAS[ entrada[1] ] # 1,2, ..., 8
            columna = COLUMNAS[ entrada[0].upper() ] # A, B, ..., H
            if tablero[fila][columna] != '[]': # si en la casilla hay una pieza
                print("Has elegido la pieza: ", tablero[fila][columna])
                return fila, columna , entrada # seleccionamos la pieza OUTPUT
            else:
                    print("No hay ninguna pieza en esa casilla. Elige otra vez.")
        else:
            print("Entrada no válida. Elige otra vez.")

def elegir_casilla_donde_mover(tablero):
    '''
    Pide al usuario que elija una casilla donde mover la pieza
    -INPUT-----
    tablero: list -- tablero del juego
    -OUTPUT-----
    (fila, columna): tuple 
        fila: int -- fila de la casilla
        columna: int -- columna de la casilla
        entrada: str -- entrada del usuario
    '''
    while True:
        entrada = input("Introduce la posición de la casilla a la que deseas mover la pieza: ")
        if entrada[0] in 'ABCDEFGHabcdefgh' and entrada[1] in '12345678':
            fila = FILAS[ entrada[1] ] # 1,2, ..., 8
            columna = COLUMNAS[ entrada[0].upper() ] # A, B, ..., H
            if tablero[fila][columna] == '[]': # si la casilla está vacía
                return fila, columna, entrada # nos podemos mover ahí OPUTPUT
            else:
                print("En esta casilla ya hay una pieza. Elige otra vez.")

        else:
            print("Entrada no válida. Elige otra vez.")

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
    tablero[fila][columna] = '[]' # y la casilla en la que estaba antes la dejamos vacía
    return tablero

def pedir_movimiento_a_visualizar(mensaje, MOVIMIENTOS):
    '''
    Funcion que pregunta al usuario que tablero de los jugados quiere revisualizar
    -INPUT-----
    entrada: str -- entrada del usuario
    movements: list -- lista de tableros que se han acumulado a lo largo del juego
    
    -OUTPUT-----
    entrada: int -- entrada del usuario convertida a entero'''
    while True:
        entrada = input(mensaje)    
        try:
            entrada = int(entrada)
            if 0 <= entrada <= len(MOVIMIENTOS):
                return entrada
            else:
                print("Este número no corresponde a un movimiento.")
        except:
            print("Error. Introduce un número válido.")

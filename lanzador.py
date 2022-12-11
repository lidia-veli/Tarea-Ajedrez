# ---------- IMPORTACIONES ----------
from data.juego_ajedrez import *

# ---------- VARIABLES ----------

# ---------- FUNCIONES ----------

def imprimir_tablero(tablero):
    for fila in tablero:
        for casilla in fila:
            print(casilla, end=' ')
        print()

# ---------- PROGRAMA PRINCIPAL ----------
if __name__ == '__main__':
    imprimir_tablero(tablero_inicial)

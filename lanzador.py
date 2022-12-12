# ---------- IMPORTACIONES ----------
from data.piezas_ajedrez import *

from modulos.movimientos import *
from modulos.booleano import *
# ---------- VARIABLES ----------
log_movimientos = [] #lista donde vamos a registrar lso movimientos de la partida

# ---------- FUNCIONES ----------
def JuegoAjedrez():
    '''
    Funcion para jugar al ajedrez
    '''
    print('~~ Bienvenido al juego de ajedrez ~~')
    print('Los movimientos se introducen en formato algebraico, e.g: a2, b3, c4, ...')
    imprimir_tablero(tablero_inicial) # tablero inicial
    
    #-- REDIRECCIONAMOS LA SALIDA ESTÁNDAR A UN ARCHIVO
    sys.stdout = open("data/partida_ajedrez.txt", "a", encoding="utf-8") # AÑADIR TEXTO (append) en el archivo seleccionado

    guardar_tablero(tablero_inicial)
    tablero = tablero_inicial
    while pedir_entrada_si_o_no("¿Quieres hacer algún movimiento? (s/n): ")==True: #mientras nos diga que sí
        # le preguntámos qué pieza quiere mover
        fila, columna, posicion = elegir_pieza_a_mover(tablero)
        # y a dónde quiere moverla
        fil_nueva, col_nueva, pos_nueva = elegir_casilla_donde_mover(tablero)
        # movemos la pieza
        mover_pieza(tablero, fila, columna, fil_nueva, col_nueva)
        log_movimientos.append(posicion +'a'+ pos_nueva) # resgistramos el movimiento
        guardar_tablero(tablero) # guardamos el tablero en el archivo
        print()
        
        

    # si pedir_entrada_si_o_no() devuelve False, el jugador no quiere hacer más movimientos
    
    #-- CERRAMOS EL ARCHIVO donde guardamos los movimientos
    sys.stdout.close()
    
    
    




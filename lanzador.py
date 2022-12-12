# ---------- IMPORTACIONES ----------
from data.piezas_ajedrez import *

from modulos.movimientos import *
from modulos.booleano import *
# ---------- VARIABLES ----------
log_movimientos = ['tablero inicial'] #lista donde vamos a registrar lso movimientos de la partida
TABLEROS = [tablero_inicial]

# ---------- FUNCIONES ----------
def JuegoAjedrez():
    '''
    Funcion para jugar al ajedrez
    '''
    print()
    print('~~ Bienvenido al juego de ajedrez ~~')
    print('Los movimientos se introducen en formato algebraico, e.g: a2, b3, c4, ...')
    imprimir_tablero(tablero_inicial)
    print()

    guardar_tablero(tablero_inicial) # guardamos el tablero inicial en el archivo
    tablero = tablero_inicial

    while pedir_entrada_si_o_no("¿Quieres hacer algún movimiento? (s/n): ")==True: #mientras nos diga que sí
        # le preguntámos qué pieza quiere mover
        fila, columna, posicion = elegir_pieza_a_mover(tablero)
        # y a dónde quiere moverla
        fil_nueva, col_nueva, pos_nueva = elegir_casilla_donde_mover(tablero)
        # movemos la pieza
        tablero = mover_pieza(tablero, fila, columna, fil_nueva, col_nueva)
        log_movimientos.append(posicion +'-'+ pos_nueva) # resgistramos el movimiento
        # guardamos el tablero en el archivo
        guardar_tablero(tablero)
        TABLEROS.append(tablero)    
        
        

    # si pedir_entrada_si_o_no() devuelve False, el jugador no quiere hacer más movimientos
    
    # le preguntamos al usuario qué movimiento desea visualizar
    mov = pedir_movimiento_a_visualizar('¿Qué movimiento desea visualizar? (0 es el tablero inicial): ', log_movimientos)
    
    # y mostramos el tablero correspondiente
    print('Tablero del movimiento', mov, ':', log_movimientos[mov])
    imprimir_tablero(TABLEROS[mov]) #los indices de la lista empiezan en 0
    




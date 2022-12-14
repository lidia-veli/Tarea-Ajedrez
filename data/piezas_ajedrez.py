piezas = {
    'Peon_N': '♟',
    'Torre_N': '♜',
    'Caballo_N': '♞',
    'Alfil_N': '♝',
    'Reina_N': '♛',
    'Rey_N': '♚',
    'Peon_B': '♙',
    'Torre_B': '♖',
    'Caballo_B': '♘',
    'Alfil_B': '♗',
    'Reina_B': '♕',
    'Rey_B': '♔',
    }

lista_piezas = [ piezas[i] for i in piezas ]

tablero_inicial = [
    [' ','  ','A','   ','B','   ','C','   ','D','   ','E','   ','F','   ','G','   ','H'],
    ['1','  ','♜','  ','♞','  ','♝','  ','♛','  ','♚','  ','♝','  ','♞','  ','♜'],
    ['2','  ','♟','  ','♟','  ','♟','  ','♟','  ','♟','  ','♟','  ','♟','  ','♟'],
    ['3','  ','[]','  ','[]','  ','[]','  ','[]','  ','[]','  ','[]','  ','[]','  ','[]'],
    ['4','  ','[]','  ','[]','  ','[]','  ','[]','  ','[]','  ','[]','  ','[]','  ','[]'],
    ['5','  ','[]','  ','[]','  ','[]','  ','[]','  ','[]','  ','[]','  ','[]','  ','[]'],
    ['6','  ','[]','  ','[]','  ','[]','  ','[]','  ','[]','  ','[]','  ','[]','  ','[]'],
    ['7','  ','♙','  ','♙','  ','♙','  ','♙','  ','♙','  ','♙','  ','♙','  ','♙'],
    ['8','  ','♖','  ','♘','  ','♗','  ','♕','  ','♔','  ','♗','  ','♘','  ','♖'],
]

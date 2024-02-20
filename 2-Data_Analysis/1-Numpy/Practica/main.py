import funciones as f


tablero = f.crear_tablero()

barco_1 = [(0,1), (1,1)]
barco_2 = [(1,3), (1,4), (1,5), (1,6)]

tablero = f.colocar_barco(barco_1, tablero)
tablero = f.colocar_barco(barco_2, tablero)

tablero = f.disparar((3,5), tablero)
tablero = f.disparar((1,7), tablero)
tablero = f.disparar((1,5), tablero)

print(tablero)
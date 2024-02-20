import numpy as np

def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, "_")

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def disparar(casilla, tablero):
    if tablero[casilla] == "_":
        print("Agua")
        tablero[casilla] = "A"
    elif tablero[casilla] == "O":
        print("Tocado")
        tablero[casilla] = "X"
    else:
        print("Ya has disparado aquí")
    return tablero
from tateti import Tateti

if __name__ == '__main__':
    juego = Tateti()

    while not juego.empate():
        fil = int(input("Ingrese el numero de fila: "))
        col = int(input("Ingrese el numero de columna: "))
        juego.insertar(fil,col)
        if juego.victoria():
            if juego.token == "O":
                print("Gano el Jugador 1")
            else:
                print("Gano el Jugador 2")
            break
        for a in range(len(juego.tablero)):
            for b in range(len(juego.tablero[a])):
                if b == 1 or b == 0:
                    if juego.tablero[a][b] == 0:
                        print("     |", end="")
                    else:
                        print("  {}  |".format(juego.tablero[a][b]), end="")
                else:
                    if juego.tablero[a][b] == 0:
                        print("     ", end="")
                    else:
                        print("  {}  ".format(juego.tablero[a][b]), end="")
            print("\n-----------------")
    if  juego.empate():
        print("Empate")            
    for a in range(len(juego.tablero)):
            for b in range(len(juego.tablero[a])):
                if b == 1 or b == 0:
                    if juego.tablero[a][b] == 0:
                        print("     |", end="")
                    else:
                        print("  {}  |".format(juego.tablero[a][b]), end="")
                else:
                    if juego.tablero[a][b] == 0:
                        print("     ", end="")
                    else:
                        print("  {}  ".format(juego.tablero[a][b]), end="")
            print("\n-----------------")
from tateti import Tateti

if __name__ == '__main__':
    juego = Tateti()

    while juego.empate():
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
            print(juego.tablero[a])
    if not juego.empate():
        print("Empate")            
    for a in range(len(juego.tablero)):
            print(juego.tablero[a])
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
        juego.print_tablero()
    if  juego.empate():
        print("Empate")            
    juego.print_tablero()

class Tateti:
    def __init__(self):
        self.nombre1 = ""
        self.nombre2 = ""
        self.tablero = [[0 for x in range(3)] for y in range(3)]
        self.tokensp1 = 4
        self.tokensp2 = 4
        self.token = "X"
        self.turno = True
    
    def validar_num(self, number):
        return number <= 2 and number >= 0

    def insertar(self, fil, col):
        if self.validar_num(fil) and self.validar_num(col):
            if self.tablero[fil][col] == 0:
                self.tablero[fil][col] = self.token
                if (self.token == "X"):
                    self.tokensp1 -= 1
                    self.token = "O"
                else:
                    self.tokensp2 -= 1
                    self.token = "X"
                return True
            else:
                return False


    def victoria(self):
        auxX = 0
        auxO = 0
        for i in range(len(self.tablero)):
            if self.tablero[i][i] == "X":
                auxX += 1
            if self.tablero[i][i] == "O":
                auxO += 1
        if auxX == 3:
            return True
        if auxO == 3:
            return True

        for a in range(len(self.tablero)):
            auxX = 0
            auxO = 0
            for b in self.tablero[a]:
                if b == "X":
                    auxX += 1
                if auxX == 3:
                    return True
                if b == "O":
                    auxO += 1
                if auxO == 3:
                    return True
        
        for a in range(len(self.tablero)):
            auxX = 0
            auxO = 0
            for b in range(len(self.tablero[a])):
                if self.tablero[b][a] == "X":
                    auxX += 1
                if auxX == 3:
                    return True
                if self.tablero[b][a] == "O":
                    auxO += 1
                if auxO == 3:
                    return True
        auxX = 0
        auxO = 0
        for i in range(len(self.tablero)):
            if self.tablero[i][len(self.tablero)-1-i] == "X":
                auxX += 1
            if self.tablero[i][len(self.tablero)-1-i] == "O":
                auxO += 1
        if auxX == 3:
            return True
        if auxO == 3:
            return True

    def empate(self):
        return not 0 in self.tablero

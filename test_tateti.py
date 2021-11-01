import unittest
from parameterized import parameterized
from tateti import Tateti

class TestTateti(unittest.TestCase):

    def test_tablero_tamanio(self):
        juego = Tateti()
        self.assertTrue(type(juego.tablero), list)
        self.assertEqual(len(juego.tablero), 3)
        for col in range(len(juego.tablero)):
            self.assertEqual(len(juego.tablero[col]), 3)

    def test_tablero_vacio(self):
        juego = Tateti()
        for a in range(len(juego.tablero)):
            for b in range(len(juego.tablero[a])):
                self.assertEqual(juego.tablero[a][b],0)

    def test_tokens(self):
        juego = Tateti()
        self.assertEqual(juego.tokensp1, 4)
        self.assertEqual(juego.tokensp2, 4)

    def test_put_X_OK(self):
        juego = Tateti()
        juego.insertar(0, 0)
        self.assertEqual(juego.tablero[0][0], "X")
    
    def test_put_X_ERROR(self):
        juego = Tateti()
        self.assertTrue(juego.insertar(0,0))
        self.assertFalse(juego.insertar(0, 0))
        self.assertEqual(juego.tablero[0][0], "X")
    
    def test_cant_mov_p1_4(self):
        juego = Tateti()
        juego.token = "X"
        juego.insertar(1,1)
        juego.token = "X"
        juego.insertar(0,1)
        juego.token = "X"
        juego.insertar(2,0)
        juego.token = "X"
        juego.insertar(2,1)
        self.assertEqual(juego.tokensp1, 0)

    def test_cant_mov_p1_2(self):
        juego = Tateti()
        juego.token = "X"
        juego.insertar(1,1)
        juego.token = "X"
        juego.insertar(0,1)
        self.assertEqual(juego.tokensp1, 2)

    def test_cant_mov_p2_4(self):
        juego = Tateti()
        juego.token = "O"
        juego.insertar(1,1)
        juego.token = "O"
        juego.insertar(0,1)
        juego.token = "O"
        juego.insertar(2,0)
        juego.token = "O"
        juego.insertar(2,1)
        self.assertEqual(juego.tokensp2, 0)

    def test_posicion_valida_invalida(self):
        juego = Tateti()
        self.assertTrue(juego.validar_num(0))
        self.assertTrue(juego.validar_num(1))
        self.assertTrue(juego.validar_num(2))
        self.assertFalse(juego.validar_num(3))
        self.assertFalse(juego.validar_num(-1))

    def test_jugar_2_jugadas(self):
        juego = Tateti()
        juego.insertar(0, 0) #Inserto una X en 0 0 
        self.assertEqual(juego.tablero[0][0], "X")
        juego.insertar(1, 1) #Inserto una O en 1 1 
        self.assertEqual(juego.tablero[1][1], "O")
        juego.insertar(1, 1) #Intento insertar una X en 1 1 pero ya hay una O
        self.assertEqual(juego.tablero[1][1], "O")
        juego.insertar(1, 2)
        self.assertEqual(juego.tablero[1][2], "X")
    
    def test_victoria_p1_d(self):
        juego = Tateti()
        juego.token = "X"
        juego.insertar(1,1)
        juego.token = "X"
        juego.insertar(0,0)
        juego.token = "X"
        juego.insertar(2,2)
        self.assertTrue(juego.victoria())

    def test_victoria_p1_dinv(self):
        juego = Tateti()
        juego.token = "X"
        juego.insertar(0,2)
        juego.token = "X"
        juego.insertar(1,1)
        juego.token = "X"
        juego.insertar(2,0)
        self.assertTrue(juego.victoria())

    def test_victoria_p1_f0(self):
        juego = Tateti()
        juego.token = "X"
        juego.insertar(0,0)
        juego.token = "X"
        juego.insertar(0,1)
        juego.token = "X"
        juego.insertar(0,2)
        self.assertTrue(juego.victoria())

    def test_victoria_p1_f1(self):
        juego = Tateti()
        juego.token = "X"
        juego.insertar(1,0)
        juego.token = "X"
        juego.insertar(1,1)
        juego.token = "X"
        juego.insertar(1,2)
        self.assertTrue(juego.victoria())

    def test_victoria_p1_f2(self):
        juego = Tateti()
        juego.token = "X"
        juego.insertar(2,0)
        juego.token = "X"
        juego.insertar(2,1)
        juego.token = "X"
        juego.insertar(2,2)
        self.assertTrue(juego.victoria())

    def test_victoria_p1_c0(self):
        juego = Tateti()
        juego.token = "X"
        juego.insertar(0,0)
        juego.token = "X"
        juego.insertar(1,0)
        juego.token = "X"
        juego.insertar(2,0)
        self.assertTrue(juego.victoria())

    def test_victoria_p1_c1(self):
        juego = Tateti()
        juego.token = "X"
        juego.insertar(0,1)
        juego.token = "X"
        juego.insertar(1,1)
        juego.token = "X"
        juego.insertar(2,1)
        self.assertTrue(juego.victoria())
    
    def test_victoria_p1_c2(self):
        juego = Tateti()
        juego.token = "X"
        juego.insertar(0,2)
        juego.token = "X"
        juego.insertar(1,2)
        juego.token = "X"
        juego.insertar(2,2)
        self.assertTrue(juego.victoria())
    
    def test_victoria_p2_d(self):
        juego = Tateti()
        juego.token = "O"
        juego.insertar(1,1)
        juego.token = "O"
        juego.insertar(0,0)
        juego.token = "O"
        juego.insertar(2,2)
        self.assertTrue(juego.victoria())

    def test_victoria_p2_dinv(self):
        juego = Tateti()
        juego.token = "O"
        juego.insertar(0,2)
        juego.token = "O"
        juego.insertar(1,1)
        juego.token = "O"
        juego.insertar(2,0)
        self.assertTrue(juego.victoria())

    def test_victoria_p2_f0(self):
        juego = Tateti()
        juego.token = "O"
        juego.insertar(0,0)
        juego.token = "O"
        juego.insertar(0,1)
        juego.token = "O"
        juego.insertar(0,2)
        self.assertTrue(juego.victoria())

    def test_victoria_p2_f1(self):
        juego = Tateti()
        juego.token = "O"
        juego.insertar(1,0)
        juego.token = "O"
        juego.insertar(1,1)
        juego.token = "O"
        juego.insertar(1,2)
        self.assertTrue(juego.victoria())

    def test_victoria_p2_f2(self):
        juego = Tateti()
        juego.token = "O"
        juego.insertar(2,0)
        juego.token = "O"
        juego.insertar(2,1)
        juego.token = "O"
        juego.insertar(2,2)
        self.assertTrue(juego.victoria())

    def test_victoria_p2_c0(self):
        juego = Tateti()
        juego.token = "O"
        juego.insertar(0,0)
        juego.token = "O"
        juego.insertar(1,0)
        juego.token = "O"
        juego.insertar(2,0)
        self.assertTrue(juego.victoria())
    
    def test_victoria_p2_c1(self):
        juego = Tateti()
        juego.token = "O"
        juego.insertar(0,1)
        juego.token = "O"
        juego.insertar(1,1)
        juego.token = "O"
        juego.insertar(2,1)
        self.assertTrue(juego.victoria())
    
    def test_victoria_p2_c2(self):
        juego = Tateti()
        juego.token = "O"
        juego.insertar(0,2)
        juego.token = "O"
        juego.insertar(1,2)
        juego.token = "O"
        juego.insertar(2,2)
        self.assertTrue(juego.victoria())

    def test_empate(self):
        juego = Tateti()
        juego.insertar(0,0)
        juego.insertar(0,1)
        juego.insertar(0,2)
        juego.insertar(1,0)
        juego.insertar(1,1)
        juego.insertar(1,2)
        juego.insertar(2,1)
        juego.insertar(2,0)
        juego.insertar(2,2)
        self.assertTrue(juego.empate())



if __name__ == '__main__':
    unittest.main()
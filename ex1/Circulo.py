## Bibliotecas
import Forma

import turtle as t
import math
#

class Circulo(Forma.Forma):
    ## Atributos
    def __init__(self, area:float, cor:str) -> None:
        super().__init__() # Inicializar classe Pai

        self.cor = cor
        self.area = area
    #

    ## Métodos
    def desenhar(self) -> None:
        turtle = t.Turtle()
        turtle.speed(10)
        turtle.color(self.cor)

        turtle.penup()
        turtle.goto([0, -math.sqrt(self.area/math.pi)])
        turtle.pendown()

        # A = pi * r^2 -> sqrt(A/pi) = r
        turtle.circle(radius=math.sqrt(self.area/math.pi)) 
    #
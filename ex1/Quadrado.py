## Bibliotecas
import Forma

import turtle as t
import math
#

class Quadrado(Forma.Forma):
    ## Atributos
    def __init__(self, area:float, cor:str) -> None:
        super().__init__() # Inicilizar classe pai

        self.area = area
        self.cor = cor
    #

    ## Métodos
    def desenhar(self) -> None:
        turtle = t.Turtle()
        turtle.speed(10)
        turtle.color(self.cor)

        lado = math.sqrt(self.area) # A = l^2 -> l = sqrt(A)
        
        # Isso aqui centraliza o quadrado na tela
        turtle.penup()
        turtle.goto([-lado/2, -lado/2]) 
        turtle.pendown()

        for _ in range(4):
            turtle.forward(lado)
            turtle.left(90)
    #
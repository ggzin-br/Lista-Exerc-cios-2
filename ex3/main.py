## Bibliotecas
from Ponto import Ponto
import turtle as t
import math
#

###
"""
Objetivo: bandeira do Brasil utilizando o objeto iterável Ponto() e turtle
Entrada: área do retângulo principal da bandeira
Saida: bandeira

Requisitos: utilizar o goto() da turtle com o Ponto()
"""
###


def losango(tt: t.Turtle, area:list[float], PROPORCAO:tuple[float, float, float, float, float]) -> None:
    ###
    """
    Aqui é responsável por fazer um losango na parte central da bandeira
    Algoritmo ->
    A setinha do turtle irá até o canto da tela (areaX - proporção * areaY)
    Depois será utilizado o a fórmula para encontrar o lado do losango -> 
    lado = sqrt( [ X/2 - Y*CONST ]^2 + [ Y/2 - Y*CONST ]^2 )
    
    anguloReflexãoB = PI - 2*arcsin( (X/2 - Y*CONST)/ lado)
    anguloReflexãoA = PI - 2*arcsin( (Y/2 - Y*CONST)/ lado)

    Essa rotação somente vale para os ângulos de cima do losango
    formulaRotacao = PI - 2B (angulo da parte de cima do triângulo)
    """
    ###
    ## Declarações
    lado = math.sqrt(
                math.pow( 
                    (area[0]/2 - area[1]*PROPORCAO[2]), 2 
                )
                + 
                math.pow(
                    (area[1]/2 - area[1]*PROPORCAO[2]), 2
                )
    )
    #

    ## Algoritmo
    tt.left(math.pi - math.asin((area[1]/2 - area[1]*PROPORCAO[2])/ lado))

    tt.fillcolor("yellow")
    tt.begin_fill()
    for _ in range(1, 5, 1):
        tt.forward(lado)
        tt.left((
            math.pi - 2*math.asin((area[0]/2 - area[1]*PROPORCAO[2])/ lado),
            math.pi - 2*math.asin((area[1]/2 - area[1]*PROPORCAO[2])/ lado) 
        )[not _%2])
    tt.end_fill()
    
    tt.right(math.pi - math.asin((area[1]/2 - area[1]*PROPORCAO[2])/ lado)) # Voltar a inclinação antiga
    #

    return

def retangulo(tt: t.Turtle, area:list[float]) -> None:
    ###
    """
    Aqui é responsável por fazer um retângulo na parte central da tela.
    O algoritmo foi pensado para cada iteração do loop. O valor será ímpar/par e acessando dimensões diferentes (x,y)
    """
    ###

    ## Algoritmo
    tt.fillcolor("green")
    tt.begin_fill()

    for _ in range(4):
        tt.forward( area[_%2] )
        tt.right(math.pi/2)

    tt.end_fill()
    #

    return

def circulo(tt: t.Turtle, area: list[float], PROPORCAO:tuple[float, float, float, float, float]) -> None:
    ###
    """
    Aqui é responsável por fazer a parte da bola azul da bandeira
    Para fazer a bola, será usado o .circle() e será centralizada usando -> Ponto(-area[0]/2, area[1]/2)
    """
    ###

    ## Algoritmo

    tt.fillcolor("blue")
    tt.begin_fill()
    tt.circle(area[1] * PROPORCAO[4] / 2)
    tt.end_fill()
    #
    

def main():
    ## Declarações
    area:list[float]
    resolucao:list[float]
    tt: t.Turtle
    # DimensãoX | DimensãoY | DistLosango | GrossuraFaixa | TamBola
    # Dist&Grossura&Tam -> relacionados com a DimensãoY
    PROPORCAO = ( 7/12, 10/12, 0.1214285714, 0.0357142857, 0.5)
    #

    ## Algoritmo
    t.Screen().setup(1.0, 1.0)
    area = [t.window_width()*PROPORCAO[0], t.window_height()*PROPORCAO[1]] # Proporção de 7:10
    
    tt = t.Turtle()
    tt.radians()
    tt.speed(10)

    # Retângulo principal
    tt.penup()
    tt.goto(Ponto(-area[0]/2, area[1]/2)) # Centralização do retângulo
    tt.pendown()
    retangulo(tt, area)
    #

    # Losango
    tt.penup()
    tt.goto(Ponto(-area[0]/2, 0))
    tt.forward(area[0] - (PROPORCAO[2] * area[1]))
    tt.pendown()
    losango(tt, area, PROPORCAO)
    #

    # Circulo
    tt.penup()
    tt.goto(Ponto(-area[0]/2, -area[1]/4))
    tt.forward(area[0]/2)
    tt.pendown()
    circulo(tt, area, PROPORCAO)
    #
    
    t.mainloop()
    #


if __name__ == "__main__": main()

## Onde foi que eu errei -> Leandro e Leonardo
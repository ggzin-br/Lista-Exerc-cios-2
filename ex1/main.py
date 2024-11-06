## Biblioteca
import Circulo
import Quadrado
import turtle
#

def main():
    Circulo.Circulo(100000, "red").desenhar()
    Quadrado.Quadrado(100000, "red").desenhar()
    turtle.mainloop()

if __name__ == "__main__": main()
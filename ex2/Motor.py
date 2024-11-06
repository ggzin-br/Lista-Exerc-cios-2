class Motor:
    ## Atributos
    modeloM:str
    cilindrada:str
    def __init__(self, modelo:str, cilindrada:str) -> None:
        self.modeloM = modelo
        self.cilindrada = cilindrada
    #

    ## Métodos
    def status(self) -> str:
        return "O motor {} | {}cc existe!".format(self.modeloM, self.cilindrada)
    #
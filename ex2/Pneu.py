class Pneu:
    ## Atributos
    modeloP:str
    medida:str
    def __init__(self, modelo:str, medida:str) -> None:
        self.modeloP = modelo
        self.medida = medida
    #

    ## Métodos
    def status(self) -> str:
        return "O pneu {} | {} existe!".format(self.modeloP, self.medida)
    #
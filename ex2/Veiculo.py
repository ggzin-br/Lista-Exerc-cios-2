## Bibliotecas
from Pneu import Pneu
from Motor import Motor
#

class Veiculo(Motor, Pneu):
    ## Atributos
    modeloCarro:str
    def __init__(self, modeloCarro: str, modeloMotor: str, modeloPneu: str, medidaPneu: str, cilindrada: str) -> None:

        # O super somente inicializa a primeira classe da herança (Motor)
        Motor.__init__(self, modeloMotor, cilindrada)
        Pneu.__init__(self, modeloPneu, medidaPneu)

        self.modeloCarro = modeloCarro
    #

    ## Métodos
    def status(self) -> str:
        return f"""
        Modelo carro: {self.modeloCarro}

        \tMotor
        {Motor.status(self)}

        \tPneu
        {Pneu.status(self)}
        """
        # Para inicializar a outra, é necessário fazer isto

    #
    
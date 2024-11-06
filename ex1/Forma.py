from abc import ABC, abstractmethod

class Forma(ABC):
    ## Atributos
    cor:str
    area:float
    #

    ## Métodos
    @abstractmethod
    def desenhar(self) -> None: ...
    #

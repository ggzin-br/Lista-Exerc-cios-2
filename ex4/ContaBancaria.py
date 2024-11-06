from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    ## Atributos
    _numConta: str # Um "_" significa protected
    _titular: str
    _saldo: float
    #

    # Se caso der erro em alguma das operações, será lançado um False no retorno
    ## Métodos
    def depositar(self, valor:float) -> bool: 
        if valor > 0:
            self._saldo += valor
            return True
        return False

    @abstractmethod
    def sacar(self) -> bool: ... 

    @property
    @abstractmethod
    def infConta(self) -> str: ...

    @property
    def getSaldo(self) -> float: 
        return self._saldo
    #
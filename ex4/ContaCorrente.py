## Bibliotecas
from ContaBancaria import ContaBancaria
#

class ContaCorrente(ContaBancaria):
    ## Atributos
    _chequeEspecial: float
    def __init__(self, numConta: str, titular:str, chequeEspecial: float, saldoInicial:float=0) -> None:
        super().__init__() # Inicializar classe pai

        self._numConta = numConta
        self._titular = titular
        self._saldo = saldoInicial
        self._chequeEspecial = chequeEspecial
    #

    ## Métodos
    def sacar(self, valor:float) -> bool:
        if valor <= 0: return False

        if (self._saldo - valor) >= 0: 
            self._saldo -= valor
        elif (self._saldo + self._chequeEspecial - valor) >= 0: # Operaçao válida
            self._saldo -= valor
        else:
            return False
        
        return True

    @property
    def infConta(self) -> str:
        return f"""
        Titular da Conta: {self._titular}
        Número da Conta: {self._numConta}
        
        Cheque Especial: {self._chequeEspecial}
        Saldo: {self._saldo}
        """
    #
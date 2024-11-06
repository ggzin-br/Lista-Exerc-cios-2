## Bibliotecas
from ContaBancaria import ContaBancaria
#

class ContaPoupanca(ContaBancaria):
    ## Atributos
    _valJuros: float
    def __init__(self, numConta: str, titular: str, valJuros: float, saldoInicial:float=0) -> None:
        super().__init__() # Inicializar classe pai

        self._numConta = numConta
        self._titular = titular
        self._saldo = saldoInicial * valJuros + saldoInicial
        self._valJuros = valJuros
    #

    ## Métodos
    def sacar(self, valor:float) -> bool: # -> A cada saque será computado mais e mais juros
        if valor <= 0: return False

        if (self._saldo - valor) >= 0: 
            self._saldo -= valor 
            self._saldo *= self._valJuros + self._saldo
        else:
            return False
        
        return True

    @property
    def infConta(self) -> str:
        return f"""
        Titular da Conta: {self._titular}
        Número da Conta: {self._numConta}
        
        Porcentagem dos jurus: {self._valJuros}
        Saldo: {self._saldo}
        """
    #
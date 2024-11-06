## Bibliotecas
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
#

def main():
    ## Atributos
    corrente = ContaCorrente("12345678-9", "Pedro", 500)
    poupanca = ContaPoupanca("18261831-1", "Fábio", 0.04, 100)
    #

    ## Algoritmo
    
    ## ContC
    print(corrente.infConta)
    
    corrente.depositar(1000)
    print(corrente.getSaldo)

    if not corrente.sacar(1600): # Acima do limite do cheque especial
        print("Operação não permitida")

    corrente.sacar(1500)
    print(corrente.infConta)
    #

    ## ContP
    print(poupanca.infConta)
    
    poupanca.depositar(900)
    print(poupanca.getSaldo)

    if not poupanca.sacar(1600): # Acima do saldo da conta
        print("Operação não permitida")

    poupanca.sacar(1000)
    print(poupanca.infConta)
    #

    #
    

if __name__ == "__main__": main()
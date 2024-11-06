## Bibliotecas
import Veiculo, Pneu, Motor
#

def main():
    vw_up = Veiculo.Veiculo("VW Up! (Altas Aventuras)", "Audi", "Pirelli", "175/65-70", "999")
    print(vw_up.status())
    

if __name__ == "__main__": main()
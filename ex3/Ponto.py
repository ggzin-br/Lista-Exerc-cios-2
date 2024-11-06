from typing import Iterator


class Ponto:
    x:float; y:float
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y
    
    # Essa função deixa o objeto iterável
    def __iter__(self):
        for _ in self.__getstate__(): # Isso aqui retorna a chave/valor do objeto
            yield self.__dict__.get(_) # Isso aqui pega o valor de um atributo do objeto
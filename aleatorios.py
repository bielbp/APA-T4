"""
Cuarta tarea de APA - Generación de números aleatorios

Biel Bernal Pratdesaba

"""
class Aleat:
    """
    Classe Aleat que implementa un generador de numeros aleatorios
    en el rango 0 <= x_n <m usando el método LGC.

    >>> rand = Aleat(m=32, a=9, c=13, X0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1

    """
    
    def __init__(self, *, m = 2 ** 48, a = 25214903917, c = 11, X0 = 1212121):
        """
        Costructor de la clase Aleat. Inicializa los parametros del
        generador.
        """
        self.m = m
        self.a = a
        self.c = c
        self.x = X0
        return None
    
    def __next__(self):
        """
        Método magico que genera el siguiente número aleatorio usando el algoritmo LGC.
        """
        self.x = (self.a * self.x + self.c) % self.m
        return self.x
    
    def __call__(self, X0):
        """
        Método mágico que sebrecarga la llamda a funcion.
        """
        self.x = X0
        return 
    
def aleat(*, m=2**48, a=25214903917, c=11, X0=1212121):
    """
    Funcion generadora.

    >>> rand = aleat(m=64, a=5, c=46, X0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    x = X0
    while True:
        x = (a * x + c) % m
        aux = yield(x)
        if aux is not None:
            x = aux
    
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
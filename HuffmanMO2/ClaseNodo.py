class Nodo:
    def __init__(self, simbolo=None, freq=0, izq=None, der=None):
        self.simbolo = simbolo
        self.freq = freq
        self.izq = izq
        self.der = der

    def __lt__(self, otro):
        return self.freq < otro.freq
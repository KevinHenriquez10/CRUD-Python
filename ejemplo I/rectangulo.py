class rectangulo: 
    base=0
    altura=0

    def __init__(self, valorBase, valorAltura):
        self.base=valorBase
        self.altura=valorAltura

    def calcularPerimetro(self):
        p= (self.base*2)+(self.altura*2)
        return p

    def calcularArea(self):
        a=self.base*self.altura
        return a
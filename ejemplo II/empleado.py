class empleado:
    nombre=""
    dias=0
    salarioBasico=0

    def __init__(self, valNombre, valDias, valSalarioBasico):
        self.nombre=valNombre
        self.dias=valDias
        self.salarioBasico=valSalarioBasico

    def obtener_nombre(self):
        return self.nombre

    def calcular_devengado(self):
        sd=self.salarioBasico*self.dias/30
        return sd

    def calcular_auxilio(self):
        aux = 112000*self.dias/30
        return aux
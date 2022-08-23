class estudiante:

    nombre=""
    notaFI=0
    notaPI=0
    notaFII=0
    notaPII=0
    notaFIII=0
    notaPIII=0

    def __init__(self, vNombre, vNotaFI, vNotaPI, vNotaFII, vNotaPII, vNotaFIII, vNotaPIII):
        self.nombre=vNombre
        self.notaFI=vNotaFI
        self.notaPI=vNotaPI
        self.notaFII=vNotaFII
        self.notaPII=vNotaPII
        self.notaFIII=vNotaFIII
        self.notaPIII=vNotaPIII

    def mostrarNombre(self):
        return self.nombre

    def calcular_corteI(self):
        c1=self.notaFI*0.40+self.notaPI*0.60
        return c1
    def calcular_corteII(self):
        c2=self.notaFII*0.30+self.notaPII*0.70
        return c2
    def calcular_corteIII(self):
        c3=self.notaFIII*0.50+self.notaPIII*0.50
        return c3
    def calcular_notaFinal(self):
        n_final=(self.notaFI*0.40+self.notaPI*0.60)*0.30+(self.notaFII*0.30+self.notaPII*0.70)*0.30+(self.notaFIII*0.50+self.notaPIII*0.50)*0.40
        return n_final
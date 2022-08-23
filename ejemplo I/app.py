from rectangulo import *

base = float(input("Digite el valor de la base del rectangulo: "))
altura = float(input("Digite el valor de la altura del rectangulo: "))
rec = rectangulo(base, altura)
perimetro = rec.calcularPerimetro()
area = rec.calcularArea()
print(f"El valor del perimetro del rectangulo es de: {perimetro} y el valor del area es de: {area}") 
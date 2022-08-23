from estudiante import *

nombre = input("Digite su nombre completo: ")
notaFI = float(input("Digite la nota formativa I: "))
notaPI = float(input("Digite la nota parcial I: "))
notaFII = float(input("Digite la nota formativa II: "))
notaPII = float(input("Digite la nota parcial II: "))
notaFIII = float(input("Digite la nota formativa III: "))
notaPIII = float(input("Digite la nota parcial III: "))

est  = estudiante(nombre, notaFI, notaPI, notaFII, notaPII, notaFIII, notaPIII)
nombre_estudiante = est.mostrarNombre()
corteI = est.calcular_corteI()
corteII = est.calcular_corteII()
corteIII = est.calcular_corteIII()
final = est.calcular_notaFinal()

print(f"El estudiante {nombre_estudiante} tiene nota en el corte I de {corteI} nota en corte II de {corteII} nota en corte III de {corteIII} y una nota definitiva de {final}")
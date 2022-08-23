from empleado import *

nombre = input("Digite su nombre completo: ")
dias = int(input("Digite los días laborados: "))
salarioBase = int(input("Digite el valor de su salario base: "))

emp = empleado(nombre, dias, salarioBase)
r_nombre = emp.obtener_nombre()
r_sdevengado = emp.calcular_devengado()
r_auxilio = emp.calcular_auxilio()

print(f"El empleado {r_nombre} tiene un salario devengado de ${r_sdevengado} pesos y un auxilio de transporte por valor de ${r_auxilio} pesos")
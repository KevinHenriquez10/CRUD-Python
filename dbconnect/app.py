import os
from db import DAO
from funciones_utiles import funciones

def menuPrincipal():
    continuar = True
    while (continuar):
        opcionCorrecta=False
        while (not opcionCorrecta):
            print("|*******************************************************************************************************|\n"
            "|*********************     Bienvenido a su software de peliculas y series online    ********************|\n"
            "|*********************                                                              ********************|\n"
            "|*********************                 1. Listar Titulos.                           ********************|\n"
            "|*********************                 2. Agregar Titulos.                          ********************|\n"
            "|*********************                 3. Modificar Titulos.                        ********************|\n"
            "|*********************                 4. Eliminar Titulos.                         ********************|\n"
            "|*********************                 5. Salir.                                    ********************|\n"
            "|*********************                                                              ********************|\n"
            "|*******************************************************************************************************|")
            opcion = int(input("Ingrese la opción a seleccionar: "))
            if opcion <1 or opcion >5:
                os.system("cls")
                print("La opción seleccionada no es correcta \n")
            elif(opcion == 5):
                continuar = False
                os.system("cls")
                print("Gracias por usar nuestra app!")
                break
            else:
                os.system("cls")
                opcionCorrecta=True
                ejecutarOpcion(opcion)
    

def ejecutarOpcion(opcion):
        dao = DAO()
        fun = funciones
        if opcion == 1:
            lista = dao.listar()
            fun.listarTitulos(lista)
        elif opcion == 2:
            titulo = funciones.getTitulo()
            dao.registrar(titulo)
        elif opcion == 3:
            titulo = funciones.getTitulo()
            dao.actualizar(titulo)
        elif opcion == 4:
            cod = input("Ingrese el codigo del titulo a eliminar: ")
            codigo = funciones.validarCodigo(cod)
            lista = dao.listar()
            for li in lista:
                print(li)
                if int(codigo) == li[1]:
                    print(cod)
                    dao.eliminar(codigo)
                    return False
            print("EL titulo no se encuentra registrado en la base de datos! ")


menuPrincipal()


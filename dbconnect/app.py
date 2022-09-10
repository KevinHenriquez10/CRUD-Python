import os
from funciones_utiles import funciones

def menuPrincipal():
    continuar = True
    while (continuar):
        opcionCorrecta=False
        while (not opcionCorrecta):
            print("|*******************************************************************************************************|\n"
            "|*********************     Bienvenido a su software educativo en linea              ********************|\n"
            "|*********************                                                              ********************|\n"
            "|*********************                 1. Gestionar Alumnos.                        ********************|\n"
            "|*********************                 2. Gestionar Profesores.                     ********************|\n"
            "|*********************                 3. Gestionar Cursos.                         ********************|\n"
            "|*********************                 4. Gestionar Periodos.                       ********************|\n"
            "|*********************                 5. Salir.                                    ********************|\n"
            "|*********************                                                              ********************|\n"
            "|*******************************************************************************************************|")
            opcion = int(input("Ingrese la opción a seleccionar: "))
            if opcion <1 or opcion >4:
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
    if opcion==1:
        continuar = True
        while (continuar):
            opcionCorrecta=False
            while (not opcionCorrecta):
                print("|*******************************************************************************************************|\n"
                "|*********************     Bienvenido a su software educativo en linea              ********************|\n"
                "|*********************                                                              ********************|\n"
                "|*********************                 1. Listar Alumnos.                           ********************|\n"
                "|*********************                 2. Agregar Alumnos.                          ********************|\n"
                "|*********************                 3. Actualizar Alumnos.                       ********************|\n"
                "|*********************                 4. Eliminar Alumnos.                         ********************|\n"
                "|*********************                 5. Menú Principal.                           ********************|\n"
                "|*********************                                                              ********************|\n"
                "|*******************************************************************************************************|")
                opcion = int(input("Ingrese la opción a seleccionar: "))
                if opcion <1 or opcion >5:
                    os.system("cls")
                    print("La opción seleccionada no es correcta \n")
                elif(opcion == 5):
                    continuar = False
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    opcionCorrecta=True
                    funciones.menuEstudiantes(opcion)
    if opcion==2:
        continuar = True
        while (continuar):
            opcionCorrecta=False
            while (not opcionCorrecta):
                print("|*******************************************************************************************************|\n"
                "|*********************     Bienvenido a su software educativo en linea              ********************|\n"
                "|*********************                                                              ********************|\n"
                "|*********************                 1. Listar Profesor.                          ********************|\n"
                "|*********************                 2. Agregar Profesor.                         ********************|\n"
                "|*********************                 3. Actualizar Profesor.                      ********************|\n"
                "|*********************                 4. Eliminar Profesor.                        ********************|\n"
                "|*********************                 5. Menú Principal.                           ********************|\n"
                "|*********************                                                              ********************|\n"
                "|*******************************************************************************************************|")
                opcion = int(input("Ingrese la opción a seleccionar: "))
                if opcion <1 or opcion >5:
                    os.system("cls")
                    print("La opción seleccionada no es correcta \n")
                elif(opcion == 5):
                    continuar = False
                    os.system("cls")
                    break
                else:
                    os.system("cls")
                    opcionCorrecta=True
                    funciones.menuProfesores(opcion)
    if opcion==3:
        continuar = True
        while (continuar):
            opcionCorrecta=False
            while (not opcionCorrecta):
                print("|*******************************************************************************************************|\n"
                "|*********************     Bienvenido a su software educativo en linea              ********************|\n"
                "|*********************                                                              ********************|\n"
                "|*********************                 1. Listar Cursos.                            ********************|\n"
                "|*********************                 2. Agregar Cursos.                           ********************|\n"
                "|*********************                 3. Actualizar Cursos.                        ********************|\n"
                "|*********************                 4. Eliminar Cursos.                          ********************|\n"
                "|*********************                 5. Menú Principal.                           ********************|\n"
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
                    funciones.menuCursos(opcion)
    
    if opcion==4:
        continuar = True
        while (continuar):
            opcionCorrecta=False
            while (not opcionCorrecta):
                print("|*******************************************************************************************************|\n"
                "|*********************     Bienvenido a su software educativo en linea              ********************|\n"
                "|*********************                                                              ********************|\n"
                "|*********************                 1. Listar Periodos.                          ********************|\n"
                "|*********************                 2. Agregar Periodos.                         ********************|\n"
                "|*********************                 3. Actualizar Periodos.                      ********************|\n"
                "|*********************                 4. Eliminar Periodos.                        ********************|\n"
                "|*********************                 5. Menú Principal.                           ********************|\n"
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
                    funciones.menuPeriodos(opcion)


menuPrincipal()


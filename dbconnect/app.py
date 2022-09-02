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
            "|*********************                 1. Listar Alumnos.                           ********************|\n"
            "|*********************                 2. Listar Profesores.                        ********************|\n"
            "|*********************                 3. Agregar Alumnos.                          ********************|\n"
            "|*********************                 4. Agregar Profesores.                       ********************|\n"
            "|*********************                 5. Actualizar Alumnos.                       ********************|\n"
            "|*********************                 6. Actualizar Profesores.                    ********************|\n"
            "|*********************                 7. Eliminar Alumnos.                         ********************|\n"
            "|*********************                 8. Eliminar Profesores.                      ********************|\n"
            "|*********************                 9. Salir.                                    ********************|\n"
            "|*********************                                                              ********************|\n"
            "|*******************************************************************************************************|")
            opcion = int(input("Ingrese la opción a seleccionar: "))
            if opcion <1 or opcion >8:
                os.system("cls")
                print("La opción seleccionada no es correcta \n")
            elif(opcion == 9):
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
            lista = dao.listarAlumnos()
            fun.listarAlumnos(lista)
        elif opcion == 2:
            lista = dao.listarProfesores()
            fun.listarProfesores(lista)
        elif opcion == 3:
            alumno = funciones.getAlumno()
            dao.registrarAlumno(alumno)
        elif opcion == 4:
            profesor = funciones.getProfesor()
            dao.registrarProfesor(profesor)
        elif opcion == 5:
            alumno = funciones.getAlumno()
            id = int(input("Ingrese el id del alumno a actualizar: "))
            dao.actualizarAlumno(alumno, id)
        elif opcion == 6:
            profesor = funciones.getProfesor()
            id = int(input("Ingrese el id del profesor a actualizar: "))
            dao.actualizarProfesor(profesor, id)
        elif opcion == 7:
            id = int(input("Ingrese el id del alumno a eliminar: "))
            lista = dao.listarAlumnos()
            for alumno in lista:
                if(alumno[0] == id):
                    dao.eliminarAlumno(id)
                else:
                    print("No se encontró el alumno a eliminar!")
        elif opcion == 8:
            id = int(input("Ingrese el id del profesor a eliminar: "))
            lista = dao.listarProfesores()
            for profesor in lista:
                if(profesor[0] == id):
                    dao.eliminarProfesor(id)
                else:
                    print("No se encontró el profesor a eliminar!")

menuPrincipal()


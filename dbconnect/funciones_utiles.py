import datetime
import os

from db import DAO

class funciones:
    nombre=""
    apellido=""
    fecha_nacimiento="1950-01-01"
    tipo_identificacion=""
    identificacion=""
    direccion=""
    telefono=""
    email=""

    def __init__(self, vNombre, vApellido, vFecha_nacimiento, vTipo_identificacion, vIdentificacion, vDireccion, vTelefono, vEmail):
        self.nombre = vNombre
        self.apellido = vApellido
        self.fecha_nacimiento=vFecha_nacimiento
        self.tipo_identificacion = vTipo_identificacion
        self.identificacion = vIdentificacion
        self.direccion = vDireccion
        self.telefono=vTelefono
        self.email = vEmail
    
    def validarCodigo(codigo):
        if(codigo.isnumeric() and len(codigo) == 6):
            return codigo
        else:
            valido = False
            while not valido:
                codigo = input("Ingrese un codigo valido (numeros de 6 digitos): ")
                if(codigo.isnumeric() and len(codigo) == 6):
                    valido = True
                    return codigo

    def getAlumno():
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        fecha_nacimiento = str(input("Ingrese la fecha de nacimiento ('YYYY-MM-DD'): "))
        valido=False
        while not valido:
            try:
                datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
                valido=True
            except ValueError:
                fecha_nacimiento = str(input("Fecha incorrecta, el formato debe ser así ('YYYY-MM-DD')(2000-12-31): "))
        tipo_identificacion = input("Ingrese su tipo de identificacion: (C.C), (T.I), (PASAPORTE), (Registro Civil): ")
        valido = False
        if(tipo_identificacion == "C.C" or tipo_identificacion == "T.I" or tipo_identificacion == "PASAPORTE" or tipo_identificacion == "Registro Civil"):
            valido == True
        else:
            while not valido:
                tipo_identificacion = input("Ingrese su tipo de identificacion: (C.C), (T.I), (PASAPORTE), (Registro Civil): ")
                if(tipo_identificacion == "C.C" or tipo_identificacion == "T.I" or tipo_identificacion == "PASAPORTE" or tipo_identificacion == "Registro Civil"):
                    valido == True
        identificacion = input("Ingrese su identificacion: ")
        direccion = input("Ingrese su dirección: ")
        telefono = input("Ingrese su telefono: ")
        email = input("Ingrese su email: ")

        alumno = (nombre, apellido, fecha_nacimiento, tipo_identificacion, identificacion, direccion, telefono, email)
        return alumno
    
    def getProfesor():
        nombre = input("Ingrese el nombre del profesor: ")
        apellido = input("Ingrese el apellido del profesor: ")
        fecha_nacimiento = str(input("Ingrese la fecha de nacimiento ('YYYY-MM-DD'): "))
        valido=False
        while not valido:
            try:
                datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()
                valido=True
            except ValueError:
                fecha_nacimiento = str(input("Fecha incorrecta, el formato debe ser así ('YYYY-MM-DD')(2000-12-31): "))
        tipo_identificacion = input("Ingrese su tipo de identificacion: (C.C), (PASAPORTE), (C.E): ")
        valido = False
        if(tipo_identificacion == "C.C" or tipo_identificacion == "PASAPORTE" or tipo_identificacion == "C.E"):
            valido == True
        else:
            while not valido:
                tipo_identificacion = input("Ingrese su tipo de identificacion: (C.C), (T.I), (PASAPORTE), (Registro Civil): ")
                if(tipo_identificacion == "C.C" or tipo_identificacion == "PASAPORTE" or tipo_identificacion == "C.E"):
                    valido == True
        identificacion = input("Ingrese su identificacion: ")
        direccion = input("Ingrese su dirección: ")
        telefono = input("Ingrese su telefono: ")
        email = input("Ingrese su email: ")

        profesor = (nombre, apellido, fecha_nacimiento, tipo_identificacion, identificacion, direccion, telefono, email)
        return profesor
    
    def getCurso():
        codigo = input("Ingrese el codigo del curso: ")
        valido=False
        while not valido:
            try:
                if(codigo.isnumeric() and len(codigo)==6):
                    valido=True
            except ValueError:
                codigo = input("Ingrese el codigo del curso: ")
        nombre = input("Ingrese el nombre del curso: ")
        creditos = input("Ingrese los creditos del curso: ")
        curso = (codigo, nombre, creditos)
        return curso

    def getPeriodo():
        dao = DAO()
        fun = funciones
        lista = dao.listarCursos()
        fun.listarCursos(lista)
        idCurso = input("Ingrese el identificador del curso: ")
        lista = dao.listarAlumnos()
        fun.listarAlumnos(lista)
        idAlumno = input("Ingrese el identificador del alumno: ")
        lista = dao.listarProfesores()
        fun.listarProfesores(lista)
        idProfesor = input("Ingrese el identificador del profesor: ")
        fecha_inicio = str(input("Ingrese la fecha de inicio ('YYYY-MM-DD'): "))
        valido=False
        while not valido:
            try:
                datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
                valido=True
            except ValueError:
                fecha_inicio = str(input("Fecha incorrecta, el formato debe ser así ('YYYY-MM-DD')(2000-12-31): "))
        periodo = (idCurso, idAlumno, idProfesor, fecha_inicio)
        return periodo
    
    def listarAlumnos(lista):
        print("Alumnos: \n")
        cont = 1
        if(len(lista)==0):
            print("No hay datos para mostrar...")
        else:
            for alumno in lista:
                datos = "{0}. id: {1} | Nombre: {2} | Apellido: {3} | Fecha de Nacimiento: {4} | Tipo de Identificación: {5} | Identificación: {6} | Dirección: {7} | Telefono: {8} | Email: {9}"
                print(datos.format(cont, alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], alumno[5], alumno[6], alumno[7], alumno[8]))
                cont +=1
                print(" ")

    def listarProfesores(lista):
        print("Profesores: \n")
        cont = 1
        if(len(lista)==0):
            print("No hay datos para mostrar...")
        else:
            for profesor in lista:
                datos = "{0}. id: {1} | Nombre: {2} | Apellido: {3} | Fecha de Nacimiento: {4} | Tipo de Identificación: {5} | Identificación: {6} | Dirección: {7} | Telefono: {8} | Email: {9}"
                print(datos.format(cont, profesor[0], profesor[1], profesor[2], profesor[3], profesor[4], profesor[5], profesor[6], profesor[7], profesor[8]))
                cont +=1
                print(" ")

    def listarCursos(lista):
        print("Cursos: \n")
        cont = 1
        if(len(lista)==0):
            print("No hay datos para mostrar...")
        else:
            for curso in lista:
                datos = "{0}. id: {1} | Codigo: {2} | Nombre: {3} | Creditos: {4}"
                print(datos.format(cont, curso[0], curso[1], curso[2], curso[3]))
                cont +=1
                print(" ")

    def listarPeriodos(lista):
        print("Periodos: \n")
        cont = 1
        if(len(lista)==0):
            print("No hay datos para mostrar...")
        else:
            for periodo in lista:
                datos = "{0}. id: {1} | Alumno: {2} | Profesor: {3} | Curso: {4} | Fecha de Inicio: {5}"
                print(datos.format(cont, periodo[0], periodo[1], periodo[2], periodo[3], periodo[4]))
                cont +=1
                print(" ")

    def menuEstudiantes(opcion):
        dao = DAO()
        fun = funciones
        
        if opcion == 1:
            lista = dao.listarAlumnos()
            fun.listarAlumnos(lista)
        elif opcion == 2:
            alumno = funciones.getAlumno()
            dao.registrarAlumno(alumno)
        elif opcion == 3:
            lista = dao.listarAlumnos()
            fun.listarAlumnos(lista)
            alumno = funciones.getAlumno()
            id = int(input("Ingrese el id del alumno a actualizar: "))
            dao.actualizarAlumno(alumno, id)
        elif opcion == 4:
            estado = False
            lista = dao.listarAlumnos()
            fun.listarAlumnos(lista)
            id = int(input("Ingrese el id del alumno a eliminar: "))
            lista = dao.listarAlumnos()
            for alumno in lista:
                if(alumno[0] == id):
                    dao.eliminarAlumno(id)
                    estado = True
                    break
            if(estado == False):
                print("No se encontró el alumno a eliminar!")

    def menuProfesores(opcion):
        dao = DAO()
        fun = funciones
        
        if opcion == 1:
            lista = dao.listarProfesores()
            fun.listarProfesores(lista)
        elif opcion == 2:
            profesor = funciones.getProfesor()
            dao.registrarProfesor(profesor)
        elif opcion == 3:
            lista = dao.listarProfesores()
            fun.listarProfesores(lista)
            profesor = funciones.getProfesor()
            id = int(input("Ingrese el id del profesor a actualizar: "))
            dao.actualizarProfesor(profesor, id)
        elif opcion == 4:
            estado=False
            lista = dao.listarProfesores()
            fun.listarProfesores(lista)
            id = int(input("Ingrese el id del profesor a eliminar: "))
            lista = dao.listarProfesores()
            for profesor in lista:
                if(profesor[0] == id):
                    dao.eliminarProfesor(id)
                    estado=True
                    break
            if(estado==False):
                print("No se encontró el profesor a eliminar!")
    
    def menuCursos(opcion):
        dao = DAO()
        fun = funciones
        if opcion == 1:
            lista = dao.listarCursos()
            fun.listarCursos(lista)
        elif opcion == 2:
            alumno = funciones.getCurso()
            dao.registrarCurso(alumno)
        elif opcion == 3:
            lista = dao.listarCursos()
            fun.listarCursos(lista)
            curso = funciones.getCurso()
            id = int(input("Ingrese el id del curso a actualizar: "))
            dao.actualizarCurso(curso, id)
        elif opcion == 4:
            estado = False
            lista = dao.listarCursos()
            fun.listarCursos(lista)
            id = int(input("Ingrese el id del curso a eliminar: "))
            lista = dao.listarCursos()
            for curso in lista:
                if(curso[0] == id):
                    dao.eliminarCurso(id)
                    estado = True
                    break
            if(estado == False):
                print("No se encontró el curso a eliminar!")

    def menuPeriodos(opcion):
        dao = DAO()
        fun = funciones
        if opcion == 1:
            lista = dao.listarPeriodos()
            fun.listarPeriodos(lista)
        elif opcion == 2:
            periodo = funciones.getPeriodo()
            dao.registrarPeriodo(periodo)
        elif opcion == 3:
            periodo = funciones.getPeriodo()
            id = int(input("Ingrese el id del periodo a actualizar: "))
            dao.actualizarPeriodo(periodo, id)
        elif opcion == 4:
            estado = False
            lista = dao.listarPeriodos()
            fun.listarPeriodos(lista)
            id = int(input("Ingrese el id del periodo a eliminar: "))
            lista = dao.listarPeriodos()
            for periodo in lista:
                if(periodo[0] == id):
                    dao.eliminarPeriodo(id)
                    estado = True
                    break
            if(estado == False):
                print("No se encontró el periodo a eliminar!")



    
    

    
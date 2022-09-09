import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(user='KevCode', 
            password='KevCodeUniversidad', 
            host='universidad.csgqzknx8bvo.us-east-1.rds.amazonaws.com', 
            database='Colegio', 
            port='3306')

        except Error as ex:
            print('Error en la conexion con la base de datos: {0}'.format(ex))

    def listarAlumnos(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc('listar_alumnos')
                for result in cursor.stored_results():
                    return result.fetchall()
            except Error as ex:
                print('Error al listar los estudiantes: {0}'.format(ex))

    def listarProfesores(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.callproc('listar_profesores')
                for result in cursor.stored_results():
                    return result.fetchall()
            except Error as ex:
                print('Error al listar los profesores: {0}'.format(ex))

    def registrarAlumno(self, alumno):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('registrar_alumno', (alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], alumno[5], alumno[6], alumno[7]))
                self.conexion.commit()
                print("Estudiante creado satisfactoriamente! \n")
            except Error as ex:
               print('Error al registrar el estudiante: {0}'.format(ex)) 

    def registrarProfesor(self, profesor):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('registrar_profesor', (profesor[0], profesor[1], profesor[2], profesor[3], profesor[4], profesor[5], profesor[6], profesor[7]))
                self.conexion.commit()
                print("Profesor creado satisfactoriamente! \n")
            except Error as ex:
               print('Error al registrar el profesor: {0}'.format(ex)) 

    def eliminarAlumno(self, id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('eliminar_alumno', (id,))
                self.conexion.commit()
                print("Estudiante eliminado con exito! \n")
            except Error as ex:
                print('Error al eliminar el estudiante: {0}'.format(ex))
    
    def eliminarProfesor(self, id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('eliminar_profesor', (id,))
                self.conexion.commit()
                print("Profesor eliminado con exito! \n")
            except Error as ex:
                print('Error al eliminar el profesor: {0}'.format(ex))

    def actualizarAlumno(self, alumno, id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('actualizar_alumno',(alumno[0], alumno[1], alumno[2], alumno[3], alumno[4], alumno[5], alumno[6], alumno[7], id))
                self.conexion.commit()
                print("Alumno actualizado satisfactoriamente! \n")
            except Error as ex:
               print('Error al actualizar: {0}'.format(ex)) 

    def actualizarProfesor(self, profesor, id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.callproc('actualizar_profesor',(profesor[0], profesor[1], profesor[2], profesor[3], profesor[4], profesor[5], profesor[6], profesor[7], id))
                self.conexion.commit()
                print("Profesor actualizado satisfactoriamente! \n")
            except Error as ex:
               print('Error al actualizar: {0}'.format(ex))

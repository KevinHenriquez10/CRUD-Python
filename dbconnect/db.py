import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(user='KevCode', 
            password='KevCodeUniversidad', 
            host='universidad.csgqzknx8bvo.us-east-1.rds.amazonaws.com', 
            database='Universidad', 
            port='3306')

        except Error as ex:
            print('Error en la conexion con la base de datos: {0}'.format(ex))

    def listar(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM peliculas_series ORDER BY fecha ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print('Error al listar los titulos: {0}'.format(ex))

    def registrar(self, titulo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "INSERT INTO peliculas_series (codigo, titulo, fecha, calificacion) VALUES ('{0}', '{1}', '{2}', '{3}')"
                cursor.execute(query.format(titulo[0], titulo[1], titulo[2], titulo[3]))
                self.conexion.commit()
                print("Titulo creado satisfactoriamente! \n")
            except Error as ex:
               print('Error al registrar el titulo: {0}'.format(ex)) 

    def eliminar(self, codigo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "DELETE FROM peliculas_series WHERE codigo = {0}"
                cursor.execute(query.format(codigo))
                self.conexion.commit()
                print("Titulo eliminado con exito! \n")
            except Error as ex:
                print('Error al eliminar el titulo: {0}'.format(ex))

    def actualizar(self, titulo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                query = "UPDATE peliculas_series SET titulo='{0}', fecha='{1}', calificacion='{2}' WHERE codigo='{3}'"
                cursor.execute(query.format(titulo[1], titulo[2], titulo[3], titulo[0]))
                self.conexion.commit()
                print("Titulo actualizado satisfactoriamente! \n")
            except Error as ex:
               print('Error al actualizar: {0}'.format(ex)) 

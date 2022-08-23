import datetime

class funciones:

    codigo=0
    nombrePoS = ""
    fecha = "1950-01-01"
    clasificacion=0.0

    def __init__(self, vCodigo, vNombrePoS, vFecha, vCalificacion):
        self.codigo = vCodigo
        self.nombrePoS = vNombrePoS
        self.fecha=vFecha
        self.clasificacion = vCalificacion
    
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

    def getTitulo():
        codigo = input("Ingrese el codigo del titulo: ")
        valido = False
        if(codigo.isnumeric() and len(codigo) == 6):
            valido == True
        else:
            while not valido:
                codigo = input("Ingrese un codigo valido (numeros de 6 digitos): ")
                if(codigo.isnumeric() and len(codigo) == 6):
                    valido = True
        nombre = input("Ingrese el nombre del titulo: ")
        fecha = str(input("Ingrese la fecha del titulo ('YYYY-MM-DD'): "))
        valido=False
        while not valido:
            try:
                datetime.datetime.strptime(fecha, '%Y-%m-%d').date()
                valido=True
            except ValueError:
                fecha = str(input("Fecha incorrecta, el formato debe ser así ('YYYY-MM-DD')(2000-12-31): "))
        calificacion = input("Ingrese la calificación del titulo: ")
        valido = False
        while not valido:
            try:
                float(calificacion)
                valido = True
            except:
                calificacion = input("Ingrese una calificacion valida: ")

        titulo = (codigo, nombre, fecha, calificacion)
        return titulo
    

    
    def listarTitulos(lista):
        print("Titulos: \n")
        cont = 1
        for titulo in lista:
            datos = "{0}. Código: {1} | Titulo: {2} | Fecha Lanzamiento: {3} | Calificación: {4}"
            print(datos.format(cont, titulo[1], titulo[2], titulo[3], titulo[4]))
            cont +=1
            print(" ")



    
    

    
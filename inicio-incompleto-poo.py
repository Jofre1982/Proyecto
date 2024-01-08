import mysql.connector

class Conexion:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1121710953",
            database="colegio"
        )

    def obtener_conexion(self):
        return self.conexion

class Entidad:
    def __init__(self, usuario, contrasena, conexion):
        self.usuario = usuario
        self.contrasena = contrasena
        self.conexion = conexion

    def verificar_entidad(self):
        cursor = self.conexion.cursor()

        # comparar datos en la tabla estudiante
        consulta_estudiante = "SELECT EstudianteID FROM Estudiante WHERE Nombre = %s AND Contraseña = %s"
        cursor.execute(consulta_estudiante, (self.usuario, self.contrasena))
        resultado_estudiante = cursor.fetchone()
        if resultado_estudiante:
            return "Estudiante"

        # comparar datos en la tabla profesor
        consulta_profesor = "SELECT ProfesorID FROM Profesor WHERE Nombre = %s AND Contraseña = %s"
        cursor.execute(consulta_profesor, (self.usuario, self.contrasena))
        resultado_profesor = cursor.fetchone()
        if resultado_profesor:
            return "Profesor"

        # comparar datos en la tabla administrativo
        consulta_administrativo = "SELECT AdministrativoID FROM Administrativo WHERE Nombre = %s AND Contraseña = %s"
        cursor.execute(consulta_administrativo, (self.usuario, self.contrasena))
        resultado_administrativo = cursor.fetchone()
        if resultado_administrativo:
            return "Administrativo"
        
        cursor.close()
        return "No se encontró ninguna entidad con los datos de inicio de sesión proporcionados"

class Estudiante:
    def __init__(self):
        self.documento = input("Digite su documento de identificación: ")
        self.nombre = input("Digite su nombre: ")
        self.apellido = input("Digite su apellido: ")
        self.fecha_nacimiento = input("Digite su fecha de nacimiento: ")
        self.direccion = input("Digite su dirección: ")
        self.telefono = input("Digite su teléfono: ")
        self.correo = input("Digite su correo: ")
        self.grado = input("Digite su grado: ")

class Profesor:
    def __init__(self):
        self.documento = input("Digite su documento de identificación: ")
        self.nombre = input("Digite su nombre: ")
        self.apellido = input("Digite su apellido: ")
        self.fecha_nacimiento = input("Digite su fecha de nacimiento: ")
        self.direccion = input("Digite su dirección: ")
        self.telefono = input("Digite su teléfono: ")
        self.correo = input("Digite su correo: ")
        self.especialidad = input("Digite su materia de especialidad: ")

class Administrativo:
    def __init__(self):
        self.documento = input("Digite su documento de identificación: ")
        self.nombre = input("Digite su nombre: ")
        self.apellido = input("Digite su apellido: ")
        self.fecha_nacimiento = input("Digite su fecha de nacimiento: ")
        self.direccion = input("Digite su dirección: ")
        self.telefono = input("Digite su teléfono: ")
        self.correo = input("Digite su correo: ")
        self.puesto = input("Digite su puesto: ")

def registrarse(rol):
    if rol == "estudiante":
        estudiante = Estudiante()
    elif rol == "profesor":
        profesor = Profesor()
    elif rol == "administrativo":
        administrativo = Administrativo()

def inicio_sesion():
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    conexion = Conexion().obtener_conexion()
    entidad = Entidad(usuario, contrasena, conexion)
    entidad.verificar_entidad()

def home(opcion):
    if opcion == "iniciar sesion":
        inicio_sesion()
    elif opcion == "registrarse":
        rol = input("Ingrese su rol (estudiante, profesor, administrativo): ")
        registrarse(rol)

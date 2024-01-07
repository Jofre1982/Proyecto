import mysql.connector

class Conexion:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "1121710953"
        self.database = "colegio"
        self.conexion = None

    def establecer_conexion(self):
        self.conexion = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def cerrar_conexion(self):
        if self.conexion:
            self.conexion.close()

class Estudiante:
    def __init__(self):
        self.documento = None
        self.nombre = None
        self.apellido = None
        self.fecha_nacimiento = None
        self.direccion = None
        self.telefono = None
        self.correo = None
        self.grado = None

    def ingresar_datos(self):
        self.documento = input("Digite su documento de identificación: ")
        self.nombre = input("Digite su nombre: ")
        self.apellido = input("Digite su apellido: ")
        self.fecha_nacimiento = input("Digite su fecha de nacimiento: ")
        self.direccion = input("Digite su dirección: ")
        self.telefono = input("Digite su teléfono: ")
        self.correo = input("Digite su correo: ")
        self.grado = input("Digite su grado: ")

    def guardar_datos(self, conexion):
        cursor = conexion.conexion.cursor()
        consulta = "INSERT INTO Estudiante (Documento, Nombre, Apellido, FechaNacimiento, Direccion, Telefono, Correo, Grado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (self.documento, self.nombre, self.apellido, self.fecha_nacimiento, self.direccion, self.telefono, self.correo, self.grado)
        cursor.execute(consulta, datos)
        conexion.conexion.commit()
        cursor.close()

class Profesor:
    def __init__(self):
        self.documento = None
        self.nombre = None
        self.apellido = None
        self.fecha_nacimiento = None
        self.direccion = None
        self.telefono = None
        self.correo = None
        self.especialidad = None

    def ingresar_datos(self):
        self.documento = input("Digite su documento de identificación: ")
        self.nombre = input("Digite su nombre: ")
        self.apellido = input("Digite su apellido: ")
        self.fecha_nacimiento = input("Digite su fecha de nacimiento: ")
        self.direccion = input("Digite su dirección: ")
        self.telefono = input("Digite su teléfono: ")
        self.correo = input("Digite su correo: ")
        self.especialidad = input("Digite su materia de especialidad: ")

    def guardar_datos(self, conexion):
        cursor = conexion.conexion.cursor()
        consulta = "INSERT INTO Profesor (Documento, Nombre, Apellido, FechaNacimiento, Direccion, Telefono, Correo, Especialidad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (self.documento, self.nombre, self.apellido, self.fecha_nacimiento, self.direccion, self.telefono, self.correo, self.especialidad)
        cursor.execute(consulta, datos)
        conexion.conexion.commit()
        cursor.close()

class Administrativo:
    def __init__(self):
        self.documento = None
        self.nombre = None
        self.apellido = None
        self.fecha_nacimiento = None
        self.direccion = None
        self.telefono = None
        self.correo = None
        self.puesto = None

    def ingresar_datos(self):
        self.documento = input("Digite su documento de identificación: ")
        self.nombre = input("Digite su nombre: ")
        self.apellido = input("Digite su apellido: ")
        self.fecha_nacimiento = input("Digite su fecha de nacimiento: ")
        self.direccion = input("Digite su dirección: ")
        self.telefono = input("Digite su teléfono: ")
        self.correo = input("Digite su correo: ")
        self.puesto = input("Digite su puesto: ")

    def guardar_datos(self, conexion):
        cursor = conexion.conexion.cursor()
        consulta = "INSERT INTO Administrativo (Documento, Nombre, Apellido, FechaNacimiento, Direccion, Telefono, Correo, Puesto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (self.documento, self.nombre, self.apellido, self.fecha_nacimiento, self.direccion, self.telefono, self.correo, self.puesto)
        cursor.execute(consulta, datos)
        conexion.conexion.commit()
        cursor.close()

def verificar_entidad(usuario, contrasena, conexion):
    cursor = conexion.conexion.cursor()

    # comparar datos en la tabla estudiante
    consulta_estudiante = "SELECT EstudianteID FROM Estudiante WHERE Nombre = %s AND Contraseña = %s"
    cursor.execute(consulta_estudiante, (usuario, contrasena))
    resultado_estudiante = cursor.fetchone()
    if resultado_estudiante:
        return "Estudiante"

    # comparar datos en la tabla profesor
    consulta_profesor = "SELECT ProfesorID FROM Profesor WHERE Nombre = %s AND Contraseña = %s"
    cursor.execute(consulta_profesor, (usuario, contrasena))
    resultado_profesor = cursor.fetchone()
    if resultado_profesor:
        return "Profesor"

    # comparar datos en la tabla administrativo
    consulta_administrativo = "SELECT AdministrativoID FROM Administrativo WHERE Nombre = %s AND Contraseña = %s"
    cursor.execute(consulta_administrativo, (usuario, contrasena))
    resultado_administrativo = cursor.fetchone()
    if resultado_administrativo:
        return "Administrativo"
    
    cursor.close()
    return "No se encontró ninguna entidad con los datos de inicio de sesión proporcionados"

def registrarse(rol):
    conexion = Conexion()
    conexion.establecer_conexion()

    if rol == "estudiante":
        estudiante = Estudiante()
        estudiante.ingresar_datos()
        estudiante.guardar_datos(conexion)
    elif rol == "profesor":
        profesor = Profesor()
        profesor.ingresar_datos()
        profesor.guardar_datos(conexion)
    elif rol == "administrativo":
        administrativo = Administrativo()
        administrativo.ingresar_datos()
        administrativo.guardar_datos(conexion)

    conexion.cerrar_conexion()

def inicio_sesion():
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    conexion = Conexion()
    conexion.establecer_conexion()
    verificar_entidad(usuario, contrasena, conexion)
    conexion.cerrar_conexion()

def home(opcion):
    if opcion == "iniciar sesion":
        inicio_sesion()
    elif opcion == "registrarse":
        rol = input("Ingrese su rol (estudiante, profesor, administrativo): ")
        registrarse(rol)

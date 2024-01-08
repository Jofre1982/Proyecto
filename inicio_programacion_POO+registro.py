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
        self.EstudianteID = None
        self.nombre = None
        self.apellido = None
        self.FechaNacimiento = None
        self.direccion = None
        self.telefono = None
        self.CorreoElectronico = None
        self.CursoID = None

    def ingresar_datos(self):
        self.EstudianteID = input("Digite su EstudianteID de identificación: ")
        self.nombre = input("Digite su nombre: ")
        self.apellido = input("Digite su apellido: ")
        self.FechaNacimiento = input("Digite su fecha de nacimiento: ")
        self.direccion = input("Digite su dirección: ")
        self.telefono = input("Digite su teléfono: ")
        self.CorreoElectronico = input("Digite su CorreoElectronico: ")
        self.CursoID = input("Digite su CursoID: ")

    def guardar_datos(self, conexion):
        cursor = conexion.conexion.cursor()
        consulta = "INSERT INTO Estudiante (EstudianteID, Nombre, Apellido, FechaNacimiento, Direccion, Telefono, CorreoElectronico, CursoID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (self.EstudianteID, self.nombre, self.apellido, self.FechaNacimiento, self.direccion, self.telefono, self.CorreoElectronico, self.CursoID)
        cursor.execute(consulta, datos)
        conexion.conexion.commit()
        cursor.close()

class Profesor:
    def __init__(self):
        self.ProfesorID = None
        self.nombre = None
        self.apellido = None
        self.FechaNacimiento = None
        self.direccion = None
        self.telefono = None
        self.CorreoElectronico = None
        self.especialidad = None

    def ingresar_datos(self):
        self.ProfesorID = input("Digite su ProfesorID de identificación: ")
        self.nombre = input("Digite su nombre: ")
        self.apellido = input("Digite su apellido: ")
        self.FechaNacimiento = input("Digite su fecha de nacimiento: ")
        self.direccion = input("Digite su dirección: ")
        self.telefono = input("Digite su teléfono: ")
        self.CorreoElectronico = input("Digite su CorreoElectronico: ")
        self.especialidad = input("Digite su materia de especialidad: ")

    def guardar_datos(self, conexion):
        cursor = conexion.conexion.cursor()
        consulta = "INSERT INTO Profesor (ProfesorID, Nombre, Apellido, FechaNacimiento, Direccion, Telefono, CorreoElectronico, Especialidad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (self.ProfesorID, self.nombre, self.apellido, self.FechaNacimiento, self.direccion, self.telefono, self.CorreoElectronico, self.especialidad)
        cursor.execute(consulta, datos)
        conexion.conexion.commit()
        cursor.close()

class Administrativo:
    def __init__(self):
        self.AdministrativoID = None
        self.nombre = None
        self.apellido = None
        self.FechaNacimiento = None
        self.direccion = None
        self.telefono = None
        self.CorreoElectronico = None
        self.puesto = None

    def ingresar_datos(self):
        self.AdministrativoID = input("Digite su AdministrativoID de identificación: ")
        self.nombre = input("Digite su nombre: ")
        self.apellido = input("Digite su apellido: ")
        self.FechaNacimiento = input("Digite su fecha de nacimiento: ")
        self.direccion = input("Digite su dirección: ")
        self.telefono = input("Digite su teléfono: ")
        self.CorreoElectronico = input("Digite su CorreoElectronico: ")
        self.puesto = input("Digite su puesto: ")

    def guardar_datos(self, conexion):
        cursor = conexion.conexion.cursor()
        consulta = "INSERT INTO Administrativo (AdministrativoID, Nombre, Apellido, FechaNacimiento, Direccion, Telefono, CorreoElectronico, Puesto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (self.AdministrativoID, self.nombre, self.apellido, self.FechaNacimiento, self.direccion, self.telefono, self.CorreoElectronico, self.puesto)
        cursor.execute(consulta, datos)
        conexion.conexion.commit()
        cursor.close()

def verificar_entidad(usuario, contrasena, conexion):
    cursor = conexion.conexion.cursor()

    # comparar datos en la tabla Administrativo
    consulta_Administrativo = "SELECT AdministrativoID FROM Administrativo WHERE ID = %s AND Nombre = %s"
    cursor.execute(consulta_Administrativo, (contrasena, usuario))
    resultado_Administrativo = cursor.fetchone()
    if resultado_Administrativo:
        return "Administrativo"

    # comparar datos en la tabla profesor
    consulta_profesor = "SELECT ProfesorID FROM Profesor WHERE ID = %s AND Nombre = %s"
    cursor.execute(consulta_profesor, (contrasena, usuario))
    resultado_profesor = cursor.fetchone()
    if resultado_profesor:
        return "Profesor"

    # comparar datos en la tabla estudiante
    consulta_estudiante = "SELECT EstudianteID FROM Estudiante WHERE ID = %s AND Nombre = %s"
    cursor.execute(consulta_estudiante, (contrasena, usuario))
    resultado_estudiante = cursor.fetchone()
    if resultado_estudiante:
        return "Estudiante"
    
    cursor.close()
    return "No se encontró ninguna entidad con los datos de inicio de sesión proporcionados"


def registrarse(rol):
    conexion = Conexion()
    conexion.establecer_conexion()

    if rol == "Administrativo":
        administrativo = Administrativo()
        administrativo.ingresar_datos()
        administrativo.guardar_datos(conexion)
    elif rol == "profesor":
        profesor = Profesor()
        profesor.ingresar_datos()
        profesor.guardar_datos(conexion)
    elif rol == "estudiante":
        estudiante = Estudiante()
        estudiante.ingresar_datos()
        estudiante.guardar_datos(conexion)

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
        rol = input("Ingrese su rol (Administrativo, profesor, estudiante): ")
        registrarse(rol)

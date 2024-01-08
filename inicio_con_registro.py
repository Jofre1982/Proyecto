import mysql.connector

def establecer_conexion():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1121710953",
        database="colegio"
    )
    return conexion

def verificar_entidad(usuario, contrasena, conexion):
    cursor = conexion.cursor()

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

def estudiante(documento, nombre, apellido, fecha_nacimiento, direccion, telefono, correo, grado):
    documento = input("Digite su documento de identificación: ")
    nombre = input("Digite su nombre: ")
    apellido = input("Digite su apellido: ")
    fecha_nacimiento = input("Digite su fecha de nacimiento: ")
    direccion = input("Digite su dirección: ")
    telefono = input("Digite su teléfono: ")
    correo = input("Digite su correo: ")
    grado = input("Digite su grado: ")
    
    # Insertar datos en la tabla estudiante
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Estudiante (Documento, Nombre, Apellido, FechaNacimiento, Direccion, Telefono, Correo, Grado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    datos = (documento, nombre, apellido, fecha_nacimiento, direccion, telefono, correo, grado)
    cursor.execute(consulta, datos)
    conexion.commit()
    cursor.close()
    conexion.close()

def profesor(documento, nombre, apellido, fecha_nacimiento, direccion, telefono, correo, especialidad):
    documento = input("Digite su documento de identificación: ")
    nombre = input("Digite su nombre: ")
    apellido = input("Digite su apellido: ")
    fecha_nacimiento = input("Digite su fecha de nacimiento: ")
    direccion = input("Digite su dirección: ")
    telefono = input("Digite su teléfono: ")
    correo = input("Digite su correo: ")
    especialidad = input("Digite su materia de especialidad: ")
    
    # Insertar datos en la tabla profesor
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Profesor (Documento, Nombre, Apellido, FechaNacimiento, Direccion, Telefono, Correo, Especialidad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    datos = (documento, nombre, apellido, fecha_nacimiento, direccion, telefono, correo, especialidad)
    cursor.execute(consulta, datos)
    conexion.commit()
    cursor.close()
    conexion.close()

def administrativo(documento, nombre, apellido, fecha_nacimiento, direccion, telefono, correo):
    documento = input("Digite su documento de identificación: ")
    nombre = input("Digite su nombre: ")
    apellido = input("Digite su apellido: ")
    fecha_nacimiento = input("Digite su fecha de nacimiento: ")
    direccion = input("Digite su dirección: ")
    telefono = input("Digite su teléfono: ")
    correo = input("Digite su correo: ")
    puesto = input("Digite su puesto: ")
    
    # Insertar datos en la tabla administrativo
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Administrativo (Documento, Nombre, Apellido, FechaNacimiento, Direccion, Telefono, Correo, Puesto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    datos = (documento, nombre, apellido, fecha_nacimiento, direccion, telefono, correo, puesto)
    cursor.execute(consulta, datos)
    conexion.commit()
    cursor.close()
    conexion.close()

def registrarse(rol):
    if rol == "estudiante":
        estudiante()
    elif rol == "profesor":
        profesor()
    elif rol == "administrativo":
        administrativo()

def inicio_sesion():
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    conexion = establecer_conexion()
    verificar_entidad(usuario, contrasena, conexion)

def home(opcion):
    if opcion == "iniciar sesion":
        inicio_sesion()
    elif opcion == "registrarse":
        rol = input("Ingrese su rol (estudiante, profesor, administrativo): ")
        registrarse(rol)
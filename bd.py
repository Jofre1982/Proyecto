import mysql.connector

# Función para establecer la conexión a la base de datos
def establecer_conexion():
    return mysql.connector.connect(
        host="3386",
        user="root",
        password="Realmadrid1*",
        database="proyecto"
    )

# Función para verificar el inicio de sesión en la base de datos MySQL
def login(usuario, contrasena):
    conn = establecer_conexion()
    cursor = conn.cursor()

    # Verificar si el usuario y la contraseña coinciden en la base de datos
    query = "SELECT * FROM usuarios WHERE usuario=%s AND contrasena=%s"
    cursor.execute(query, (usuario, contrasena))
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        return True
    else:
        return False

# Función para agregar un nuevo usuario a la base de datos
def registrar_usuario(usuario, contrasena):
    conn = establecer_conexion()
    cursor = conn.cursor()

    # Verificar si el usuario ya existe
    query_verificar = "SELECT * FROM usuarios WHERE usuario=%s"
    cursor.execute(query_verificar, (usuario,))
    resultado_verificar = cursor.fetchone()

    if resultado_verificar:
        #("El usuario ya existe. Por favor, elige otro nombre de usuario.")
    else:
        # Insertar nuevo usuario en la base de datos
        query_insertar = "INSERT INTO usuarios (usuario, contrasena) VALUES (%s, %s)"
        cursor.execute(query_insertar, (usuario, contrasena))
        conn.commit()
            #("Registro exitoso. Ahora puedes iniciar sesión.")

    conn.close()






  
  
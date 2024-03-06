import mysql.connector

def ConexionBaseDeDatos():
    conexion = None
    try:
        conexion = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            database='clientesdb'
        )
        print("Conexión exitosa a la base de datos")
    except mysql.connector.Error as e:
        print(f"Error al conectarse a la base de datos: {e}")
    return conexion

class CConexion:
    def __init__(self):
        self.conexion = ConexionBaseDeDatos()
        if self.conexion is None:
            exit(1)  # Salir si no se puede conectar a la base de datos

# Ejemplo de uso
if __name__ == "__main__":
    mi_conexion = CConexion()
    # Aquí puedes usar mi_conexion.conexion para interactuar con la base de datos

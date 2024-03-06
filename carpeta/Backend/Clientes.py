from conexion import *

class Cclientes:

    def ingresarClientes(nombres,apellidos,sexo):

        try:
         cone = CConexion.ConexionBaseDeDatos()
         cursor = cone.cursor()
         sql ="insert into usuarios values(null,%s,%s,%s);"   

        except mysql.connector.Error as error:
            print("Error de ingreso de datos{}".format(error))    
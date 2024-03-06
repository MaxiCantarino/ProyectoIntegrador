<<<<<<< HEAD
from conexion import *

class Cclientes:

    def ingresarClientes(nombres,apellidos,sexo):

        try:
         cone = CConexion.ConexionBaseDeDatos()
         cursor = cone.cursor()
         sql ="insert into usuarios values(null,%s,%s,%s);"   

        except mysql.connector.Error as error:
=======
from conexion import *

class Cclientes:

    def ingresarClientes(nombres,apellidos,sexo):

        try:
         cone = CConexion.ConexionBaseDeDatos()
         cursor = cone.cursor()
         sql ="insert into usuarios values(null,%s,%s,%s);"   

        except mysql.connector.Error as error:
>>>>>>> 53f93dd75a7ceb6d18c2c431cb827f42caadc2c8
            print("Error de ingreso de datos{}".format(error))    
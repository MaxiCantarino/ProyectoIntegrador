<<<<<<< HEAD
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class FormularioClientes:
    def __init__(self):
        self.base = None
        self.textBoxId = None
        self.textBoxNombres = None
        self.textBoxApellidos = None
        self.combo = None
        self.groupBox = None
        self.tree = None

    def formulario(self):
        try:
            self.base = tk.Tk()
            self.base.geometry("600x400")
            self.base.title("Formulario Python")

            self.groupBox = ttk.LabelFrame(self.base, text="Datos del Personal", padding=(10, 10))
            self.groupBox.pack(padx=10, pady=10)

            labelId = ttk.Label(self.groupBox, text="Id:", width=10)
            labelId.grid(row=0, column=0, padx=5, pady=5)
            self.textBoxId = ttk.Entry(self.groupBox, width=30)
            self.textBoxId.grid(row=0, column=1, padx=5, pady=5)

            labelNombres = ttk.Label(self.groupBox, text="Nombres:", width=10)
            labelNombres.grid(row=1, column=0, padx=5, pady=5)
            self.textBoxNombres = ttk.Entry(self.groupBox, width=30)
            self.textBoxNombres.grid(row=1, column=1, padx=5, pady=5)

            labelApellidos = ttk.Label(self.groupBox, text="Apellidos:", width=10)
            labelApellidos.grid(row=2, column=0, padx=5, pady=5)
            self.textBoxApellidos = ttk.Entry(self.groupBox, width=30)
            self.textBoxApellidos.grid(row=2, column=1, padx=5, pady=5)

            labelSexo = ttk.Label(self.groupBox, text="Sexo:", width=10)
            labelSexo.grid(row=3, column=0, padx=5, pady=5)
            self.combo = ttk.Combobox(self.groupBox, values=["Masculino", "Femenino"], width=27)
            self.combo.grid(row=3, column=1, padx=5, pady=5)
            self.combo.set("Masculino")

            guardar_btn = ttk.Button(self.groupBox, text="Guardar", width=10, command=self.guardarRegistros)
            guardar_btn.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

            self.groupBox_lista = ttk.LabelFrame(self.base, text="Lista del Personal", padding=(10, 10))
            self.groupBox_lista.pack(padx=10, pady=10, fill="both", expand=True)

            self.tree = ttk.Treeview(self.groupBox_lista, columns=("Id", "Nombres", "Apellidos", "Sexo"), show='headings', height=5)
            self.tree.column("# 1", anchor=tk.CENTER, width=50)
            self.tree.heading("# 1", text="Id")
            self.tree.column("# 2", anchor=tk.CENTER, width=150)
            self.tree.heading("# 2", text="Nombres")
            self.tree.column("# 3", anchor=tk.CENTER, width=150)
            self.tree.heading("# 3", text="Apellidos")
            self.tree.column("# 4", anchor=tk.CENTER, width=100)
            self.tree.heading("# 4", text="Sexo")
            self.tree.pack(padx=10, pady=10, fill="both", expand=True)

            self.base.mainloop()

        except ValueError as error:
            print("Error al mostrar la interfaz, error: {}".format(error))

    def guardarRegistros(self):
        try:
            nombres = self.textBoxNombres.get()
            apellidos = self.textBoxApellidos.get()
            sexo = self.combo.get()

            conn = mysql.connector.connect(
                host='localhost',
                user='tu_usuario',
                password='tu_contraseña',
                database='clientesdb'
            )

            cursor = conn.cursor()
            sql = "INSERT INTO clientes (nombres, apellidos, sexo) VALUES (%s, %s, %s)"
            val = (nombres, apellidos, sexo)
            cursor.execute(sql, val)

            conn.commit()
            messagebox.showinfo("Información", "Datos guardados correctamente en la base de datos")
            
            self.actualizarLista()  # Actualizar la lista después de guardar

            cursor.close()
            conn.close()

            self.textBoxId.delete(0, tk.END)
            self.textBoxNombres.delete(0, tk.END)
            self.textBoxApellidos.delete(0, tk.END)

        except mysql.connector.Error as error:
            messagebox.showerror("Error", "Error al guardar los datos en la base de datos: {}".format(error))

    def actualizarLista(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='tu_usuario',
                password='tu_contraseña',
                database='clientesdb'
            )

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes")
            rows = cursor.fetchall()

            # Limpiar árbol antes de actualizar
            for row in self.tree.get_children():
                self.tree.delete(row)

            for row in rows:
                self.tree.insert("", tk.END, values=row)

            cursor.close()
            conn.close()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", "Error al actualizar la lista: {}".format(error))


if __name__ == "__main__":
    formulario_clientes = FormularioClientes()
    formulario_clientes.formulario()
=======
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class FormularioClientes:
    def __init__(self):
        self.base = None
        self.textBoxId = None
        self.textBoxNombres = None
        self.textBoxApellidos = None
        self.combo = None
        self.groupBox = None
        self.tree = None

    def formulario(self):
        try:
            self.base = tk.Tk()
            self.base.geometry("600x400")
            self.base.title("Formulario Python")

            self.groupBox = ttk.LabelFrame(self.base, text="Datos del Personal", padding=(10, 10))
            self.groupBox.pack(padx=10, pady=10)

            labelId = ttk.Label(self.groupBox, text="Id:", width=10)
            labelId.grid(row=0, column=0, padx=5, pady=5)
            self.textBoxId = ttk.Entry(self.groupBox, width=30)
            self.textBoxId.grid(row=0, column=1, padx=5, pady=5)

            labelNombres = ttk.Label(self.groupBox, text="Nombres:", width=10)
            labelNombres.grid(row=1, column=0, padx=5, pady=5)
            self.textBoxNombres = ttk.Entry(self.groupBox, width=30)
            self.textBoxNombres.grid(row=1, column=1, padx=5, pady=5)

            labelApellidos = ttk.Label(self.groupBox, text="Apellidos:", width=10)
            labelApellidos.grid(row=2, column=0, padx=5, pady=5)
            self.textBoxApellidos = ttk.Entry(self.groupBox, width=30)
            self.textBoxApellidos.grid(row=2, column=1, padx=5, pady=5)

            labelSexo = ttk.Label(self.groupBox, text="Sexo:", width=10)
            labelSexo.grid(row=3, column=0, padx=5, pady=5)
            self.combo = ttk.Combobox(self.groupBox, values=["Masculino", "Femenino"], width=27)
            self.combo.grid(row=3, column=1, padx=5, pady=5)
            self.combo.set("Masculino")

            guardar_btn = ttk.Button(self.groupBox, text="Guardar", width=10, command=self.guardarRegistros)
            guardar_btn.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

            self.groupBox_lista = ttk.LabelFrame(self.base, text="Lista del Personal", padding=(10, 10))
            self.groupBox_lista.pack(padx=10, pady=10, fill="both", expand=True)

            self.tree = ttk.Treeview(self.groupBox_lista, columns=("Id", "Nombres", "Apellidos", "Sexo"), show='headings', height=5)
            self.tree.column("# 1", anchor=tk.CENTER, width=50)
            self.tree.heading("# 1", text="Id")
            self.tree.column("# 2", anchor=tk.CENTER, width=150)
            self.tree.heading("# 2", text="Nombres")
            self.tree.column("# 3", anchor=tk.CENTER, width=150)
            self.tree.heading("# 3", text="Apellidos")
            self.tree.column("# 4", anchor=tk.CENTER, width=100)
            self.tree.heading("# 4", text="Sexo")
            self.tree.pack(padx=10, pady=10, fill="both", expand=True)

            self.base.mainloop()

        except ValueError as error:
            print("Error al mostrar la interfaz, error: {}".format(error))

    def guardarRegistros(self):
        try:
            nombres = self.textBoxNombres.get()
            apellidos = self.textBoxApellidos.get()
            sexo = self.combo.get()

            conn = mysql.connector.connect(
                host='localhost',
                user='tu_usuario',
                password='tu_contraseña',
                database='clientesdb'
            )

            cursor = conn.cursor()
            sql = "INSERT INTO clientes (nombres, apellidos, sexo) VALUES (%s, %s, %s)"
            val = (nombres, apellidos, sexo)
            cursor.execute(sql, val)

            conn.commit()
            messagebox.showinfo("Información", "Datos guardados correctamente en la base de datos")
            
            self.actualizarLista()  # Actualizar la lista después de guardar

            cursor.close()
            conn.close()

            self.textBoxId.delete(0, tk.END)
            self.textBoxNombres.delete(0, tk.END)
            self.textBoxApellidos.delete(0, tk.END)

        except mysql.connector.Error as error:
            messagebox.showerror("Error", "Error al guardar los datos en la base de datos: {}".format(error))

    def actualizarLista(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='tu_usuario',
                password='tu_contraseña',
                database='clientesdb'
            )

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes")
            rows = cursor.fetchall()

            # Limpiar árbol antes de actualizar
            for row in self.tree.get_children():
                self.tree.delete(row)

            for row in rows:
                self.tree.insert("", tk.END, values=row)

            cursor.close()
            conn.close()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", "Error al actualizar la lista: {}".format(error))


if __name__ == "__main__":
    formulario_clientes = FormularioClientes()
    formulario_clientes.formulario()
>>>>>>> 53f93dd75a7ceb6d18c2c431cb827f42caadc2c8

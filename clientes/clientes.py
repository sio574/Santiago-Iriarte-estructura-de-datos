import tkinter as tk
from tkinter import messagebox

# Clase nodo
class Nodo:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None

# Clase lista circular
class ListaCircular:
    def __init__(self):
        self.inicio = None

    def insertar_cliente(self, cedula, nombre):
        nuevo = Nodo(cedula, nombre)
        if self.inicio is None:
            self.inicio = nuevo
            nuevo.siguiente = nuevo
        else:
            temp = self.inicio
            while temp.siguiente != self.inicio:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
        messagebox.showinfo("Éxito", "Cliente insertado correctamente")

    def listar_clientes(self):
        if self.inicio is None:
            return "No hay clientes."
        resultado = ""
        temp = self.inicio
        while True:
            resultado += f"Cédula: {temp.cedula} - Nombre: {temp.nombre}\n"
            temp = temp.siguiente
            if temp == self.inicio:
                break
        return resultado

# Interfaz gráfica
class Aplicacion:
    def __init__(self, root):
        self.lista = ListaCircular()

        root.title("Lista Circular de Clientes")
        root.geometry("400x300")

        tk.Label(root, text="Cédula:").pack()
        self.cedula_entry = tk.Entry(root)
        self.cedula_entry.pack()

        tk.Label(root, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.pack()

        tk.Button(root, text="Insertar Cliente", command=self.insertar).pack(pady=5)
        tk.Button(root, text="Listar Clientes", command=self.listar).pack(pady=5)
        tk.Button(root, text="Salir", command=root.quit).pack(pady=5)

        self.resultado = tk.Text(root, height=10, width=50)
        self.resultado.pack()

    def insertar(self):
        cedula = self.cedula_entry.get()
        nombre = self.nombre_entry.get()
        if cedula and nombre:
            self.lista.insertar_cliente(cedula, nombre)
            self.cedula_entry.delete(0, tk.END)
            self.nombre_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Debes ingresar cédula y nombre")

    def listar(self):
        resultado = self.lista.listar_clientes()
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, resultado)

root = tk.Tk()
app = Aplicacion(root)
root.mainloop()

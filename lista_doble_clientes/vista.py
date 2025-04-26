import tkinter as tk
from tkinter import messagebox
from controlador import ClienteControlador

class App:
    def __init__(self, root):
        self.controlador = ClienteControlador()
        self.root = root
        self.root.title("Lista Doble de Clientes")
        self.root.geometry("400x400")

        tk.Label(root, text="Cédula:").pack()
        self.entry_cedula = tk.Entry(root)
        self.entry_cedula.pack()

        tk.Label(root, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()

        tk.Button(root, text="Insertar Cliente", command=self.insertar_cliente).pack(pady=5)
        tk.Button(root, text="Listar →", command=self.listar_derecha).pack()
        tk.Button(root, text="Listar ←", command=self.listar_izquierda).pack()

        self.text_area = tk.Text(root, height=10)
        self.text_area.pack(pady=10)

    def insertar_cliente(self):
        try:
            cedula = int(self.entry_cedula.get())
            nombre = self.entry_nombre.get().strip()
            if nombre:
                self.controlador.insertar_cliente(cedula, nombre)
                messagebox.showinfo("Éxito", "Cliente insertado correctamente")
                self.entry_cedula.delete(0, tk.END)
                self.entry_nombre.delete(0, tk.END)
            else:
                messagebox.showwarning("Advertencia", "El nombre no puede estar vacío")
        except ValueError:
            messagebox.showerror("Error", "La cédula debe ser un número")

    def listar_derecha(self):
        self.text_area.delete("1.0", tk.END)
        for cliente in self.controlador.obtener_derecha():
            self.text_area.insert(tk.END, cliente + "\n")

    def listar_izquierda(self):
        self.text_area.delete("1.0", tk.END)
        for cliente in self.controlador.obtener_izquierda():
            self.text_area.insert(tk.END, cliente + "\n")

import tkinter as tk
from tkinter import messagebox

# Nodo para lista simple
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Bicola implementada con lista simple
class Bicola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar_derecha(self, valor):
        nuevo = Nodo(valor)
        if not self.primero:
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo

    def insertar_izquierda(self, valor):
        nuevo = Nodo(valor)
        if not self.primero:
            self.primero = self.ultimo = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero = nuevo

    def atender_derecha(self):
        if not self.primero:
            return None
        if self.primero == self.ultimo:
            valor = self.ultimo.valor
            self.primero = self.ultimo = None
            return valor
        actual = self.primero
        while actual.siguiente != self.ultimo:
            actual = actual.siguiente
        valor = self.ultimo.valor
        actual.siguiente = None
        self.ultimo = actual
        return valor

    def atender_izquierda(self):
        if not self.primero:
            return None
        valor = self.primero.valor
        self.primero = self.primero.siguiente
        if not self.primero:
            self.ultimo = None
        return valor

    def listar(self):
        elementos = []
        actual = self.primero
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
        return " <- ".join(elementos) if elementos else "Bicola vacía"

# Interfaz gráfica
class App:
    def __init__(self, root):
        self.bicola = Bicola()

        root.title("Bicola - Lista Simple")
        root.geometry("400x300")

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        tk.Button(root, text="Insertar por la derecha", command=self.insertar_derecha).pack()
        tk.Button(root, text="Insertar por la izquierda", command=self.insertar_izquierda).pack()
        tk.Button(root, text="Atender por la derecha", command=self.atender_derecha).pack()
        tk.Button(root, text="Atender por la izquierda", command=self.atender_izquierda).pack()
        tk.Button(root, text="Listar", command=self.listar).pack()
        tk.Button(root, text="Salir", command=root.quit).pack(pady=10)

        self.resultado = tk.Label(root, text="Bicola vacía", fg="blue")
        self.resultado.pack(pady=10)

    def insertar_derecha(self):
        valor = self.entry.get()
        if valor:
            self.bicola.insertar_derecha(valor)
            self.entry.delete(0, tk.END)
            self.listar()

    def insertar_izquierda(self):
        valor = self.entry.get()
        if valor:
            self.bicola.insertar_izquierda(valor)
            self.entry.delete(0, tk.END)
            self.listar()

    def atender_derecha(self):
        valor = self.bicola.atender_derecha()
        if valor is not None:
            messagebox.showinfo("Atendido por la derecha", f"Elemento: {valor}")
        else:
            messagebox.showwarning("Atención", "La bicola está vacía")
        self.listar()

    def atender_izquierda(self):
        valor = self.bicola.atender_izquierda()
        if valor is not None:
            messagebox.showinfo("Atendido por la izquierda", f"Elemento: {valor}")
        else:
            messagebox.showwarning("Atención", "La bicola está vacía")
        self.listar()

    def listar(self):
        self.resultado.config(text=self.bicola.listar())

# Ejecutar app
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

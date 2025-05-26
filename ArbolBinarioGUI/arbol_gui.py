import tkinter as tk
from tkinter import messagebox

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, raiz, dato):
        if raiz is None:
            return Nodo(dato)
        elif dato < raiz.dato:
            raiz.izq = self.insertar(raiz.izq, dato)
        else:
            raiz.der = self.insertar(raiz.der, dato)
        return raiz

    def in_orden(self, raiz):
        if raiz:
            return self.in_orden(raiz.izq) + [raiz.dato] + self.in_orden(raiz.der)
        return []

    def pre_orden(self, raiz):
        if raiz:
            return [raiz.dato] + self.pre_orden(raiz.izq) + self.pre_orden(raiz.der)
        return []

    def post_orden(self, raiz):
        if raiz:
            return self.post_orden(raiz.izq) + self.post_orden(raiz.der) + [raiz.dato]
        return []

class Interfaz:
    def __init__(self, master):
        self.arbol = ArbolBinario()
        self.master = master
        master.title("Árbol Binario Ordenado")

        self.label = tk.Label(master, text="Dato a insertar:")
        self.label.pack()

        self.entrada = tk.Entry(master)
        self.entrada.pack()

        self.boton_insertar = tk.Button(master, text="Insertar", command=self.insertar_dato)
        self.boton_insertar.pack()

        self.boton_inorden = tk.Button(master, text="In Orden", command=self.mostrar_inorden)
        self.boton_inorden.pack()

        self.boton_postorden = tk.Button(master, text="Post Orden", command=self.mostrar_postorden)
        self.boton_postorden.pack()

        self.boton_preorden = tk.Button(master, text="Pre Orden", command=self.mostrar_preorden)
        self.boton_preorden.pack()

        self.salida = tk.Text(master, height=10, width=40)
        self.salida.pack()

    def insertar_dato(self):
        try:
            dato = int(self.entrada.get())
            self.arbol.raiz = self.arbol.insertar(self.arbol.raiz, dato)
            messagebox.showinfo("Éxito", f"Dato {dato} insertado.")
            self.entrada.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número entero.")

    def mostrar_inorden(self):
        recorrido = self.arbol.in_orden(self.arbol.raiz)
        self.salida.delete("1.0", tk.END)
        self.salida.insert(tk.END, "In Orden:\n" + " ".join(map(str, recorrido)))

    def mostrar_postorden(self):
        recorrido = self.arbol.post_orden(self.arbol.raiz)
        self.salida.delete("1.0", tk.END)
        self.salida.insert(tk.END, "Post Orden:\n" + " ".join(map(str, recorrido)))

    def mostrar_preorden(self):
        recorrido = self.arbol.pre_orden(self.arbol.raiz)
        self.salida.delete("1.0", tk.END)
        self.salida.insert(tk.END, "Pre Orden:\n" + " ".join(map(str, recorrido)))

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()

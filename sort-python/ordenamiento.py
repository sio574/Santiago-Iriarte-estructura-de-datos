import tkinter as tk
from tkinter import messagebox

def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insercion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x < pivote]
        mayores = [x for x in arr[1:] if x >= pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)

class OrdenamientoGUI:
    def __init__(self, root):
        root.title("Métodos de Ordenamiento")
        root.geometry("400x300")

        tk.Label(root, text="Ingresa los números separados por coma:").pack()
        self.entrada = tk.Entry(root, width=40)
        self.entrada.pack()

        tk.Button(root, text="Burbuja", command=self.metodo_burbuja).pack(pady=5)
        tk.Button(root, text="Inserción", command=self.metodo_insercion).pack(pady=5)
        tk.Button(root, text="Quicksort", command=self.metodo_quicksort).pack(pady=5)
        tk.Button(root, text="Salir", command=root.quit).pack(pady=5)

        self.resultado = tk.Text(root, height=6, width=50)
        self.resultado.pack()

    def obtener_lista(self):
        try:
            return list(map(int, self.entrada.get().split(',')))
        except:
            messagebox.showerror("Error", "Ingresa solo números separados por coma.")
            return None

    def mostrar_resultado(self, metodo, lista):
        if lista is not None:
            ordenada = metodo(lista.copy())
            self.resultado.delete("1.0", tk.END)
            self.resultado.insert(tk.END, f"Resultado: {ordenada}")

    def metodo_burbuja(self):
        self.mostrar_resultado(burbuja, self.obtener_lista())

    def metodo_insercion(self):
        self.mostrar_resultado(insercion, self.obtener_lista())

    def metodo_quicksort(self):
        self.mostrar_resultado(quicksort, self.obtener_lista())

root = tk.Tk()
app = OrdenamientoGUI(root)
root.mainloop()

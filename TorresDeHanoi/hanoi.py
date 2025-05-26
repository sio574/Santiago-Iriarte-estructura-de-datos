import tkinter as tk
import time
from tkinter import messagebox

class HanoiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Torres de Hanoi - Interfaz Gráfica")
        self.root.geometry("640x400")
        self.root.resizable(False, False)

        self.frame = tk.Frame(self.root, bg="white")
        self.frame.pack(pady=10)

        self.label = tk.Label(self.frame, text="¿Cuántos discos quieres usar? (1 a 6)", font=("Arial", 12), bg="white")
        self.label.pack(pady=5)

        self.entry = tk.Entry(self.frame, font=("Arial", 12), justify="center")
        self.entry.pack(pady=5)

        self.btn = tk.Button(self.frame, text="Iniciar", font=("Arial", 12), bg="#007ACC", fg="white", command=self.iniciar_animacion)
        self.btn.pack(pady=10)

        self.canvas = tk.Canvas(self.root, width=600, height=250, bg='white')
        self.canvas.pack()

    def iniciar_animacion(self):
        entrada = self.entry.get()
        if not entrada.isdigit():
            messagebox.showerror("Error", "Por favor, ingresa un número entre 1 y 6.")
            return
        discos = int(entrada)
        if discos < 1 or discos > 6:
            messagebox.showerror("Error", "El número debe estar entre 1 y 6.")
            return

        # Limpiar canvas y variables
        self.canvas.delete("all")
        self.torres = [[], [], []]
        self.discos = []
        self.num_discos = discos

        # Crear torres visuales
        for i in range(3):
            x = 100 + i * 200
            self.canvas.create_rectangle(x - 5, 100, x + 5, 250, fill="gray")

        # Crear discos (el más grande primero, que va al fondo)
        for i in range(1, discos + 1):  # del más grande al más pequeño
            width = 20 + (discos - i + 1) * 20
            disco = self.canvas.create_rectangle(0, 0, width, 20, fill="skyblue", outline="black")
            self.torres[0].insert(0, disco)  # los grandes primero (fondo de la torre)
            self.discos.append(disco)

        self.dibujar_torres()
        self.root.after(1000, lambda: self.torres_de_hanoi(discos, 0, 2, 1))

    def dibujar_torres(self):
        for i in range(3):
            for j, disco in enumerate(self.torres[i]):  # ya están en orden correcto
                ancho = self.canvas.coords(disco)[2] - self.canvas.coords(disco)[0]
                x_centro = 100 + i * 200
                y = 250 - (len(self.torres[i]) - j - 1) * 22
                self.canvas.coords(disco, x_centro - ancho // 2, y - 20, x_centro + ancho // 2, y)

    def mover_disco(self, desde, hacia):
        disco = self.torres[desde].pop()
        self.torres[hacia].append(disco)
        self.dibujar_torres()
        self.root.update()
        time.sleep(0.5)

    def torres_de_hanoi(self, n, desde, hacia, auxiliar):
        if n == 1:
            self.mover_disco(desde, hacia)
        else:
            self.torres_de_hanoi(n - 1, desde, auxiliar, hacia)
            self.mover_disco(desde, hacia)
            self.torres_de_hanoi(n - 1, auxiliar, hacia, desde)

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = HanoiGUI(root)
    root.mainloop()

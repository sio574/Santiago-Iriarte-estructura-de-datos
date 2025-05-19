import tkinter as tk
import time

class HanoiGUI:
    def __init__(self, master, num_discos):
        self.master = master
        self.num_discos = num_discos
        self.canvas = tk.Canvas(master, width=600, height=300, bg='white')
        self.canvas.pack()
        self.torres = [[], [], []]  # Tres torres A, B y C
        self.discos = []

        # Crear los discos y ubicarlos en la torre 0 (izquierda)
        for i in range(num_discos, 0, -1):
            width = 20 + i * 20
            disco = self.canvas.create_rectangle(0, 0, width, 20, fill="skyblue", outline="black")
            self.torres[0].append(disco)
            self.discos.append(disco)

        self.dibujar_torres()
        self.master.after(1000, lambda: self.torres_de_hanoi(num_discos, 0, 2, 1))

    def dibujar_torres(self):
        self.canvas.delete("peg")
        for i in range(3):
            x = 100 + i * 200
            self.canvas.create_rectangle(x - 5, 100, x + 5, 250, fill="gray", tags="peg")

        for i in range(3):
            for j, disco in enumerate(reversed(self.torres[i])):
                ancho = self.canvas.coords(disco)[2] - self.canvas.coords(disco)[0]
                x_centro = 100 + i * 200
                y = 250 - j * 22
                self.canvas.coords(disco, x_centro - ancho // 2, y - 20, x_centro + ancho // 2, y)

    def mover_disco(self, desde, hacia):
        disco = self.torres[desde].pop()
        self.torres[hacia].append(disco)
        self.dibujar_torres()
        self.master.update()
        time.sleep(0.5)

    def torres_de_hanoi(self, n, desde, hacia, auxiliar):
        if n == 1:
            self.mover_disco(desde, hacia)
        else:
            self.torres_de_hanoi(n - 1, desde, auxiliar, hacia)
            self.mover_disco(desde, hacia)
            self.torres_de_hanoi(n - 1, auxiliar, hacia, desde)

def main():
    root = tk.Tk()
    root.title("Torres de Hanoi Gráfico")

    while True:
        try:
            discos = int(input("¿Cuántos discos quieres usar (entre 1 y 6)? "))
            if 1 <= discos <= 6:
                break
            else:
                print("Por favor elige entre 1 y 6 discos.")
        except ValueError:
            print("Ingresa un número válido.")

    app = HanoiGUI(root, discos)
    root.mainloop()

if __name__ == "__main__":
    main()

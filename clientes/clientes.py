# Clase Nodo: Representa a cada cliente en la lista
class Nodo:
    def __init__(self, cedula, nombre):
        self.cedula = cedula         # Cedula del cliente
        self.nombre = nombre         # Nombre del cliente
        self.siguiente = None        # Apunta al siguiente nodo


# Clase ListaCircular: Maneja la lista circular
class ListaCircular:
    def __init__(self):
        self.inicio = None  # Variable que se ubica en el último nodo

    # Método para insertar un nuevo cliente
    def insertar_cliente(self, cedula, nombre):
        nuevo = Nodo(cedula, nombre)  # Solo se puede crear la variable "nuevo"
        
        if self.inicio is None:
            # Primer nodo: apunta a sí mismo y se vuelve el inicio
            nuevo.siguiente = nuevo
            self.inicio = nuevo
        else:
            # Recorremos hasta llegar al último nodo
            temp = self.inicio
            while temp.siguiente != self.inicio:
                temp = temp.siguiente
            # Insertamos al final y actualizamos punteros
            temp.siguiente = nuevo
            nuevo.siguiente = self.inicio
            self.inicio = nuevo  # La variable inicio se ubica en el nuevo último nodo

    # Método para listar los clientes hacia la derecha
    def listar_clientes(self):
        if self.inicio is None:
            print("No hay clientes en la lista.")
            return

        print("Lista de clientes:")
        temp = self.inicio.siguiente  # Empezamos desde el primer nodo
        while True:
            print(f"Cédula: {temp.cedula}, Nombre: {temp.nombre}")
            if temp == self.inicio:
                break
            temp = temp.siguiente


# --------------------- MENÚ PRINCIPAL ---------------------
def menu():
    lista = ListaCircular()

    while True:
        print("\n--- Menú de Clientes ---")
        print("1. Insertar Cliente")
        print("2. Listar Clientes hacia la derecha")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cedula = input("Ingrese la cédula del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")
            lista.insertar_cliente(cedula, nombre)
        elif opcion == "2":
            lista.listar_clientes()
        elif opcion == "3":
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutamos el menú
menu()

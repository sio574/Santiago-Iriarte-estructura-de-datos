class Nodo:
    def __init__(self, cedula, nombre):
        self.cedula = cedula         
        self.nombre = nombre         
        self.siguiente = None        
class ListaCircular:
    def __init__(self):
        self.inicio = None  
    def insertar_cliente(self, cedula, nombre):
        nuevo = Nodo(cedula, nombre)  
        
        if self.inicio is None:
            nuevo.siguiente = nuevo
            self.inicio = nuevo
        else:
            temp = self.inicio
            while temp.siguiente != self.inicio:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.siguiente = self.inicio
            self.inicio = nuevo  
    def listar_clientes(self):
        if self.inicio is None:
            print("No hay clientes en la lista.")
            return

        print("Lista de clientes:")
        temp = self.inicio.siguiente  
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
menu()

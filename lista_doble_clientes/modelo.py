class NodoDoble:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.anterior = None
        self.siguiente = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None

    def insertar_ordenado(self, cedula, nombre):
        nuevo = NodoDoble(cedula, nombre)
        if not self.cabeza or cedula < self.cabeza.cedula:
            nuevo.siguiente = self.cabeza
            if self.cabeza:
                self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.cedula < cedula:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior = nuevo
            actual.siguiente = nuevo
            nuevo.anterior = actual

    def listar_derecha(self):
        lista = []
        actual = self.cabeza
        while actual:
            lista.append(f"Cédula: {actual.cedula} - Nombre: {actual.nombre}")
            actual = actual.siguiente
        return lista

    def listar_izquierda(self):
        lista = []
        actual = self.cabeza
        if not actual:
            return lista
        while actual.siguiente:
            actual = actual.siguiente
        while actual:
            lista.append(f"Cédula: {actual.cedula} - Nombre: {actual.nombre}")
            actual = actual.anterior
        return lista

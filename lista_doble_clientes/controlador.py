from modelo import ListaDoble

class ClienteControlador:
    def __init__(self):
        self.lista = ListaDoble()

    def insertar_cliente(self, cedula, nombre):
        self.lista.insertar_ordenado(cedula, nombre)

    def obtener_derecha(self):
        return self.lista.listar_derecha()

    def obtener_izquierda(self):
        return self.lista.listar_izquierda()

public class ListaDoble {
    NodoDoble cabeza;

    // Insertar ordenado por cédula
    public void insertarOrdenado(int cedula, String nombre) {
        NodoDoble nuevo = new NodoDoble(cedula, nombre);
        if (cabeza == null || cedula < cabeza.cedula) {
            nuevo.siguiente = cabeza;
            if (cabeza != null) cabeza.anterior = nuevo;
            cabeza = nuevo;
        } else {
            NodoDoble actual = cabeza;
            while (actual.siguiente != null && actual.siguiente.cedula < cedula) {
                actual = actual.siguiente;
            }
            nuevo.siguiente = actual.siguiente;
            if (actual.siguiente != null) actual.siguiente.anterior = nuevo;
            actual.siguiente = nuevo;
            nuevo.anterior = actual;
        }
    }

    // Listar hacia la derecha (inicio -> fin)
    public void listarDerecha() {
        NodoDoble actual = cabeza;
        while (actual != null) {
            System.out.println("Cédula: " + actual.cedula + " - Nombre: " + actual.nombre);
            actual = actual.siguiente;
        }
    }

    // Listar hacia la izquierda (fin -> inicio)
    public void listarIzquierda() {
        if (cabeza == null) return;
        NodoDoble actual = cabeza;
        // Ir al último nodo
        while (actual.siguiente != null) {
            actual = actual.siguiente;
        }
        // Volver hacia atrás
        while (actual != null) {
            System.out.println("Cédula: " + actual.cedula + " - Nombre: " + actual.nombre);
            actual = actual.anterior;
        }
    }
}
public class ListaSimple {
    private Nodo cabeza;

    public ListaSimple() {
        cabeza = null;
    }

    public void insertarOrdenado(Cliente cliente) {
        Nodo nuevo = new Nodo(cliente);
        if (cabeza == null || cliente.getCedula().compareTo(cabeza.cliente.getCedula()) < 0) {
            nuevo.siguiente = cabeza;
            cabeza = nuevo;
        } else {
            Nodo actual = cabeza;
            while (actual.siguiente != null &&
                   cliente.getCedula().compareTo(actual.siguiente.cliente.getCedula()) > 0) {
                actual = actual.siguiente;
            }
            nuevo.siguiente = actual.siguiente;
            actual.siguiente = nuevo;
        }
    }

    public void listar() {
        Nodo actual = cabeza;
        while (actual != null) {
            System.out.println(actual.cliente);
            actual = actual.siguiente;
        }
    }
}

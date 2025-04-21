public class NodoDoble {
    int cedula;
    String nombre;
    NodoDoble anterior;
    NodoDoble siguiente;

    public NodoDoble(int cedula, String nombre) {
        this.cedula = cedula;
        this.nombre = nombre;
        this.anterior = null;
        this.siguiente = null;
    }
}
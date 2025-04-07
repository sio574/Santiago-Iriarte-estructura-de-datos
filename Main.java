
    import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ListaSimple lista = new ListaSimple();
        Scanner scanner = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\n--- Menú ---");
            System.out.println("1. Insertar Cliente");
            System.out.println("2. Listar Clientes hacia la derecha");
            System.out.println("3. Salir");
            System.out.print("Seleccione una opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine(); // Limpiar buffer

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese cédula: ");
                    String cedula = scanner.nextLine();
                    System.out.print("Ingrese nombre: ");
                    String nombre = scanner.nextLine();
                    Cliente cliente = new Cliente(cedula, nombre);
                    lista.insertarOrdenado(cliente);
                    break;
                case 2:
                    System.out.println("\n--- Lista de Clientes ---");
                    lista.listar();
                    break;
                case 3:
                    System.out.println("Saliendo...");
                    break;
                default:
                    System.out.println("Opción inválida.");
            }
        } while (opcion != 3);

        scanner.close();
    }
}



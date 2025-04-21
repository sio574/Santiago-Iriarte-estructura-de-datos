import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ListaDoble lista = new ListaDoble();
        int opcion;

        do {
            System.out.println("\n--- MENÚ DE CLIENTES ---");
            System.out.println("1. Insertar cliente");
            System.out.println("2. Listar clientes hacia la derecha");
            System.out.println("3. Listar clientes hacia la izquierda");
            System.out.println("4. Salir");
            System.out.print("Elige una opción: ");
            opcion = sc.nextInt();
            sc.nextLine(); // Limpiar el buffer

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese cédula del cliente: ");
                    int cedula = sc.nextInt();
                    sc.nextLine(); // Limpiar el buffer
                    System.out.print("Ingrese nombre del cliente: ");
                    String nombre = sc.nextLine();
                    lista.insertarOrdenado(cedula, nombre);
                    System.out.println("Cliente insertado correctamente.");
                    break;
                case 2:
                    System.out.println("\n--- Listado hacia la derecha ---");
                    lista.listarDerecha();
                    break;
                case 3:
                    System.out.println("\n--- Listado hacia la izquierda ---");
                    lista.listarIzquierda();
                    break;
                case 4:
                    System.out.println("Saliendo de la aplicación. ¡Chao mi amor! 💕");
                    break;
                default:
                    System.out.println("Opción inválida, intenta otra vez.");
            }

        } while (opcion != 4);

        sc.close();
    }
}
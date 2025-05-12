# Programa para demostrar métodos de ordenamiento

def burbuja(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def insercion(lista):
    for i in range(1, len(lista)):
        valor = lista[i]
        j = i - 1
        while j >= 0 and valor < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor
    return lista

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x < pivote]
        mayores = [x for x in lista[1:] if x >= pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)

def mostrar_menu():
    print("\n--- MENÚ DE ORDENAMIENTO ---")
    print("1. Método Burbuja")
    print("2. Método de Inserción")
    print("3. Método Quicksort")
    print("4. Salir")

# Ciclo principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion in ['1', '2', '3']:
        numeros = input("Ingresa los números separados por coma: ")
        lista = [int(x) for x in numeros.split(",")]

        if opcion == '1':
            resultado = burbuja(lista.copy())
            print("Lista ordenada (Burbuja):", resultado)
        elif opcion == '2':
            resultado = insercion(lista.copy())
            print("Lista ordenada (Inserción):", resultado)
        elif opcion == '3':
            resultado = quicksort(lista.copy())
            print("Lista ordenada (Quicksort):", resultado)

    elif opcion == '4':
        print("Saliendo del programa")
        break
    else:
        print("Opción inválida, intenta de nuevo.")

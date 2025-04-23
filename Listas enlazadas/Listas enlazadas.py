# Clase Nodo representa cada elemento de la lista
class Nodo:
    def __init__(self, dato):
        self.dato = dato              # Dato que guarda el nodo
        self.siguiente = None         # Referencia al siguiente nodo

# Clase ListaEnlazada contiene métodos para manipular la lista
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None           # Referencia al primer nodo de la lista

    # Método para verificar si la lista está vacía
    def esta_vacia(self):
        return self.cabeza is None

    # Inserta un nodo al inicio de la lista
    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza  # El nuevo nodo apunta al que era la cabeza
        self.cabeza = nuevo_nodo            # Se actualiza la cabeza al nuevo nodo

    # Cuenta la cantidad de nodos en la lista
    def cantidad_nodos(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    # Suma todos los valores enteros almacenados en los nodos
    def suma_valores(self):
        suma = 0
        actual = self.cabeza
        while actual:
            if isinstance(actual.dato, int):  # Verifica que el dato sea entero
                suma += actual.dato
            actual = actual.siguiente
        return suma

    # Devuelve el valor del primer nodo (la cabeza)
    def primer_valor(self):
        if self.cabeza:
            return self.cabeza.dato
        return None  # Si la lista está vacía

    # Recorre y muestra todos los elementos de la lista
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# ------------------ Código principal ------------------
if __name__ == "__main__":
    lista = ListaEnlazada()
    print("Ingrese números para la lista enlazada (escriba 'fin' para terminar):")

    # Lee datos desde el usuario hasta que escriba 'fin'
    while True:
        entrada = input("Dato: ")
        if entrada.lower() == "fin":
            break
        if entrada.isdigit():  # Solo se permite ingresar enteros positivos
            lista.insertar_al_inicio(int(entrada))  # Inserta al inicio
        else:
            print("Ingrese solo números enteros o 'fin'.")

    # Muestra el contenido y resultados de los métodos implementados
    print("\nContenido de la lista enlazada:")
    lista.mostrar()

    print("¿La lista está vacía?", "Sí" if lista.esta_vacia() else "No")
    print("Cantidad de nodos:", lista.cantidad_nodos())
    print("Suma de los valores:", lista.suma_valores())
    print("Primer valor de la lista:", lista.primer_valor())

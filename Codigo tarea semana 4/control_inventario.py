from producto import Producto
from utils import mostrar_menu, validar_entero, validar_flotante, buscar_producto

productos = []

def registrar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría: ")
    precio = validar_flotante("Precio: $")
    stock = validar_entero("Cantidad en stock: ")
    nuevo = Producto(nombre, categoria, precio, stock)
    productos.append(nuevo)
    print("Producto registrado exitosamente.")

def agregar_stock():
    nombre = input("Ingrese el nombre del producto: ")
    producto = buscar_producto(nombre, productos)
    if producto:
        cantidad = validar_entero("Cantidad a agregar: ")
        producto.agregar_stock(cantidad)
    else:
        print("Producto no encontrado.")

def retirar_stock():
    nombre = input("Ingrese el nombre del producto: ")
    producto = buscar_producto(nombre, productos)
    if producto:
        cantidad = validar_entero("Cantidad a retirar: ")
        producto.retirar_stock(cantidad)
    else:
        print("Producto no encontrado.")

def mostrar_info_producto():
    nombre = input("Ingrese el nombre del producto: ")
    producto = buscar_producto(nombre, productos)
    if producto:
        producto.mostrar_info()
    else:
        print("Producto no encontrado.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            agregar_stock()
        elif opcion == '3':
            retirar_stock()
        elif opcion == '4':
            mostrar_info_producto()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
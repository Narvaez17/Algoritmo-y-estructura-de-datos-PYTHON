#Codigo
def calcular_aporte(vehiculo, km=0, toneladas=0):
    if vehiculo == "bicicleta":
        return 100
    elif vehiculo in ["moto", "carro"]:
        return km * 30
    elif vehiculo == "camion":
        return km * 30 + toneladas * 25
    else:
        return "Tipo de vehículo no válido"

# Ejemplo de uso
vehiculo = input("Ingrese el tipo de vehículo (bicicleta, moto, carro, camion): ").lower()

if vehiculo == "bicicleta":
    importe = calcular_aporte(vehiculo)
elif vehiculo in ["moto", "carro"]:
    km = float(input("Ingrese los kilómetros recorridos: "))
    importe = calcular_aporte(vehiculo, km)
elif vehiculo == "camion":
    km = float(input("Ingrese los kilómetros recorridos: "))
    toneladas = float(input("Ingrese las toneladas transportadas: "))
    importe = calcular_aporte(vehiculo, km, toneladas)
else:
    importe = "Vehículo no válido"

print(f"El importe a pagar es: {importe} córdobas")


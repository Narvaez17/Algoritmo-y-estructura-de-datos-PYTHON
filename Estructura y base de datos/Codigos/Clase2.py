
#Ejemplo de condicionales
#print("Digita tu edad:")
#edad = int(input())

#if edad>=16:
    #print("Es mayor de edad")
#else:
    #print("No es mayor de edad")

#print("Fin del programa")#

usuario = input("USUARIO:")
usuario = usuario.upper()

if usuario == "DOSSON":
    print("Bienvenido, DOSSON")
    password = input("CONTRASEÑA: " .upper())
    if password.upper() == "25042007":
        print("Usted es un usuario valido")

    else:
        print("Contrase;a invalida")

else:
    print("USUARIO NO VALIDO")


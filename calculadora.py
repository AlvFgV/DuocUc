print("---CALCULADORA---")

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))

while True:
    print("\nMenu de opciones")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Dividir")
    print("4 - Multiplicar")
    print("5 - Salir")

    opc = int(input("Ingresa una opcion: "))

    if opc == 1:
        print("Resultado:", num1 + num2)

    elif opc == 2:
        print("Resultado:", num1 - num2)

    elif opc == 3:
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("No se puede dividir entre 0")

    elif opc == 4:
        print("Resultado:", num1 * num2)

    elif opc == 5:
        print("Saliendo de la calculadora...")
        break

    else:
        print("Opcion no valida")

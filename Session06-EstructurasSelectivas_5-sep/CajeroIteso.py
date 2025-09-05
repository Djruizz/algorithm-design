pinCorrecto = 1234
Saldo = 1000

print("Bienvenido a el Banco ITESO")
inputPin = int(input("Ingresa tu pin: "))
if(inputPin != pinCorrecto):
    print("El pin ingresado es incorrecto")
else:
    print("\nPin correcto. Acceso concedido\n")
    print("Acciones disponibles:")
    print("1. Consultar Saldo \n2. Retirar dinero \n3. Depositar dinero" )
    Accion = int(input("Ingresa el numero de la acción que quieres realizar: "))
    if Accion == 1: #Consultar Saldo
        print("Saldo actual: ", Saldo)
    elif Accion == 2: #Retirar Saldo

        montoSolicitado = float(input("Ingresa el monto que deseas retirar: "))

        if(montoSolicitado > Saldo):
            print("Fondos insuficientes")
        elif (montoSolicitado >= 0):
            Saldo -= montoSolicitado
            print("Nuevo saldo: ", Saldo)
        else:
            print("Monto inválido")

    elif Accion == 3: #Depositar Dinero
        montoDepositado = float(input("Ingresa el monto que deseas depositar: "))
        if montoDepositado >0:
            Saldo += montoDepositado
            print("Nuevo Saldo: ", Saldo)
        else:
            print("Monto inválido")
    else:
        print("Opción no válida")


#**Ejercicio Dieciséis**
##Desarrolla un programa en Python que permita gestionar una lista de tareas pendientes. El programa debe cumplir con los siguientes requisitos:
#
##- Debe permitir agregar nuevas tareas a la lista.
##- Debe permitir marcar tareas como completadas, lo que las eliminará de la lista de tareas pendientes.
##- Debe mostrar la lista actual de tareas pendientes.
##- Debe proporcionar un menú interactivo que permita al usuario seleccionar entre las opciones anteriores y salir del programa.
##El menú debe presentar las siguientes opciones:
#
##- Agregar tarea
##- Marcar tarea como completada
##- Mostrar tareas
##- Salir
tareas = []
while True:
    print("Bienvenido al menu de tareas:")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas")
    print("4. Salir")
    opcion:int = int(input("Seleccione una opción del menu de tares: "))
    if opcion == 1:
        tareas.append(input("Ingrese la nueva tarea: "))
    elif opcion == 2:
        tarea_completada = tareas.pop(int(input("Ingrese el indice de la tarea completada: ")) - 1)
        print(f"la tarea {tarea_completada} ha sido marcada como completada y eliminada de la lista")
    elif opcion == 3:
        print("Lista de tareas pendientes:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    elif opcion == 4:
        break
#**Ejercicio Diecisiete**
##Crea un programa en Python que simule el funcionamiento de un cajero automático. El programa debe permitir al usuario realizar las siguientes operaciones:
#
##- Verificar el saldo de su cuenta.
##- Depositar dinero en su cuenta.
##- Retirar dinero de su cuenta.
##- Salir del programa.
##El programa debe iniciar con un saldo inicial predeterminado y mostrar un menú con las siguientes opciones:
#
##- Verificar saldo
##- Depositar dinero
##- Retirar dinero
##- Salir

saldo_restante = 100
while True:
    print("Menú de cajero automatico:")
    print("1. Verificar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion:int = int(input("Seleccione una opción del menu de cajero automatico: "))
    if opcion == 1:
        print(f"Su saldo actual es: ${saldo_restante}")
    elif opcion == 2:
        cantidad:float = float(input("Ingrese la cantidad a depositar: "))
        saldo_restante += cantidad
        print(f"Se ha depositado ${cantidad}")
    elif opcion == 3:
        cantidad:float = float(input("Ingrese la cantidad a retirar: "))
        if cantidad > saldo_restante:
            print("su saldo restante es menor a la cantidad que quiere retirar")
        else:
            saldo_restante -= cantidad
            print(f"Se ha retirado ${cantidad}")
    elif opcion == 4:
        break
#**Ejercicio Dieciocho**
##Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.
password:bool=True
while password:
    contraseña_ingresada:str = input("Ingrese la contraseña: ")
    confirmar_contraseña:str = input("confirme la contraseña nuevamente: ")
    if contraseña_ingresada == confirmar_contraseña:
        print("Contraseña confirmada.")
        break
    else:
        print("Las contraseñas no coinciden. Inténtelo de nuevo.")
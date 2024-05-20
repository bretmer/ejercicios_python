#**Ejercicio Cuatro**
##Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
for n in range(10):
    for i in range(1,11):
        print(f"{n+1}*{i}={(n+1)*i}")
#**Ejercicio Cinco**
##Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
palabra_invertida=""
palabra_usuario:str=input("ingrese una palabra:")
for n in palabra_usuario:
   palabra_invertida = n + palabra_invertida
print(palabra_invertida)
#**Ejercicio Seis**
##Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo.
numero_entero:int=int(input("ingrese un numero: "))
for i in range(1,numero_entero+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")
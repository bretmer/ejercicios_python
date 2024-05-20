#**Ejercicio Uno**
##Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 puede entrar gratis, si tiene entre 4 y 18 debe pagar 5 soles, y si es mayor de 18 deberá pagar 10 soles.
edad_cliente:int=int(input("ingrese su edad: "))
if edad_cliente < 4:
     print("su ingreso es gratis")
elif edad_cliente >=4 and edad_cliente <=18:
     print("por su ingreso debe pagar s/.5 ")
elif edad_cliente >18:
    print("por su ingreso debe pagar s/.10")
#**Ejercicio Dos**
##Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces
palabra:str=input("escribe una palabra: ")
print(palabra*10)
#**Ejercicio Tres**
##Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
numero_entero:int=int(input("ingrese un numero entero positivo: "))
for n in range(1,numero_entero):
    if n%2!=0:
        print(n , end=",")
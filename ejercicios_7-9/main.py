#**Ejercicio Siete**
##Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase:str=input("escriba una frase: ")
letra:str=input("escriba una letra: ")
contador_letra:int=0
for n in range(0,len(frase)):
    if frase[n]==letra:
        contador_letra+=1
print(f"la letra {letra} aparece {contador_letra} veces en la frase")
#**Ejercicio Ocho**
##Escribir un programa que pida al usuario una palabra y luego muestre por pantalla la primera letra la letra que se encuentra en medio y la ultima letra separadas por comas(,).
primera_letra:str=""
letra_medio:str=""
ultima_letra:str=""
for n in range(1):
    palabra:str=input("ingrese una palabra: ")
    primera_letra+=palabra[0]
    letra_medio+=palabra[len(palabra) // 2]
    ultima_letra+=palabra[-1]
letras=primera_letra+letra_medio+ultima_letra
print(letras)  

#**Ejercicio Nueve**
##Escriba un programa que pregunte cuántos números se van a introducir, luego pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el anterior.
valores = int(input("¿Cuántos valores vas a introducir? "))
if valores > 0:
    numero_anterior = int(input("Introduce un número: "))
    for i in range(1, valores):
        numero_actual = int(input("Introduce el siguiente número: "))
        if numero_actual <= numero_anterior:
            print("El número introducido no es mayor que el anterior.") 
        numero_actual = numero_anterior       
else:
    print("¡IMPOSIBLE!")
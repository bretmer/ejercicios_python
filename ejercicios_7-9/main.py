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
letras:str=""
palabra:str=input("ingrese un palabra: ")
for n in palabra:
    letras+=palabra[-1]
    print(letras)
    
#**Ejercicio Nueve**
##Escriba un programa que pregunte cuántos números se van a introducir, luego pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el anterior.
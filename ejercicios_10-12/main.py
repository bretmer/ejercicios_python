#**Ejercicio Diez**
##Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase:str=input("escriba una frase: ")
letra:str=input("escriba una letra: ")
contador_letra:int=0
for n in range(0,len(frase)):
    if frase[n]==letra:
        contador_letra+=1
print(f"la letra {letra} aparece {contador_letra} veces en la frase")
#**Ejercicio Once**
##Escriba un programa que pregunte cuantos números se van a introducir, pida los esos números (que puedan ser decimales) y calcule su suma, mostrar por terminal la suma de los números introducidos.
valores:int=int(input("¿cuantos valores va introducir?"))
suma=0
for _ in range(valores):
    numero_usuario:float=float(input("ingrese su numero: "))
    suma+=numero_usuario
print(f"la suma es {suma}")
#**Ejercicio Doce**
##Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.
valores:int=int(input("¿cuantos valores va introducir?"))
contador=0
for _ in range(valores):
     numero_usuario:int=int(input("escriba un numero: "))
     if numero_usuario <0:
          contador+=1
print(f"ha escrito {contador} numeros negativos")
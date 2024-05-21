#**Ejercicio Trece**
##Vamos a diseñar una calculadora que se enciende y hasta que no tecleamos `SAL` no se apaga.
#
##Esta calculadora funciona de la siguiente manera:
#
##- Recogemos los datos A y B
##- Si operación es 1 calcula la raíz cuadrada de la suma de A y B
##- Si operación es 2 calcula A / B. Vigilamos que B no sea 0...
##- Si la operación es 3 calculamos la siguiente fórmula: ( A * B ) / 2.5
encendida=True
while encendida:
    print("Bienvenido a la calculadora:")
    print("1. Calcular la raíz cuadrada de la suma de A y B")
    print("2. Calcular A / B")
    print("3. Calcular (A * B) / 2.5")
    print("Escribe 'SAL' para apagar la calculadora.")
    operacion:str=input("ingrese una operacion de la calculadora: ")
    if operacion == "SAL":
        break
    if operacion == "1":
        A:int=int(input("ingrese un numero: "))
        B:int=int(input("ingrese otro numero: "))
        resultado:float = 0.5**(A+B)
        print(f"el resultado es {resultado}")
    elif operacion == "2":
        A:int=int(input("ingrese un numero: "))
        B:int=int(input("ingrese otro numero: "))
        if B == 0:
            print("¡ERROR!")
        else:
            resultado:float = A/B
            print(f"el resultado es {resultado}")
    elif operacion == "3":
        A:int=int(input("ingrese un numero: "))
        B:int=int(input("ingrese otro numero: "))
        resultado:float = (A * B)/2.5
        print(f"el resultado es {resultado}")
#**Ejercicio Catorce**
##Tenemos la pantalla del móvil bloqueada. Partiendo de un `PIN_SECRETO`, intentaremos desbloquear la pantalla. Tenemos hasta 3 intentos. Simula el proceso con Python. En caso de acceder, lanza al usuario `login correcto`. Sino, `llamando ala policía`.
pin_secreto:str="2005"
intentos_restantes:int=3
while intentos_restantes >0 :
    pin_usuario:str=input("ingrese un PIN: ")
    if pin_usuario == pin_secreto:
        print("login correcto")
        break
    else:
        intentos_restantes -= 1
        if intentos_restantes >0:
            print(f"te quedan {intentos_restantes} intentos restantes")
        else:
            print("has agotado tus intentos.  Llamando a la policia")
#**Ejercicio Quince**
##Crea un algoritmo para la sucesión de Fibonacci. La sucesión de Fibonacci es la siguiente serie:
#
##`0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89`
#
##Pista: Empezando por 0 y 1, el siguiente número es la suma de los dos números últimos.
def fibonacci(n):
    secuencia_fibonacci=[0,1]
    while len(secuencia_fibonacci) < n:
        siguiente_numero=secuencia_fibonacci[-1]+secuencia_fibonacci[-2]
        secuencia_fibonacci.append(siguiente_numero)
    return secuencia_fibonacci
n_terminos=10
resultado=fibonacci(n_terminos)
print(f"los primeros {n_terminos} terminos de la sucecion fibonacci es {resultado}")   
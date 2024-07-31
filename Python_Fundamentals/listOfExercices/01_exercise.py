# Imprimir "Hola mundo"
print('hola mundo')

# Sumar dos números
suma = 2 + 2
print(suma)

# Función para sumar dos números
def sumarDosNumeros(a, b):
    return a + b

print(sumarDosNumeros(4, 56))

# Función para determinar si un número es par o impar
def numeroParImpar(number):
    if number % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"

# Solicitar al usuario un número y verificar si es par o impar
numero = int(input("Introduce un número: "))
resultado = numeroParImpar(numero)
print(resultado)

# Función para calcular el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar al usuario un número y calcular su factorial
numero = int(input("Introduce un número: "))
resultado = factorial(numero)
print('Calculando el factorial...')
print(f"El factorial de {numero} es {resultado}.")

# Función para verificar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Función para listar números primos hasta un valor dado
def listar_primos(hasta):
    primos = []
    for numero in range(2, hasta + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

# Listar y mostrar números primos entre 1 y 100
hasta = 100
primos = listar_primos(hasta)
print(f'Números primos entre 1 y {hasta}: {primos}')

#Invertir cadena con slicing 

def invertir_cadena_slicing(cadena):
    return cadena[::-1]
#cadena[::-1] es una técnica de slicing que toma la cadena completa y la lee de atrás hacia adelante.

cadena = "hola mundo"
cadena_invertida = invertir_cadena_slicing(cadena)
print(f'Cadena invertida: {cadena_invertida}')

#Invertir cadena sin slicing

def invertir_cadena_sin_slicing(cadena):
    cadena_invertida= ""
    for char in cadena:
        cadena_invertida = char + cadena_invertida
    return cadena_invertida

cadena = "Hola Mundo"
cadena_inv = invertir_cadena_sin_slicing(cadena)
print(f'Cadena invertida: {cadena_inv}')
### Exercises: Level 1

función listar_primos:

# Función para Listar Números Primos en un Rango

Este documento explica cómo encontrar todos los números primos en un rango dado utilizando Python. La implementación incluye dos funciones principales: `es_primo` para verificar si un número es primo, y `listar_primos` para listar todos los números primos hasta un número dado.

## Código

```python
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def listar_primos(hasta):
    primos = []
    for numero in range(2, hasta + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

# Ejemplo de uso
hasta = 100
primos = listar_primos(hasta)
print(f'Números primos entre 1 y {hasta}: {primos}')
Explicación
Función es_primo


def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
Entrada: Un número entero num.
Verificación:
Si num es menor que 2, retorna False (los números menores que 2 no son primos).
Usa un bucle para verificar si num es divisible por cualquier número desde 2 hasta la raíz cuadrada de num. Si encuentra un divisor, retorna False.
Si no encuentra divisores, retorna True (el número es primo).
Función listar_primos

def listar_primos(hasta):
    primos = []
    for numero in range(2, hasta + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos
Entrada: Un número entero hasta.
Proceso:
Inicializa una lista vacía primos.
Itera sobre todos los números desde 2 hasta hasta (inclusive).
Usa la función es_primo para verificar si cada número es primo. Si es así, lo añade a la lista primos.
Salida: Devuelve la lista primos con todos los números primos en el rango especificado.
Ejemplo de Uso

hasta = 100
primos = listar_primos(hasta)
print(f'Números primos entre 1 y {hasta}: {primos}')
Define el valor de hasta como 100.
Llama a la función listar_primos para obtener todos los números primos entre 2 y 100.
Imprime la lista de números primos.
Resumen
es_primo(num): Verifica si un número es primo.
listar_primos(hasta): Genera una lista de números primos en el rango de 2 hasta hasta.
El código es útil para encontrar números primos en un rango específico de manera eficiente y clara.
r





Rango en Python
En Python, la función range(start, stop) genera una secuencia de números comenzando desde start hasta stop - 1. El valor stop no se incluye en la secuencia generada.

Uso del hasta y el + 1
En la función listar_primos, utilizamos range(2, hasta + 1):


def listar_primos(hasta):
    primos = []
    for numero in range(2, hasta + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos
Explicación:
range(2, hasta + 1):

start = 2: Queremos empezar a verificar desde el número 2, ya que 1 no es considerado un número primo.
stop = hasta + 1: Queremos incluir el número hasta en el rango de verificación. Dado que range excluye el límite superior (stop), necesitamos sumar 1 a hasta para asegurarnos de que hasta esté incluido en la secuencia.
Por ejemplo:

Si hasta es 10, range(2, hasta + 1) se convierte en range(2, 11), que genera los números: 2, 3, 4, 5, 6, 7, 8, 9, 10. Así, 10 está incluido en la secuencia generada.

Si usamos range(2, hasta), para hasta = 10, la secuencia generada sería: 2, 3, 4, 5, 6, 7, 8, 9. En este caso, 10 no estaría incluido.

Resumen
hasta + 1 asegura que el número hasta esté incluido en la secuencia de números que se va a verificar.
Sin el + 1, el rango sería exclusivo del límite superior, y el número hasta no se verificaría si es primo.





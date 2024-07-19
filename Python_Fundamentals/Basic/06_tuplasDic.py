

# Crear una tupla
mi_tupla = (1, 2, 3, "a", "b", "c")
print("Tupla:", mi_tupla)

# Acceder a elementos de la tupla
print("Primer elemento:", mi_tupla[0])
print("Último elemento:", mi_tupla[-1])

# Desempaquetar tupla
a, b, c, d, e, f = mi_tupla
print("Desempaquetado:", a, b, c, d, e, f)

# Tupla anidada
tupla_anidada = (1, 2, (3, 4), 5)
print("Tupla anidada:", tupla_anidada)
print("Elemento de la tupla anidada:", tupla_anidada[2][1])

# Tupla inmutable
# mi_tupla[0] = 10  # Esto dará un error porque las tuplas son inmutables

# Ejemplos de Diccionarios

# Crear un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
print("Diccionario:", mi_diccionario)

# Acceder a valores del diccionario
print("Nombre:", mi_diccionario["nombre"])
print("Edad:", mi_diccionario["edad"])

# Añadir y modificar valores en el diccionario
mi_diccionario["edad"] = 31
mi_diccionario["profesión"] = "Ingeniero"
print("Diccionario modificado:", mi_diccionario)

# Eliminar un elemento del diccionario
del mi_diccionario["ciudad"]
print("Diccionario después de eliminar 'ciudad':", mi_diccionario)

# Iterar sobre un diccionario
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")

# Diccionario anidado
diccionario_anidado = {
    "persona1": {
        "nombre": "Juan",
        "edad": 30
    },
    "persona2": {
        "nombre": "Ana",
        "edad": 25
    }
}
print("Diccionario anidado:", diccionario_anidado)
print("Nombre de persona2:", diccionario_anidado["persona2"]["nombre"])

# if __name__ == "__main__": es un patrón común en Python utilizado para determinar si un archivo está siendo ejecutado directamente o 
#importado como un módulo en otro script.
if __name__ == "__main__":
    # Este bloque de código solo se ejecutará si el archivo se ejecuta directamente
    print(__name__)  # Imprime "__main__" si el archivo se ejecuta directamente
    
    pass  # El "pass" es un marcador de posición que no hace nada
#def es la palabra clave que indica que estás definiendo una función.

#"argumentos de longitud variable" o "argumentos variables" en Python. Este mecanismo permite 
# a la función aceptar un número indefinido de argumentos posicionales. 
# Los argumentos se agrupan en una tupla dentro de la función.

def ars(*numbers):
    print(numbers)
    resultado = sum(numbers)
    print(resultado)
    
    
ars(2,4,6,78,12,32,123,512,2)

#kwargs

#En Python, **kwargs se utiliza para permitir que una función acepte un número variable de argumentos
#con nombre (keyword arguments). La palabra kwargs significa "keyword arguments", pero puedes usar cualquier 
#nombre después de los dos asteriscos (**). Los argumentos se agrupan en un diccionario dentro de la función.


def imprimir_info(**info):
    print(info)  # 'info' es un diccionario que contiene todos los argumentos con nombre
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

# Llama a la función con varios argumentos con nombre
imprimir_info(nombre="Juan", edad=25, ciudad="Mdz")



def function_combinada( *args, **kwargs):
    print("Argumentos posicionales: ",args)
    print("Argumentos de palabra clave valor: ",kwargs)
    
function_combinada(1,2,3, nombre = "juan", edad= 25)




def function_condicional(value):
    if value > 0: 
     return "Positive"
    elif value < 0:
     return "Negative" 
    else:
        return "Cero"
result_condicional = function_condicional(2)
print(result_condicional)

#retornar multiples valores en una function
def basic_operations(a, b):
    try:
        addition = a + b
        subtraction = a - b
        multiplication = a * b
        division = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        division = None 

    return addition, subtraction, multiplication, division

# Usage example
result = basic_operations(10, 2)
print(result)
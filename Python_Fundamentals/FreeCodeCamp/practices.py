word = "banana"
i = word.find("na")
print(i)    

#salto de linea
stuff = "x\nY"
print(stuff)


my_list = ["hola","como"]

my_list.append("estas")
print(my_list)


words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
print(pieces)
parts = pieces[3]
print(parts)
partsSplint = parts.split("-")
print(partsSplint)



#dict = {"Fri": 20, "Thu": 15, "Sat": 1}
#dict["Thu"] = 13
#dict ["Sat"] = 2
#dict ["Sun"] = 9

#print(dict)

#showDict = dict.get("Thasdasu",0)
#print(showDict)


# Bucle for: Itera sobre cada clave (key) en el diccionario counts.
#Condición if: Verifica si el valor asociado a la clave actual (counts[key]) es mayor que 10.
#Imprimir: Si la condición es verdadera, imprime la clave y su valor.

counts = {"chuck": 1, "annie": 42, "jan": 100}

for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
        
    
 

d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)


#El método items() devuelve una vista de pares clave-valor del diccionario d. Esta vista es un objeto dict_items,
# que contiene las tuplas de pares clave-valor.
    
f = {'quincy': 1, 'beau': 5, 'kris': 9}

items = f.items()

print(items)



lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)



print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )


import re  # Importa el módulo de expresiones regulares

# Suponiendo que 's' es una cadena que contiene texto
s = "example1@example.com, example2@domain.net"

# Encuentra todas las coincidencias del patrón de expresión regular '\\S+@\\S+' en la cadena 's'
# \\S+@\\S+ es una expresión regular que busca coincidencias de patrones de correo electrónico básicos:
# - \\S+ busca uno o más caracteres que no sean espacios en blanco (\\S significa "no espacio en blanco" y el + significa "uno o más")
# - @ busca el carácter arroba '@'
# - \\S+ busca uno o más caracteres que no sean espacios en blanco después del '@'
lst = re.findall('\\S+@\\S+', s)

# 'lst' ahora contiene una lista de todas las coincidencias encontradas en la cadena 's'
print(lst)  # Salida: ['example1@example.com', 'example2@domain.net']

a = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S', a)
print(lst)
#['csev@umich.edu', 'cwen@iupui.edu']

#sin el + queda
#['csev@u', 'cwen@i']

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()
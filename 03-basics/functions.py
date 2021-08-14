def mi_funcion():
    print('Hello world!')

mi_funcion()

def saludar_usuario(nombre):
    print(f"Hey hola {nombre}!")

saludar_usuario('Jason')

# Retornando un valor en una funcion
def sumar(x, y):
    return x + y

resultado = sumar(5,4)
print(resultado)


# Los valroes por defectoo es cuando no mandamos un valor por argumento entocnes vamos a asignarle uno en caso de no recivir algo
def saludar(nombre = 'World'):
    print(f'Hello {nombre}')

saludar('Jason')

# Vamos recibir una cantidad de parametros desconocida asi que hacemos lo siguiente

def agenda(*names):
    for i in names:
        print(i)
# al poner un * antes del nombre del argumento python lo convertira en una tupla
   
agenda('Jake','Limon','Benito')

# Ahora python el parametro lo convertira a un diccionario el primer ejemplo es com apsar un diccionario y el segundo como python convertira en un diccionario

def pasar_diccionario(diccionairo_fun):
    print(diccionairo_fun)
otro_diccionario = {1:'Jason', 2:'Giovani', 3:'Limon', 4:'Benito'}
pasar_diccionario(otro_diccionario)

def convertir_diccionario(**datos):
    for key, value in datos.items():
        print(f"La llave es {key} y su valor es {value}", end="\n\t")
    else:
        print('final de una funcion que su parametro lo convierte en un diccionario')

convertir_diccionario(
    PK="Primary Key",
    FK="Foreign Key",
    ASAP="A Soon As Posible"
)


otro = b'h\x65llo'
print(list(otro))
print(otro)

mistr = b'Jason'
print(list(mistr))
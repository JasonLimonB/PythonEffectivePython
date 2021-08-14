# Un diccionario defina una relacion uno a uno entre clave y valor

diccionario = {'clave1': 123, 'clave2':456, 'clave3':789, 'clave4': None}
print(diccionario)

print(diccionario['clave1'])

diccionario['clave4'] = 'LimonJake'

print(diccionario)

print(diccionario.get('clave1'))

print(diccionario.values())



# con dict indicamos a crear un diccionario pero con zip pasamos en un string las claves y como segundo parametro los valores pero en una lista
mi_diccionario = dict(zip('abcd',[1,2,3,4]))

print(mi_diccionario)

keys = mi_diccionario.keys()
print(keys)



# Vamos a trabajar con uns set

mi_set = {'Jake', 'Pam', 'Limon', 'Romero'}
print(mi_set)

# Tenemos metodos muy similares que en tuplas y asi
print('Jake' in mi_set)

mi_set.add('Benito')
print(mi_set)

mi_set.add('Jake')
print(mi_set)
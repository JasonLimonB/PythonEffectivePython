contador = 0

while contador <= 10:
    print(contador)
    contador += 1
else:
    print('Fin del ciclo while')


# Comenzando con el ciclo for

name = 'Jason'
print(len(name))
for i in name:
    print(i)

mi_arr = ['Jason', 'Giovani', 'Limon', 'Benito']

for i in mi_arr:
    print(i, end=' -> ') # Podemos agregar la palabra end para indicar como o qu ira depues de cada iteracion o si todo estara en una sola linea
else:
    print('Final de bucle for')

# Cuando no es tan necesario la informacion que estanmos iterando podemos reemplazar nuestro iterado por un _

for _ in mi_arr:
    print('El iterador no es necesario')
else:
    print('Fin del for sin importancia la iterador')


# igual podemos agregar un range para indicar cuantas veces queremos imprimir en el for
for _ in range(10):
    print('Usando range para el for')

for i in range(5):
    print(i)
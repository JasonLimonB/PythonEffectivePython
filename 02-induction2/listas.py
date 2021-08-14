names = ['Jason', 'Limon', 'Pamela', 'Diana', 'Mauricio', 'Jair', 'Jason']
print(names)

for i in names:
    print(i)

print(names[0])
print(names[-1])
print(names[0:3]) # Sin incluir el valo 3 sio queremo el valor 3 debemos poner un 4 en este caso
print(names[0:4])

print(len(names)) # Cantidad de elementos que contiene nuestra lista

names.append('Nuevo elemento')
print(names)

print(names.count('Jason'))
string_variable = "Jason Limon"
print(type(string_variable))

number_variable = 25
print(type(number_variable))

#Tambien podemos poner como una idicacion de que tipo de dato vamos almacenar en una variable pero esto no afecta al tipo de dato vaya no lo hace fuertemente tipado

ejemplo_varable: str = "Ejemplo de indicando el tipo como pista"
print(ejemplo_varable)

# si cambiamos el tipo de dato lo cambiara ya que solo es como guia de lo que almcenara

ejemplo_varable = 1234
print(ejemplo_varable)

#tipos flotantes solo es agregar el punto en el la declaracion de la variable

flotantes: float = 25.9
print(type(flotantes))

# Para datos booleanos hacemos lo siguiente

my_boolean = False
print(type(my_boolean))


#Usando cadenas de caracteres, concatenar

mi_banda_favorita = "Led Zeppelin"
print("Mi banda favorita es " +mi_banda_favorita)
print("Seguimos con mi banda favtorita ", mi_banda_favorita)
print(f"Mi badna favorita es {mi_banda_favorita}")

edad = 25

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Lo siento no eres mayor de edad")
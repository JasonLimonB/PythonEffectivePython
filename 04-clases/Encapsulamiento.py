import math # Una importacion rapida es de esta manera y ya esta en el core al menos esta libreria en el core de python

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self._apellido = apellido # Para indicar que es un atributo protect o pretejido 
        self.__edad = edad # Para indicar un atributo o metodo privado o private es poner doble guin bajo
    

persona = Persona("Jason", "Limon", 25)

print(persona.nombre) # En teoria no deberiamos acceder de esta manera a los atributos ya que solo deberian de ser de la clase
print(persona._apellido) # A pesar que si podemos acceder a este atributo no es lo mas correcto ya que esta indicado como encapsulado
# print(persona.__edad)  Si hacemos esto no vamos a tener acceso a ese atributo o metodo y mandar un error
print(persona._Persona__edad) # Pero si hacemos esto podemos acceder a ese atributo o metodo

print(math.floor(55.62))
print(math.pow(5, 2))
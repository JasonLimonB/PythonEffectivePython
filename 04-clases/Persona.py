# Para crear una clase debemos usar la pal;abra reservada class y ademas toda clase debera tener la primer letra de cada palabra en mayusculas
# SoyUnaClase  MiClase  PersonaAdulta --> solo por nombrar unos ejemplos

class Persona:

    # En esta parte es como el constructor ya que aqui es donde definimos los parametros de una clase, por ahora esta en codigo duro
    def __init__(self):
        self.nombre = 'Jason'
        self.apellido = 'Limon'
        self.edad = 25

persona1 = Persona()

print(f'El objeto persona tiene el nombre {persona1.nombre} {persona1.apellido} y tiene {persona1.edad}')
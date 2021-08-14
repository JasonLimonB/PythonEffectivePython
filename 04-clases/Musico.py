# Al momento de agregar parametros a nuestro constructor por llamarlo asi sera despues de self ya que es la referencia a la clase
# Para entender un poco self es algo parecdo al this en otros lengujes

class Musico:
    def __init__(self, nombre, instrumento):
        self.nombre = nombre
        self.instrumento = instrumento
    
# Como podemos ver al crear el objeto no usamos new como en otros lenguajes y ademas no pasamos el self al momento de instanciar el objeto
guitarrista = Musico('Jason', 'Guitarra')


print(guitarrista.nombre)
print(guitarrista.instrumento)
        
bajista = Musico('Mauricio', 'Bajo')
print(f'{bajista.nombre} toca el {bajista.instrumento}')
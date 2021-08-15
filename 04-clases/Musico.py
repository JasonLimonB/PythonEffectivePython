# Al momento de agregar parametros a nuestro constructor por llamarlo asi sera despues de self ya que es la referencia a la clase
# Para entender un poco self es algo parecdo al this en otros lengujes

class Musico:
    def __init__(self, nombre, instrumento):
        self.nombre = nombre
        self.instrumento = instrumento
    
    # Hasta los metodos deben llevar la referencia de self ya que es obligatorio
    def mostrar_detalle(self):
        print(f'El musico {self.nombre} toca el o la {self.instrumento}')

# Como podemos ver al crear el objeto no usamos new como en otros lenguajes y ademas no pasamos el self al momento de instanciar el objeto
guitarrista = Musico('Jason', 'Guitarra')


print(guitarrista.nombre)
print(guitarrista.instrumento)
        
bajista = Musico('Mauricio', 'Bajo')
print(f'{bajista.nombre} toca el {bajista.instrumento}')

bajista.mostrar_detalle()

# Podemos mandar a llamar al metodo con la clase pero necesitamos mandar por parametro la referencia de un objeto
Musico.mostrar_detalle(guitarrista)


# Podemos agregar un nuevo atributo a la clase pero solo indicado a un sol oobjeto por ejemplo
guitarrista.concierto = 'Auditorio Nacional'

print(guitarrista.concierto)
print(bajista.concierto)

# Mandara un error  en el caso de nuestro primer objeto si nos tomara el atributo como existente
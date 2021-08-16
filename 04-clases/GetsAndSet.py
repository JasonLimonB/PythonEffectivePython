class Empleado:
    def __init__(self, nombre, puesto, id) -> None:
        self._nombre = nombre
        self.__puesto = puesto
        self.__id = id
    
    # De la siguiente manera declaramos los getters
    def nombre(self):
        return self._nombre

    def id_empleado(self):
        return self.__id

    @property
    def puesto_empleado(self) -> str: # Con este decorador la funcion podremos usarla como propiedad osea sin usar parentesis
        return self.__puesto
    
    # Ahora vamos a poner un setter osea modificar un atributo de nuestra clase y es con el decorador nombre del atributo mas la palabra setter
    # Para esto debemos usar property y el mismo nombre que usamos en el get 
    @puesto_empleado.setter
    def puesto_empleado(self, puesto) -> None: # Recibimos tambien el nuevo valor a modificar
        self.__puesto = puesto
    

dev = Empleado('Jake', 'Software Developer', 2442)
print(dev.nombre()) # De esta manera podemos acceder al nombre con un metodo protect

print(dev.id_empleado()) # De la misma manera podemos acceder a lo que es private

print(dev.puesto_empleado) # Como podemos ver imprimira el puesto y no es necesario de usar los parentesis

dev.puesto_empleado = "Software Enginner"
print(dev.puesto_empleado)
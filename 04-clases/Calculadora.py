class Calculadora:
    def __init__(self, operadorA, operadorB):
        self.operadorA = operadorA
        self.operadorB = operadorB

    def sumar(self):
        return self.operadorA + self.operadorB
    
    def restar(self): # Para usar los parametros pedidos por init es usando self mas el nombre del paramtro
        return self.operadorA - self.operadorB
    
    def otro(self, name): # A pesar de los paramtros de la clase por el metodo init podemos pedir parametros en un metodo que necesitemos
        print("Metodo otro", name)
    

miCalculadora = Calculadora(20,11)
print(miCalculadora.sumar())
print(miCalculadora.restar())
miCalculadora.otro("Jake")

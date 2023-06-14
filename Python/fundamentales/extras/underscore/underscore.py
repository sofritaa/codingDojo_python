class Underscore:
    def map(self, iterable, callback):
        resultado = []
        for elemento in iterable:
            resultado.append(callback(elemento))
        return resultado
    
    def find(self, iterable, callback):
        for elemento in iterable:
            if callback(elemento):
                return elemento
        return None
    
    def filter(self, iterable, callback):
        resultado = []
        for elemento in iterable:
            if callback(elemento):
                resultado.append(elemento)
        return resultado
    
    def reject(self, iterable, callback):
        resultado = []
        for elemento in iterable:
            if not callback(elemento):
                resultado.append(elemento)
        return resultado

_ = Underscore()

doble = _.map([1, 2, 3], lambda x: x * 2)
print(doble)  # Output: [2, 4, 6]

mayor_cuatro = _.find([1, 2, 3, 4, 5, 6], lambda x: x > 4)
print(mayor_cuatro)  # Output: 5

pares = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(pares)  # Output: [2, 4, 6]

impares = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(impares)  # Output: [1, 3, 5]

class MathDojo:
    def __init__(self):
        self.resultado = 0

    def sumar(self, num, *nums):
        self.resultado += num
        for n in nums:
            self.resultado += n
        return self

    def restar(self, num, *nums):
        self.resultado -= num
        for n in nums:
            self.resultado -= n
        return self
md = MathDojo()

x = md.sumar(2).sumar(2, 5, 1).restar(3, 2).resultado
print(x)  

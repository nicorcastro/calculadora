import math

# Clase para operaciones aritméticas
class Aritmetica:
    def __init__(self):
        self.número_a = 0
        self.número_b = 0
        
    def suma(self):
        return self.número_a + self.número_b
    
    def resta(self):
        return self.número_a - self.número_b
    
    def multiplicacion(self):
        return self.número_a * self.número_b
    
    def division(self):
        if self.número_b == 0:
            return "No es posible dividir entre cero"
        else:
            return self.número_a / self.número_b
    

# Clase para operaciones trigonométricas
class Trigonometrica:
    def __init__(self):
        self.ángulo = 90
        
    def seno(self):
        x = math.radians(self.ángulo)
        return math.sin(x)
    
    def coseno(self):
        x = math.radians(self.ángulo)
        return math.cos(x)
    
    def tangente(self):
        x = math.radians(self.ángulo)
        return math.tan(x)
    
    def cotangente(self):
        x = math.radians(self.ángulo)
        return 1/math.tan(x)
    
    def secante(self):
        x = math.radians(self.ángulo)
        return 1/math.cos(x)
    
    def cosecante(self):
        x = math.radians(self.ángulo)
        return 1/math.sin(x)
    

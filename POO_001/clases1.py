from abc import ABC, abstractmethod
import math

class FG(ABC):

    def __init__(self , lado1:float):
        #Si queremos que sea protegido colocamos un guion bajo, si queremos que sea privado dos guiones bajo antes del nombre
        self.lado1 = lado1

    def __str__(self) -> str:
        return f"Lado 1: {self.lado1:.2f}" 

    @abstractmethod
    def calcular_area(self):
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        pass

class Cuadrado(FG):

    def calcular_area(self):
        return math.pow(self.lado1 , 2)
    
    def calcular_perimetro(self):
        return 4*self.lado1

    def __str__(self) -> str:
        return "Cuadrado: "+ super().__str__()

class Rectangulo(FG):

    def __init__(self,lado1:float,lado2:float):
        self.lado1=lado1
        self.lado2=lado2

    def calcular_area(self):
        return self.lado1*self.lado2
    
    def calcular_perimetro(self):
        return 2*(self.lado1+self.lado2)

    def __str__(self) -> str:
        return "Rectangulo: "+ super().__str__()+f" ,lado2: {self.lado2:.2f}"
    
class Cubo(Cuadrado):
    
    def calcular_area(self):
        return 6*math.pow(self.lado1,2)
    
    def calcular_volumen(self):
        return math.pow(self.lado1,3)

    def calcular_perimetro(self):
        return 12*self.lado1

    def __str__(self):
        return f"Cubo: lado1: {self.lado1:.2f}"

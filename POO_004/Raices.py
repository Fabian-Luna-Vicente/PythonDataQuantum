from dataclasses import dataclass
import math
@dataclass
class Raices():
    a:float
    b:float
    c:float

    def getDiscriminante(self):
        return math.pow(self.b, 2)-4*self.a*self.c

    def TieneRaices(self):
        discriminante=self.getDiscriminante()
        if discriminante >=0:
            return True
        else:
            return False

    def TieneRaiz(self):
        discriminante=self.getDiscriminante()
        if discriminante==0:
            return True
        return False


    def obtenerRaiz(self):
        return self.b*-1/2*self.a

    def obtenerRaices(self):
        discriminante=self.getDiscriminante()
        sol1=(self.b*-1)+math.sqrt(discriminante)/2*self.a
        sol2=(self.b*-1)-math.sqrt(discriminante)/2*self.a
        return sol1,sol2
    
    def calcular(self):
        if self.TieneRaices():
            if self.TieneRaiz():
                print(f"Tiene una unica solucion: {self.obtenerRaiz()}")
                return
            sol1,sol2=self.obtenerRaices()
            print(f"Tiene dos raices: solucion1: {sol1} , solucion2: {sol2}")
            return
        print(f"No hay soluciones")
        return

if __name__=='__main__':
    Raices(1,-4,4).calcular()
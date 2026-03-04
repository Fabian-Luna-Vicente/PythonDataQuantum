from enum import Enum
from abc import ABC, abstractmethod

class Letra(Enum):
    A=100
    B=80
    C=60
    D=50
    E=30
    F=10

class Color(Enum):
    BLANCO="blanco"
    NEGRO="negro"
    AZUL="azul"
    ROJO="rojo"
    GRIS="gris"

peso_precio=[[19,10],[49,50],[79,80],[80,100]]

class Electrodomestico(ABC):

    def __init__(self,precio_base:float,color:str="blanco",consumo_energetico:str="F",peso:float=5):
            self.__precio_base=precio_base
            self.comprobarColor(color)
            self.comprobarConsumoEnergetico(consumo_energetico)
            self.__peso=peso

    def obtenerPrecioBase(self):
        return self.__precio_base
    def obtenerColor(self):
        return self.__color
    def obtenerConsumoEnergetico(self):
        return self.__consumo_energetico
    def obtenerPeso(self):
        return self.__peso

    def establecerPrecioBase(self,precio_base:float):
        self.__precio_base=precio_base
    def establecerColor(self,color:Color):
        self.__color=color
    def establecerConsumoEnergetico(self,consumo_energetico:Letra):
        self.__consumo_energetico=consumo_energetico
    def establecerPeso(self,peso:float):
        self.__peso=peso 
    
    def comprobarConsumoEnergetico(self,consumo_energetico:str):
        if consumo_energetico.upper() not in Letra.__members__:
            self.__consumo_energetico=Letra.F
        else:
            self.__consumo_energetico=Letra[consumo_energetico.upper()]
    
    def comprobarColor(self,color:str):
        if color.upper() not in Color.__members__:
            self.__color=Color.BLANCO
        else:
            self.__color=Color[color.upper()]

    def calcularPrecioConPeso(self):
        for i in peso_precio:
            if self.__peso<=i[0]:
                return i[1]
        return peso_precio[-1][1]
    
    def calcularPrecioBase(self):
        precio_consumo=self.__consumo_energetico.value
        precio_peso=self.calcularPrecioConPeso()
        precio_final=self.__precio_base+precio_consumo+precio_peso
        self.__precio_base=precio_final
        return precio_final

    @abstractmethod
    def precioFinal(self):
        pass

    def __str__(self):
        return f"Precio Base: {self.__precio_base} Color: {self.__color} Consumo Energetico: {self.__consumo_energetico} Peso: {self.__peso}"

from Electrodomestico import Electrodomestico

class Lavadora(Electrodomestico):
    def __init__(self,precio_base:float,color:str="blanco",consumo_energetico:str="F",peso:float=5,carga:float=5):
        super().__init__(precio_base,color,consumo_energetico,peso)
        self.__carga=carga
    
    def obtenerCarga(self):
        return self.__carga
    
    def precioFinal(self):
        precio_final=super().calcularPrecioBase()
        if self.__carga>30:
            precio_final+=50
        return precio_final

    def __str__(self):
        return f"Precio Base: {super().obtenerPrecioBase()} Color: {super().obtenerColor()} Consumo Energetico: {super().obtenerConsumoEnergetico()} Peso: {super().obtenerPeso()} Carga: {self.__carga}"
from Electrodomestico import Electrodomestico

class Television(Electrodomestico):
    def __init__(
        self,
        precio_base:float,
        color:str="blanco",
        consumo_energetico:str="F",
        peso:float=5,
        resolucion:int=20,
        sintonizadorTDT:bool=False):

        super().__init__(precio_base,color,consumo_energetico,peso)

        self.__resolucion=resolucion
        self.__sintonizadorTDT=sintonizadorTDT
        
    def precioFinal(self):
        precio_final=super().calcularPrecioBase()
        if self.__resolucion>40:
            precio_final+=precio_final*0.3
        if self.__sintonizadorTDT:
            precio_final+=50
        return precio_final

    def __str__(self):
        return f"Precio Base: {super().obtenerPrecioBase()} Color: {super().obtenerColor()} Consumo Energetico: {super().obtenerConsumoEnergetico()} Peso: {super().obtenerPeso()} Resolucion: {self.__resolucion} Sintonizador TDT: {self.__sintonizadorTDT}"

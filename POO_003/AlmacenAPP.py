from Lavadora import Lavadora
from Television import Television

electrodomesticos=[]

def llenarAlmacen():
        electrodomesticos.append(Lavadora(100,"blanco","A",5,5))
        electrodomesticos.append(Television(100,"blanco","A",5,5,True))
        electrodomesticos.append(Television(100,"negro","C",50,5))
llenarAlmacen()

for e in electrodomesticos:
    print(e)
    print(f"Precio Final: {e.precioFinal()}")
from clases1 import Cuadrado,Rectangulo,Cubo

def imprimir():
    global lista
    for i in lista:
        print(i)
        print("Area: ",i.calcular_area())
        print("Perimetro: ",i.calcular_perimetro())
        if isinstance(i,Cubo):
            print("Volumen: ", i.calcular_volumen())

def contar():
    global lista
    contador={"cubo":0,"cuadrado":0,"rectangulo":0}
    for i in lista:
        match i.__class__.__name__:
            case "Cubo":
                contador["cubo"]+=1
            case "Cuadrado":
                contador["cuadrado"]+=1
            case "Rectangulo":
                contador["rectangulo"]+=1
    print(contador)

def contar2():
    global lista
    contador={"Cubo":0,"Cuadrado":0,"Rectangulo":0}
    for i in lista:
        contador[i.__class__.__name__]+=1
    print(contador)

if __name__=='__main__':
    lista=[]
    lista.append(Cuadrado(5))
    lista.append(Cuadrado(10))
    lista.append(Rectangulo(12,4))
    lista.append(Cubo(20))
    imprimir()
    contar()
    contar2()
    
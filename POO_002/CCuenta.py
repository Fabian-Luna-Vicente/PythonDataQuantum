
class CCuenta:
    def __init__(self,nombre:str,cuenta:str,slado:float,tipoDeInteres:float):
        self.__nombre=nombre
        self.__cuenta=cuenta
        self.__saldo=slado
        self.__tipoDeInteres=tipoDeInteres

    def asignarNombre(self,nombre:str):
        self.__nombre=nombre

    def obtenerNombre(self) ->str:
        return self.__nombre

    def asignarCuenta(self,cuenta:str):
        self.__cuenta=cuenta

    def obtenerCuenta(self) ->str:
        return self.__cuenta

    def asignarSaldo(self,saldo:float):
        self.__saldo=saldo

    def obtenerSaldo(self) ->float:
        return self.__saldo

    def asignarTipoDeInteres(self,tipoDeInteres:float):
        self.__tipoDeInteres=tipoDeInteres

    def obtenerTipoDeInteres(self) ->float:
        return self.__tipoDeInteres

    def ingreso(self,cantidad:float):
        self.__saldo+=cantidad

    def reintegro(self,cantidad:float):
        self.__saldo-=cantidad

    def estado(self):
        return self.__saldo

    @abstractmethod
    def interes(self):
        pass

    @abstractmethod
    def comisiones(self):
        pass
    
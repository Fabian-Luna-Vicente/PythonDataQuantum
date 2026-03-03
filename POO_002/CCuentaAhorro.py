class CCuentaAhorro(CCuenta):
    def __init__(self,nombre:str,cuenta:str,slado:float,tipoDeInteres:float,cuotaMantenimiento:float):
        super().__init__(nombre,cuenta,slado,tipoDeInteres)
        self.__cuotaMantenimiento=cuotaMantenimiento

    def asignarCuotaMantenimiento(self,cuotaMantenimiento:float):
        self.__cuotaMantenimiento=cuotaMantenimiento

    def obtenerCuotaMantenimiento(self) ->float:
        return self.__cuotaMantenimiento

    def interes(self):
        self.__saldo+=self.__saldo*self.__tipoDeInteres

    def comisiones(self):
        self.__saldo-=self.__saldo*self.__cuotaMantenimiento

class CCuentaCorrienteConIn(CCuentaCorriente):
    def __init__(
        self,nombre:str,
        cuenta:str,
        slado:float,
        tipoDeInteres:float,
        transacciones:int,
        importePorTrans:float,
        transExentas:int,
        ):
        super().__init__(nombre,cuenta,slado,tipoDeInteres,transacciones,importePorTrans,transExentas)
        self.__intereses=intereses

    def asignarIntereses(self,intereses:float):
        self.__intereses=intereses

    def obtenerIntereses(self) ->float:
        return self.__intereses

    def interes(self):
        if super().obtenerSaldo(self) >=3000:
            super().interes(self)

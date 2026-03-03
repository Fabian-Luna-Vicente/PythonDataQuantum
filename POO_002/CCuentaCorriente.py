class CCuentaCorriente(CCuenta):
    def __init__(
        self,nombre:str,
        cuenta:str,
        slado:float,
        tipoDeInteres:float,
        transacciones:int,
        importePorTrans:float,
        transExentas:int,
        ):
        super().__init__(nombre,cuenta,slado,tipoDeInteres)
        self.__transacciones=transacciones
        self.__importePorTrans=importePorTrans
        self.__transExentas=transExentas

    def decrementarTransacciones(self):
        self.__transacciones-=1

    def asignarImportePorTrans(self,importePorTrans:float):
        self.__importePorTrans=importePorTrans
    
    def obtenerImportePorTrans(self) ->float:
        return self.__importePorTrans

    def asignarTransExentas(self,transExentas:int):
        self.__transExentas=transExentas

    def obtenerTransExentas(self) ->int:
        return self.__transExentas

    def ingreso(self,cantidad:float):
        super().ingreso(self,cantidad)
        self.__transacciones+=1

    def reintegro(self,cantidad:float):
        super().reintegro(self,cantidad)
        self.__transacciones+=1 

    def interes(self):
        comision=0.5
        limite=3000
        saldo=super().obtenerSaldo(self)
        resto= limite- saldo

        if resto >=0:
            super().asignarSaldo(self,saldo+ comision*limite/1200)
        if resto >0:    
            super().asignarSaldo(self,saldo+super().obtenerTipoDeInteres(self)*saldo/1200)

    def comisiones(self):
        saldo=super().obtenerSaldo(self)
        super().asignarSaldo(self,saldo-self.__importePorTrans*(self.__transacciones-self.__transExentas))
        self.__transacciones=0
        
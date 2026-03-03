class CBanco:
    def __init__(self,clientes:list):
        self._clientes=clientes

    def insertarCliente(self,cliente):
        self._clientes.append(cliente)

    def eliminarCliente(self,cliente):
        self._clientes.remove(cliente)

    def obtenerClientes(self):
        return self._clientes

    def longitud(self):
        return len(self._clientes)
    
    def buscar(self,dato):
        for cliente in self._clientes:
            if cliente.obtenerNombre()==dato or cliente.obtenerCuenta()==dato:
                return cliente
        return None
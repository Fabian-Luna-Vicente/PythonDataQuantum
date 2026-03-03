from CBanco import CBanco
opciones=[
    {"name":"Saldo","fun":saldo},
    {"name":"Buscar siguiente","fun":buscar_siguiente},
    {"name":"Ingreso","fun":Ingreso},
    {"name":"Reintegro","fun":Reintegro},
    {"name":"Añadir","fun":Añadir},
    {"name":"Eliminar","fun":Eliminar},
    {"name":"Mantenimiento","fun":Mantenimiento},
    {"name":"Salir","fun":None}

]

miBanco=CBanco()
def Menu():
    op=0
    while op!=len(opciones):
        for i,e in enumerate(opciones):
            print(f"{str(i)} {e["name"]}")
        try:
            op=int(input("SELCCIONA UNA OPCION: "))
            if (op >len(opciones)):
                 input("No es un numero valido , pulse cualquier letra para continuar... ")
                 return
            if (op==len(opciones)):
                print("Adiosss..")
                return
            opciones[op-1]["fun"]()
            input("pulse cualquier letra para continuar... ")

        except ValueError:
            input("No es un numero valido , pulse cualquier letra para continuar... ")
            return

    
def pedir_y_retornar_cliente():
    nombre=input("Ingresa el nombre o cuenta del cliente")
    return miBanco.buscar(nombre)
    
def saldo():
    cliente=pedir_y_retornar_cliente()
    if cliente:
        print(f"Saldo del Cliente {cliente.obtenerNombre()} es: {cliente.estado()}")
    else:
        print("No se encontro cliente")

def buscar_siguiente():
    cliente=pedir_y_retornar_cliente()
    if cliente:
        print(cliente)
    else:
        print("No se encontro cliente")

def Ingreso():
    cliente=pedir_y_retornar_cliente()
    if not cliente:
        print("No se encontro cliente")
    else:
        try:
            cantidad=float(input("Ingrese la cantidad a añadir a :" +cliente.obtenerNombre())) 
            cliente.ingreso(cantidad)
            print("Cantidad añadida con exito!")
        except ValueError:
            print("Coloca un valor valido..")

def Reintegro():
    cliente=pedir_y_retornar_cliente()
    if not cliente:
        print("no se encontro cliente.")
    else:
        try:
            cantidad=float(input(f"Ingrese la cantidad a quitar a : {cliente.obtenerNombre()} saldo: {cliente.estado():.2f} -->")) 
            cliente.ingreso(cantidad)
            print("Operacion terminada!")
        except ValueError:
            print("Coloca un valor valido..")

def Añadir():
    nuevo=None
    while not nuevo:
        tipos=["CCuentaAhorro","CCuentaCorriente","CCuentaCorrienteConInt"]
        tipo=-1
        while tipo<=0 or tipo>len(tipos):
            for i,t in enumerate(tipos):
                print(f"{1}.-{t}")
            try:
                tipo=int(input("selecciona un tipo de cuenta --> "))
            except ValueError:
                print("valor incorrecto")
        try:
            nombre=input("Ingresa el nombre: ")
            cuenta=input("Ingresa la cuenta: ")
            tipoDeInteres=float(input("Ingresa el tipo de interes (Anual): "))

            match tipo:
                case 1:
                    cuotaMantenimiento=int(input("Ingrese Cuota Mantenimiento: "))
                    nuevo=CCuentaAhorro(nombre,cuenta,tipoDeInteres,cuotaMantenimiento)
                case 2 ,3:
                    importePorTrans=float(input("Seleccione el importe por transferencia: "))
                    transExentas=int(input("Seleccione el nuemro de transferencias excentas: "))
                    if tipo==2:
                        nuevo=CCuentaCorriente(nombre,cuenta,tipoDeInteres,importePorTrans,transExentas)
                    else:
                        nuevo=CCuentaCorrienteConInt(nombre,cuenta,tipoDeInteres,importePorTrans,transExentas)
            print("Cuenta Añadida Correctamente.")

        except ValueError:
            print("Por favor selecciona un valor valido..")

def Eliminar():
    cliente=pedir_y_retornar_cliente()
    if not cliente:
        print("No se ha encontrado el cliente.")
    else:
        miBanco.eliminarCliente(miBanco.obtenerClientes().index(cliente))
        print("Operacion Finalizada.")

def Mantenimiento():
    fecha_actual=datetime.now()
    if fecha_actual.day()==1:
        for c in miBanco.obtenerClientes():
            c.interes()
            c.comision()
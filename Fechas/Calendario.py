from datetime import datetime
import calendar

def pedirFecha():
    fecha=input("Dime una fecha (dd/mm/aaaa): ")
    fecha=datetime.strptime(fecha,"%d/%m/%Y")
    return fecha

def calendario(fecha:datetime):
    Dias=["  L ","  M ","  X ","  J ","  V ","  S ","  D "]
    dias_inicio=calendar.monthrange(fecha.year,fecha.month)
    semana_actual=dias_inicio[0]
    for d in Dias:
        print(d,end="")
    print()
    for e in range(0,dias_inicio[0]):
        print("  . ",end="")

    for i in range(1,dias_inicio[1]):

        color_inicio="\033[31m" if fecha.day==i else ""
        reset="\033[0m" if fecha.day==i else ""
        cadena=f"{color_inicio} {i:2d} {reset}" 

        print(cadena,end="" if not semana_actual==6 else None)
        
        if semana_actual==6:
            semana_actual=0
        else:
            semana_actual+=1

if __name__=='__main__':
    fecha=pedirFecha()
    calendario(fecha)
        
            

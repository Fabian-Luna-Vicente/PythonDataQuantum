from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta
import locale

def ultimoViernes(fecha:datetime):
    unmesmas=relativedelta(months=1,days=-1)
    undiamenos=timedelta(days=1)
    fecha+=unmesmas
    while fecha.strftime("%A").capitalize() !='Viernes':
        fecha-=undiamenos
    return fecha

def fechas(fecha:datetime):
    for i in range(1,13):
        fecha=fecha.replace(month=i)
        print(ultimoViernes(fecha).strftime("%d/%m/%Y"))

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL,'es_ES')
    fecha=datetime(2026,1,1)
    fechas(fecha)
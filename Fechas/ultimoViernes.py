from datetime import datetime,timedelta
import locale

locale.setlocale(locale.LC_ALL,'es_ES.UTF-8')

fecha_inicio=datetime(2026,1,1)

undiamas=timedelta(days=1)
unasemanamas=timedelta(days=7)

fecha_actual=fecha_inicio
#fecha_inicio=datetime.strptime(fecha_inicio,'%d/%m/%Y')

print(fecha_actual.strftime("%A").capitalize)
while fecha_actual.strftime("%A").capitalize() != 'Viernes':
    fecha_actual +=undiamas

ultimos_viernes=[]

for i in range(1,13):
    ultimo_viernes=""
    while fecha_actual.month ==i:
        ultimo_viernes=fecha_actual
        fecha_actual+=unasemanamas
    ultimos_viernes.append( ultimo_viernes )

for e in ultimos_viernes:
    print(e)
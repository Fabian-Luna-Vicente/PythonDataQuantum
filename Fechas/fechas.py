from datetime import datetime,timedelta
import locale

fecha = input('Dime una fecha (dd/mm/aaaa)')

fecha=datetime.strptime(fecha,'%d/%m/%Y')

undiamas=timedelta(days=1)

locale.setlocale(locale.LC_ALL,'es_ES.UTF-8')


while fecha.strftime("%A").capitalize !='Jueves':
    fecha=fecha+undiamas
    
sietediasmas=timedelta(days=7)

#el ultimo viernes de cada mes
mes=fecha.month
while fecha.month ==mes:
    print('Fecha '+ fecha.strftime("%d %B %Y").upper())
    fecha=fecha+sietediasmas
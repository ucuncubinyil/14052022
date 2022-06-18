from  datetime import  timedelta, date, datetime #Kısmı import
from locale import *

eski_zaman =  datetime(1993,11,20,0,0,0)
print(eski_zaman)

bu_gun =  date.today()
print(bu_gun)

bir_hafta_once =  bu_gun - timedelta(7)
print(bir_hafta_once)


dogum_gunu =  datetime(1993,11,20,0,0)
bu_gun_zamanli =  datetime.now()

fark =  bu_gun_zamanli - dogum_gunu
print(bu_gun_zamanli.year-dogum_gunu.year)

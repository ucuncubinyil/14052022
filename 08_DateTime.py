########################## DATETIME KUTUPHANESİ ###################
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,'Turkish_Turkey.1254')

zaman =  datetime.now()

# print(zaman)  # 2022-06-18 13:32:27.422448
# print(zaman.day) #18
# print(zaman.month)#6
# print(zaman.year) #2022
# print(zaman.fold)#0
#
# zaman2 =  datetime.datetime(2022,6,18)
# print(zaman2)  #2022-06-18 00:00:00
# print(zaman2.date()) #2022-06-18


# Zaman formatlama

# print("zaman değişkeninin formatlı hali:",zaman.strftime("%d_%m_%Y"))

"""
%d  : rakam ile gün
%m  : rakam ile ay
%Y  : rakam ile 4 haneli yıl
%y  : rakam ile 2 haneli yıl
%b  : yazı ile 3 haneli ay
%H  : rakam ile saat 
%M  : rakam ile dakika 
%S  : rakam ile saniye 
%a  : yazı ile 3 haneli gün
%A  : yazı ile tam gün adı
%D  : AY/GUN/YIL
"""

print(zaman.strftime("Bu gün günlerden  :  %A"))
print(zaman.strftime("%d %b %y"))
print(zaman.strftime("%A"))

# YIL-AY-GUN--Saat:Dakika:Saniye--GünAdı

zaman =zaman.strftime("%Y-%m-%d--%H:%M:%S--%A")
print(zaman)

zList = zaman.split("--")
tList = zList[0].split("-")
print(tList)
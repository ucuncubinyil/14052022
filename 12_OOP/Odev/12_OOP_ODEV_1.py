### ÖDEV:
# Bir Ders class'ı oluşturunuz.
# class Ders: DersAdi,DersSaati,DersOgretmeni,DersBaslamaTarihi
# class'dan bir nesne oluşturulduğunda field'lar oluşturularak içleri
# doldurulsun ve
# Dersler.txt dosyasına kayıt işlemi gerçekleştirilsin.
# Başka class başka bir dosyada tutulsun.
#

#Birinci yöntem
# import Ders
#
# ders = Ders.Ders()
# ders.ders_kaydet()

# 2. yöntem
from  Ders import Ders
ders =  Ders("Python", "72", "Mehmet Nuri ÖZTÜRK", "14.05.2022")
ders.ders_kaydet()
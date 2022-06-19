#1. sayıListesi.txt içindeki sayıların çift
# olanlarının karelerini,tek olanların 3.kuvvetlerini
# tutan kareListesi.txt dosya yazdırınız.

dosya_yolu = "C:\\MEHMET\\2022-06-19\\sayıListesi.txt"
dosya =  open(dosya_yolu, mode="r+")

sayiListesi =  dosya.readlines()
dosya.close()

kareListesi =  list()
sayiListesi_yeni = list()

for i in sayiListesi:
    sayiListesi_yeni.append(int(i.rstrip("\n")))

for i in sayiListesi_yeni:
    if int(i) % 2 == 0:
        kareListesi.append(int(i)**2)
    else:
        kareListesi.append(int(i)**3)

yeni_dosya_yolu =  "C:\\MEHMET\\2022-06-19\\kareListesi.txt"

dosya = open(yeni_dosya_yolu, mode="a+")

for i in kareListesi:
    dosya.write(f"{i}\n")

dosya.close()



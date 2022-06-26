from  Insan import *


# a =  Insan()
#
# a.ad =  input("Ad:")
# a.soyad = input("Soyad")
#
# a.konusma()
#
# Insan.konus(a)

liste =  list()
#
# for i in range(3):
# 	a = Insan()
# 	a.ad =  input("Ad")
# 	a.soyad =  input("Soyad")
# 	liste.append(a)
#
# Insan.yazdir(liste)


while True:
	a = Insan( )
	a.ad =  input("Ad")
	a.soyad =  input("Soyad")
	liste.append(a)
	cevap = input("Devam etmek ister misin?(E/H").upper()
	if cevap == "H":
		break

Insan.kaydet(liste)
Insan.yazdir(liste)
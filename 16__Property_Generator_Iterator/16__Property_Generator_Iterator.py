#####################################################
#################### PROPERTY #######################
#####################################################
#
# class Personel:
#
# 	def __init__(self, parametre):
# 		self.__isim = parametre
#
# 	def getIsim( self ):
# 		return  self.__isim
#
# 	def setIsim( self,parametre ):
# 		self.__isim = parametre
#
# 	ad = property(getIsim, setIsim) # fonsiyon isimleri sırasıyla get ve set ile olmalıdır
#
# nesne =  Personel("Sevgi")
# print(nesne.ad)


## SORU: Vize ve final notunu alarak ortalama hesaplayan(Ortalama ()) univeriste isminde bir sınıf tanımlayınız.

from Universite import Universite

ogrenci = Universite()
print(ogrenci.get_vize())
ogrenci.set_vize(80)
print(ogrenci.get_vize())


ogrenci.final =  92

ogrenci.ortalama()






















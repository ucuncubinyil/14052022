# import Matematik  #Full import
# from Matematik import Topla, Cikar #Kısmi import
from Matematik import *
from  Matematik import Carp as mehmet # takma isim kullanma

#Full import ile kullanımı
# toplama =  Matematik.Topla(2,3)
# print(toplama)
#
# cikarma = Matematik.Cikar(3,2)
# print(cikarma)


# Kismi import ile kullanımı
toplama =  Topla(2,3)
print(toplama)

cikarma = Cikar(3,2)
print(cikarma)

# Takma isim ile kullanımı
carpma =  mehmet(3,3)
print(carpma)
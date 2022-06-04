# #### Tuple: Sabit Liste ###
# # Liste'den farklı olarak ekleme,
# # çıkarma işlemleri yapılamaz.
#
# sabitListe = ()  # birinci yöntem
# sabitListe2 = tuple( )  # ikinci yöntem
#
# sabitListe = (1, 1, 3, "Mehmet", "Nuri", "Öztürk")
# print( sabitListe )
# print( type( sabitListe ) )
#
# print(sabitListe[3])
# print(sabitListe.index("Öztürk"))
# print(sabitListe.count(1))
# print(len(sabitListe))
#
# del sabitListe # sabit listeyi ramden siler
#
# my_tuple=(4,2,3,[6,5])
# print(my_tuple)
# print(my_tuple[3][1])
# print( 4 in my_tuple)
# print(55 not in my_tuple)
#
# ### Set : Kume ###
# kume = set() #birinci
# kume2 = {11,22,33,44} #ikinci
# print(type(kume))
#
# # aynı değere sahip veri ikinci kez kümede barınamaz
#
# #Eleman ekleme
# kume.add("Mehmet")
# kume.add(5)
# print(kume)
#
# #eleman çıkarma
# kume.remove(5) # tavsiye edilmeyen
# print(kume)
# kume.discard(5) #tavsiye edilen
# print(len(kume))


#### Küme işlemleri

kume={11,22,33,44}
kume2={33,44,55,66,77,88,99}

# İki küme farkı
kumeFark1 = kume2 - kume
kumeFark2 = kume - kume2
print(kumeFark1)
print(kumeFark2)

kumeFark =  kume.difference(kume2)
print(kumeFark)

# Küme Kesişim
kesisim =  kume & kume2 #1. yöntem
print(kesisim)
kesisim = kume.intersection(kume2) # 2.yöntem
print(kesisim)


# Küme Birleşim
birlesim =  kume.union(kume2)
print(birlesim)
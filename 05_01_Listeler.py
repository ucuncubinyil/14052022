############### LİSTE list() #####################

# sayilar = [] # BOŞ LİSTE
# sayilar = list()

# sayilar = [ 2, 3, 4, 5 ] # n -1
#
# print(sayilar[0])
# print(sayilar[3])

#
# listem =  [1, "Ahmet", True, 12.56, 'A']
#
# # print(type(listem))
# #
# # print(listem)
# #
# # print(listem[4])
#
# #Listeye veri ekleme
# listem.append("Mehmet") # Sona elaman ekler
# print(listem)
#
# # sozcuk = [ 'M', 'e', 'h','m', 'e', 't']
# # isim =  "Mehmet"
# # print(sozcuk)
#
# listem += ["Malatya","Muş", "Van"]
# print(listem)

# Çok boyutlu liste
# liste1 = [ [ 1, ['a','b','c'], 3 ], 4, 5, 6 ]
#
# print(liste1[0][0], liste1[0][1][0], liste1[1])
# print(liste1[1])
#
# # *** Listeden veri silme ***
# # del liste1[1] #1. yöntem
#
# liste1[0][1].remove('a')
#
# print(liste1)

# *** Listede verilen index veri ekleme ***

# rakamlar = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
# # rakamlar.insert( 4, 12 ) # araya ekler
# # rakamlar[0] = 'A' # değeri değiştirir
# # print( rakamlar )
#
# print( len(rakamlar) ) # Dizinin uzuluğunu verir
# print(rakamlar.index(9)) # 9 değerine sahip elemanın index numarasını verir

# sayilar=[10,20,30,40,20,20,20]
# print(sayilar.index(20)) # ilk 20 değerine sahip olanın indexini verir
# print(sayilar.index(20,2)) # 2. indexten sonra gelen 20 değerine sahip olanı verir
# print(sayilar.index(20,0,6 ))

isimler = [ "Ali", "Özlem", "Emre", "Halil", "Tolga" ]
# print(isimler[isimler.index("Tolga")])
# print(isimler[4])

# SORU: isimler listesindeki değerleri ekrana alt alta yazdırınız.
# for x in isimler:
#     print(x)
#
# for x in range(len(isimler)):
#     # print(isimler[x])
#     print(f"isimler[{x}] \t\t---> {isimler[x]}")
#     # print("isimler[{}]  \t\t---> {}".format(x, isimler[x]))

# *** Listedeki bir değerin kaç defa eklendiğini bulma ***

# sayilar=[10,20,30,40,20,20,20]
# # print(sayilar.count(20)) # aranan değer içerde kaç defa tekrar ediyor
#
# # Listedeki en son elemanı yazırma
# print(sayilar[-1])
# print(sayilar[-2]) # eksi tersten getirme işlemi yapar
#
# # listede aranan değerlerin indis numarasını verir
# for x in range(len(sayilar)):
#     if(sayilar[x] == 20):
#         print(x)
#
# # *** Listedeki değerşeri sıralama ***
# listem = ["Istabul","Manisa","Uşak","Izmir","Canakkale","Muş",
#           "Zonguldak","Adana","Izmit"]
# print(listem)
#
# #Listeyi sıralamadan tersine çevirir
# listem.reverse()
# print(listem)
# #
# # print("Sıralı Hali")
# listem.sort() # A-Z ve 0-9 sıralaması yapar
# print(listem)
# #
# # #Listeyi tersten sıralama
# listem.sort(reverse=True) # Z-A ve 9-0 sıralaması yapar
# print(listem)

#### Listeden değerleri dışarı atma
#
# sayilar = [ 1, 2, 3, 4, 5 ]
# print( sayilar )
#
# sayilar.pop( )  # varsayılan son elemanı siler
# print( sayilar )
#
# sayilar.pop( 2 )  # 2.indise sahip olanı siler
# print( sayilar )
#
# ##### bir değerin listede var olup olmadığı kontrol etme
#
# if 1 in sayilar:
#     print( "VAR" )
#
# listem = [ "Istabul", "Manisa", "Uşak", "Izmir", "Canakkale", "Muş",
#            "Zonguldak", "Adana", "Izmit" ]
#
# if "Manisa" in listem:
#     print("VAR")

## 2 listeyi birleştirme
#
# list1 = [ 1, 2, 3 ]
# list2 = [ 4, 5, 6 ]
# listem = list1+list2
# print(listem)
# print(listem[2])
#
# print(max(listem)) #listem listesindeki en büyük değeri verir
# print(min(listem))#listem listesindeki en küçük değeri verir
# print(sum(listem)) #listem listesindeki değerlerin toplamını değeri verir
#
# listem = list()
# for i in range(11):
#     listem.append(i)
# print(listem)
#
# # *** Tek satırda for yazma işlemi ***
# rakamlar=[i for i in range(1,10,2)]
# print(rakamlar)
# print(type(rakamlar))


# SORU 10 ile 100 arasındaki çift sayıları bir listeye atın.
# ciftler = list()
# for i in range( 10, 101, 2 ):
#     ciftler.append( i )
# print( ciftler )
#
# ciftler = [i for i in range(10,101,2)]
# print(ciftler)
#
#
# list1 = [ 10, 11, 12, 13 ]
# list2 = list( )
#
# list2 = list1.copy( )  # list1 in içeriğini list2 ye kopyala
# print( list2 )
#
# list2 = list1  # list1 in bellekteki adresini list2 nin bellek adresine taşı
# list1.append( 96 )
# print(list1)


### ALIŞTIRMALAR ###
# SORU: Kullanicidan 10 adet sayı alıp listeye atın
# ve sonrasında listenin aritmatik ortalamasını bulun.

# liste = list()
# for i in range(10):
#     sayi = int(input(f"{i+1} . sayiyi giriniz:\t"))
#     liste.append(sayi)
#
# print(sum(liste)/len(liste))

# 1. 1-100 arasında 20 adet sayı üretip listeye atın. #random kullanarak
#
# import random
#
# sayilar = list()
# for i in range(20):
#     sayi = random.randint(1,100)
#     sayilar.append(sayi)
#
# sayilar.sort()
# print(sayilar)

# 2. Sonra kullanıcıdan 3 tahmin hakkı verip
# listeden 1 sayıyı tahmnin etmesini isteyin.

sayilar = [ 1, 2, 3 ]
for i in range( 3 ):
    tahmin = int( input( "Tahmininizi Giriniz : " ) )
    if(tahmin in sayilar):
        print("Tebrikler")
        break
    else:
        print("Tekrar deneyin")

hak = 3

while hak > 0:
    hak -= 1
    tahmin = int( input( "Tahmininizi Giriniz : " ) )
    if(tahmin in sayilar):
        print("Tebrikler")
        break
    elif hak == 0:
        print("Hakkınız bitti")
    else:
        print("Tekrar deneyin")

# SORU: 1-200 arasında 20 adet rasgele sayi üretip sayilar
# isimli bir listeye atayınız.
# NOT: Sayının listede tekrar eklenmesini engelleyiniz.
##### Zip() #####
'''
Kelimenin çevirsine baktığımızdaki anlamı yansıtır.zip fermuar anlamına gelir ve
 bu mantıkla kullanılır.
2 Listeyi birbiri indisleri üzerine birleştiriyor. Bunu yaparken eleman sayısı az olan
 listeyi baz alır.

zip(list1,list2)

zip çalıştığında list, tuple veya dict döndürür.
'''

# isim = ["Ahmet","Can","İsmail"]
# yas = [20,30,40,50,60]
#
# print(zip(isim,yas))
#
# sonuc1 = list(zip(isim,yas))
# print(sonuc1)
#
# sonuc2 = dict(zip(isim,yas))
# print(sonuc2)
#
# sonuc3 = tuple(zip(isim,yas))
# print(sonuc3)
#
# for i, j in sonuc1:
# 	print(f"{i} {j} yaşındadır")

# isim = ["Ahmet","Can","İsmail"]
# kullanici_adi =  ["adurak","cozturk","isahin"]
#
# uyelerim =  list(zip(isim,kullanici_adi))
#
# for i, k in uyelerim:
# 	print(f"{i} isimli kullanıcının nicknamesi {k} ")


##### FILTER #####
'''
sayılabilen (iterable) tipindeki değerlerin içindeki , item'ları süzme işlemi yapar ve
sadece True deger donduren sonuçları verir.
Verdiği sonucun tipi filter tipindedir.
Bunu list veya tuple çevirmemiz gereklidir. Döngülere göre hız olarak daha başarılıdır.
'''
# liste = [ 12, 32, 44, 11, 12345, 6543, 213234 ]
#
# cs = [ ]
# for i in liste:
# 	if i % 2 == 0:
# 		cs.append( i )
# print( cs )
#
# # Filtre Çözümü
#
# dd = list( filter( lambda sayi: sayi % 2 == 0, liste ) )
# print( dd )
#
# dd = list( filter( lambda sayi: sayi % 2 != 0, liste ) )
# print( dd )
#
# ## ÖRNEK
# ifade = "rakam123evethayir"
#
# #Formul : # filter(func,iter)
# rakamlar = tuple( filter( lambda x: x.isdigit( ), ifade ) )
# print( rakamlar )

liste = [ "Python Dersleri", "django", "Python", "Gazi üniversitesi" ]


# def baslik( karakter ):
# 	return karakter.istitle( )
#
#
# a = tuple( filter( baslik, liste ) )
# b = list( filter( baslik, liste ) )
# # c = dict( filter( baslik, liste ) )
# print( a )
# print( b )
# # print( c )

# liste=[6,1,8,11,-5,5,9]
#
# aralik =  list(filter(lambda  s: s<=9 and s>=5,liste)) # tercih
# aralik.sort()
# print(aralik)
#
# print(  [ x for x in liste if x <=9 and x>=5]    )

######## Zip() ven Filter() Birlikte Kullanımı #########

# kisiler = ["Ahmet","Murat","Kemal","Mustafa"]
# tarihler  = [1992,1996,1998,1993]
# uyeler = list(zip(kisiler,tarihler))
# print(uyeler)
#
# filtreli_liste =  list(filter(lambda x:1996<=x[1] <=2000, uyeler))
# print(filtreli_liste)
#


def sesli_harf_control( kelime ):
	sesli = [ 'a', 'e', 'i', 'o', 'u' ]
	if kelime in sesli:
		return True
	else:
		return False

harfler = list()
kelime =  input("Kelime gir")
print(kelime)
for i in kelime:
	harfler.append(i)
print(harfler)

filtreli = list(filter(sesli_harf_control, harfler))
print(filtreli)

liste=[12,32,44,11,12345,6543,213234]

liste =  [ x**2 if x%2==0 else x**3  for x  in liste]
print(liste)



# x=lambda a,b: a if a>b else b



################# FONKSİYONLAR #####################

# Fonksiyon Tanımlama
"""
def fonksiyonismi(varsa parametre):
    # Fonksiyonun yapacağı kod bloğu yazılır.

Fonksiyonlar çağrılmadıkları sürece işlem yapmazlar.
"""

# # Parametreli Örnek
# def printMyName( name ):
#     print( name )
#
# def printMySurname():
#     print("Öztürk")
#
#
# # Fonksiyon çağırma
# printMyName( "Mehmet Nuri" )
# printMySurname()

# # Parametreye varsayılan değer atama
# def Topla(s1=0, s2=0, isim= ""):
#     print(isim)
#     print(s1+s2)
#
#
# s1 =  int(input("Birinci sayi:"))
# s2 =  int(input("İkinci sayi:"))
# Topla(s1,s2, "Ali")
#
#
# s3 =  int(input("Üçüncü sayi:"))
# s4 =  int(input("Dördüncü sayi:"))
# Topla(s3,s4, "Mehmet")

######### ALIŞTIRMALAR ##########
# SORU: Kullanıcıdan 2 sayı 1 işlem alalım ve
# alınan sayılara verilen işlemi uygulayan ve ekrana yazdıran fonksiyonu yazınız.

#
# def DortIslem( s1=0, s2=0, islem="" ):
#     if islem == "+":
#         print( s1 + s2 )
#     elif islem == "-":
#         print( s1 - s2 )
#     elif islem == "*":
#         print( s1 * s2 )
#     elif islem == "/":
#         if s2 != 0:
#             print( s1 / s2 )
#         else:
#             print( "Hiç bir sayı sıfıra bölünemez" )
#     else:
#         print( "Girilen işlem bulunamadı" )
#
#
# while True:
#     cvp = input( "İşlem yapmak ister misiniz ? (E/H)" ).upper( )
#
#     if cvp == "E":
#         s1 = int( input( "Birinci Sayı: " ) )
#         s2 = int( input( "İkinci Sayı: " ) )
#         islem = input( "Yapılacak işlem (+,-,*,/)" )
#         DortIslem( s1, s2, islem )
#     elif cvp == "H":
#         print( "Güle güle..." )
#         break
#     else:
#         print( "Hatalı seçim !!! " )


## SORU: Kendisine gönderilen sayı adedince klavyeden girilen ismi alıp listeye atan fonksiyonu yazınız.
#
# def isim_yaz( ):
#     isim_liste = list( )
#
#     sayi = int( input( "Kaç isim alınacak" ) )
#
#     for i in range( sayi ):
#         isim = input( "İsim:" )
#         isim_liste.append( isim )
#     print( isim_liste )
#
#
# isim_yaz( )
#
#
# def isim_yaz_2( sayi=0, liste=list( ) ):
#
#     if sayi > 0:
#         for i in range( sayi ):
#             isim = input( "İsim" )
#             liste.append( isim )
#
#     print( liste )
#
#
# isimlistesi = list( )
# isim_yaz_2( 2, isimlistesi )
#
# print(isimlistesi)


## Parametre olarak aldığı listedeki tek elemanları yazdıran fonksiyonu yazınız.
#
# def yazdir(liste =list()):
#     for i in liste:
#         if str(i).isdigit() and i % 2 !=0:
#             print(i)
#
# listem = [0,1,2,3,4,5, "Abc"]
# listem2 = [0,1,2,3,4,5, "Abc"]
# listem3 = [0,1,2,3,4,5, "Abc"]
#
# yazdir(listem)
# yazdir(listem2)
# yazdir(listem3)


### Belirsiz sayıda parametre alan fonksiyon ###
#
# def topla(s1,s2):
#     print(s1+s2)


# def topla( *sayilar):
#     sonuc = 0
#     for i in sayilar:
#         sonuc += i
#     print(sonuc)
#
# topla(1,2,3,4)

# Kendisine gönderilen karakter,en,
# boy parametrelerine göre ekrana karakterden oluşan bir dikdörtgen oluşturan fonksiyonu yazınız.
"""
oooooooo
oooooooo
oooooooo
oooooooo
"""


#
# def dikdortgen_ciz(karakter="-", boy=1, en=1):
#
#     for i in range(boy):
#         print(karakter*en)
#
# # dikdortgen_ciz("*", 5,30)
#
# karakter = input("Kullanılacak karakter")
# en =  int(input("En :"))
# boy =  int(input("Boy :"))
# dikdortgen_ciz(karakter, boy, en)


## DEGER DONDUREN FONKSİYONLAR ##
# değer döndürme anahtarı 'return' komutudur.
#
# kare4 = pow( 4, 2 )
# print(kare4)
#
# def usAl(taban,us):
#     sonuc =  taban ** us
#     return  sonuc
# kup4 = usAl( 4, 3 )
# print(kup4)

## Bir müşterim dolar'ını euro'ya çevirmek
# istiyor ben dolar/euro endeksini bilmediğim için doları tl => tl euro
#
# def dolarToTL( dolar, kur ):
#     return dolar * kur
#
# def TlToEuro( tl, kur ):
#     return tl * kur
#
# ondolar_degeri =  dolarToTL(10,20)
# print(ondolar_degeri)
#
# on_euro = TlToEuro(2000, 0.056)
# print(on_euro)


# Kendisine gönderilen 4 sayının ortalamasını döndüren fonksiyonu yazınız..

# def ortalama( s1=2, s2=2, s3=2, s4=2 ):
#     ortalama = (s1 + s2 + s3 + s4) / 4
#     return ortalama
#
#
# sonuc = ortalama( 1, 2, 3, 4 )
# print( sonuc )

# Kendisine gönderilen 4 sınıfa ait notların ortalamasını
# bulup bir listeye atan ve en başarılı sınıfı yazdıran fonksiyonu yazınız.
# max
#
# def ortalama(notlar):
#     toplam = 0
#     for i in notlar:
#         toplam += i
#     return toplam/len(notlar)
#
# sinif1 = {10,22,45,30,40}
# sinif2 = {5,80,60,30,40}
# sinif3 = {45,85,70,50,40}
# sinif4 = {75,85,70,90,80}
#
# ortalamalar = list()
#
# ortalamalar.append(ortalama(sinif1))
# ortalamalar.append(ortalama(sinif2))
# ortalamalar.append(ortalama(sinif3))
# ortalamalar.append(ortalama(sinif4))


# print(ortalamalar)
# print(f"En yüksek ortalama {max(ortalamalar)}")
# print(f"En düşük ortalama {min(ortalamalar)}")


# Kendisine parametre olarak gönderilen sayının
# faktöriyelini hesaplayıp döndüren fonksiyonu yazınız.


# def faktoryel_hesapla(sayi):
#     capim = 1
#     for s in range(1, sayi+1):
#         capim *= s
#     return  capim
#
# faktoryel5 = faktoryel_hesapla(5)
# print(faktoryel5)

# Kendisine gönderilen sayının asal olup olmadığını döndüren fonksiyonu yazınız.
# Asalsa: True değilse: False
# Asal sayı :1 ve kendisi hariç hiç bir sayıya bölünemeyen sayıdır. 2 en küçük asal sayıdır. 13 7 17
#
# def asal_kontrol(sayi):
#
#     if  sayi == 1:
#         return False
#     elif sayi == 2:
#         return True
#     for i in range(2,sayi):
#         if sayi % i == 0:
#             return False
#
#     return True
#
# print(asal_kontrol(17))

### Bir fonksiyon içinde fonksiyon çağrılması

# Parametre olarak aldığı 2 sayıdan büyük olanı döndüren fonksiyon
#
# def buyuk(a,b):
#     if(a>b):
#         return a
#     elif (b>a):
#         return b
#     else:
#         return a
#
# # Parametre oalrak aldığı 3 sayıdan büyük olanı döndüren fonksiyon
# def buyuk2(x,y,z):
#     return  buyuk(x, buyuk(y,z))
#
#
# sonuc = buyuk2(1,2,3)
# print(sonuc)


### TEK SATIRDA FONKSİYON TANIMLAMA
# def kare( s ):
#     return s * s


# kare = lambda s: s * s
# print( kare( 2 ) )
#
# toplama =  lambda a,b: a+b
# print(toplama(1,2))



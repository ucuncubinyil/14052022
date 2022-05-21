# while döngüsü
# For döngü


# 1 ile 10 arasındaki sayılari yazın
#
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

"""
while(koşul):
    işlem
"""

# i = 0
# while (i < 11):
#     print( i )
#     i += 1
#     break

# while True:
#     print( "Mehmet" )
#     break
# BREAK => Bu komut döngüyü kırmaya yarar.

# 90 ile 100 arasındaki sayıları ekrana yazdırınız.

# i =  90
#
# while (i<=100):
#     print(i)
#     i +=1

# 70 ile 55 arasındaki sayılarda 3'e
# tam bölünenleri ekrana yazdırınız

# sayi = 70
#
# while(sayi >=55):
#     if sayi %3 == 0:
#         print(sayi)
#     sayi -= 1

# SORU: 7 - 77 arasındaki tüm sayıların toplamını ekrana yazdırınız.

sayi = 7
toplam = 0

# while(sayi < 78):
#     print(sayi)
#     toplam += sayi
#     sayi += 1
#
# print(toplam)

# SORU: 1'den kullanıcının girdiği sayıya kadar
# olan sayıların karesini ekrana yazdıran program.

# i =  1
# sayi =  int(input("Lütfen 1 'den büyük bir sayı giriniz"))
#
# while(i <= sayi):
#     print(i **2)
#     i +=1

# CONTINUE: Run time da continue keyword'ü
# çalışırsa program bulunduğu yerden döngüye geri döner

# sayi = 1
# while ( sayi <10):
#     if(sayi == 3):
#         continue
#     if sayi == 5:
#         break
#     print(sayi)
#
#     sayi +=1

# sayi = 1
#
# while sayi<=5:
#     if sayi==2:
#         pass
#     else:
#         print(sayi)
#     sayi+=1

# SORU: Klavyeden girilen deger 'çık' ise döngüden çıkılacak.
# değilse toplama işlemi gerçekleştirilecek.

#
# toplam =  0
# while True:
#     sayi = input("Sayi: ")
#
#     if sayi == "cik":
#         break
#     else:
#         sayi =  int(sayi)
#         toplam += sayi
#
# print("Toplam  :", toplam)
# print(f"Toplam :{toplam}")
# print("Toplam :{}".format(toplam))


# SORU: 1-100 arasındaki sayıların toplayan program. Ancak aşağıdak durumlarda sayıyı
# toplama eklemeyecek
# * Sayı 7'nin katı ise toplama eklenmesin
# * Sayı'nın 3 katının 7 fazlası 37'nın katı ise döngüden çıkılsın.
#
# sayi = 1
# toplam = 0
#
# while sayi <= 100:
#     if sayi % 7 == 0:
#         sayi += 1
#         continue
#     kat = 3 * sayi + 7
#
#     if (kat % 37 == 0):
#         print( "Kat ", kat )
#         print("SAYI:", sayi )
#         break
#
#     toplam += sayi
#     sayi += 1
#
# print("TOPLAM : ",toplam)


# SORU: Klavyeden girilen sayının faktöriyelini hesaplayan program
# Faktoriyel => 5 => 1*2*3*4*5=120

# sayi =  int(input("Lütfen faktöryeli hesaplanacak sayıyı giriniz:"))
# sonuc = 1
# sayac =  1
# while sayac <= sayi:
#
#     sonuc *= sayac
#     sayac += 1
#     print("İçerdeki sonuç :",sonuc)
#
# print("SON SONUÇ:",sonuc)

# SORU: Kullanıcıdan alınan sayının asal olup olmadığını ekran yazdırınız.
# Asal sayı 1 ve kendisinden başka hiç bir sayıya bölünmeyen sayıdır. 13

# s = int( input( "Sayı Giriniz:" ) )  # 7 # 6 # 9
# asalKontrol = True
# i = 2
#
# while i < s:
#     if s % i == 0:
#         asalKontrol = False
#         break
#     i += 1
#
# if asalKontrol:
#     print( "Sayı asal" )
# else:
#     print( "Sayı asal değil" )


#SORU:
"""
    Kullanıcıadı/Email ve şifre ile giriş sağlanacak. 3 defa giriş hakkı vardır.
        Giriş Başarılı ise ekrana "Giriş Başarılı" yazsın
        Değilse
            Kullanıcıya kayıt olmak ister misiniz? 
                Hayır ise PEKİ!!! 
                Evet Kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı alarak kayıt yapalım.
                    şifre ve şifretekrarın aynı olması 
                    
                    
"""

# isim = input( "Lütfen isminizi giriniz: " )
# yas = int( input( "Lütfen yaşınızı giriniz: " ) )
# egitim = input("Mezuniyet Durumunuzu Giriniz: ")
#
# if yas >=18:
#     if egitim == "lise" or egitim == "üniversite":
#         print(f"{isim}, ehliyet alabilir")
#     else:
#         print(f"{isim}, ehliyet alamaz")
# else:
#     print( f"{isim}, ehliyet alma yaşı tutmuyor" )


# Trafiğe çıkış tarihi alınan bir aracın servis zamanını
# aşağıdaki bilgilere göre hesaplayan python uygulamasını yapınız
#
# 1. Bakım => 1. yıl
#
# 2. Bakım => 2. yıl
#
# 3. Bakım => 3. yıl
#
# yil = int( input( "Lütfen trafiğe çıkış yılınızı giriniz :" ) )
#
# simdiki_yil = 2022
#
# fark = simdiki_yil - yil
#
# if yil == simdiki_yil:
#     print( "İlk muayene yılınız : ", simdiki_yil + 1 )
#
# elif fark == 2:
#     print( "İkinci muayene yılınız :", yil + fark )
#
# elif fark == 3:
#     print( "Üçüncü muayene yılınız :", yil + fark )
#
# else:
#     print( "Hatalı süre" )

# Girilen 3 sayıyı büyüklük olarak karşılaştıran python uygulamasını yapınız.
#
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
#
# if (a > b ) and (a > c):
#     print(f"En büyük sayı {a}")
# elif (b >c) and (b > a):
#     print("En büyük sayı", b)
# elif (c >a) and (c > b):
#     print("En büyük sayı", c)
#

# ad = input( "Adınız" )
# soyad = input( "Soyadınız" )
# tc = input( "TC niz" )
# dogum_tarihi = input( "Doğum Tarihiniz" )
# meslek =  input("Mesleğiniz")
# maas =  input("Maaşınız")
#
# bilgiler = f"""
#         Adınız          :{ad}
#         Soyadınız       :{soyad}
#         T.C.            :{tc}
#         Doğum Tarihi    :{dogum_tarihi}
#         Meslek          :{meslek}
#         Maaş            :{maas}
# """
#
# print(bilgiler)

# a = 11
# b = 10
#
# if a > b : print("a b den büyük")
#
# print("Çift sayıdır") if a%2 == 0 else print("Tek sayıdır")


# kontrol = 1
#
# if kontrol == 0:
#     print( "Hata var" )
# else:
#     pass

x = 41

if x > 10:
    print( "Sayı 10 dan büyük" )
    if x > 20:
        print( "Sayı 20 den büyük" )
        if x > 40:
            print( "Sayı 40 dan büyük" )
        else:
            print("Sayı 40 dam küçük")
    else:
        print("Sayı 20 den küçük")
else:
    print("Sayı 10 dan küçük")

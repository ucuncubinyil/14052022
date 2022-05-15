##################### AKIŞ KONTROL : IF ELIF ELSE ########################################

# sayi = 6
#
# if sayi > 6:  # 1. Koşul
#     print( "Sayi 6 'ya eşittir" )
#
# elif sayi != 6:  # 2.Koşul
#     print( "Sayı 6'dan küçüktür" )
#
# else:
#     print( "Sayi 6'ya eşittir" )

# Haftanın kaçıncı günüdeyiz? ekrana gün adını yazdıralım

# gun = int( input( "Haftanın gün numarasını giriniz" ) )
#
# if gun == 1:
#     print( "Pazartesi" )
# elif gun == 2:
#     print( "Salı" )
# elif gun == 3:
#     print( "Çarşamba" )
# elif gun == 4:
#     print( 'Perşembe' )
# elif gun == 5:
#     print( "Cuma" )
# elif gun == 6 or gun == 7:
#     print( "Haftasonu" )
# else:
#     print( "Hatalı giriş yapıldı" )


# SORU: Klavyeden girilen değer: 100'den büyükse karesini, küçükse küpünü ekrana yazdıran prog.
# FORMUL karesi =  sayi*sayi kupu = sayi*sayi*sayi
#
# sayi =  int(input("Sayıyı giriniz"))
#
# if sayi > 100:
#     print(sayi*sayi)
# elif sayi < 100:
#     print(sayi*sayi*sayi)
# else:
#     print("Hatalı ")


## MOD ALMA
# sayi = 5
# print(13%5)

# TEK ÇİFT


# Klavyeden girilen sayı çift ise: Ekrana sayı çifttir yazılacak, değilse tektir yazılacak
# sayi = sayi%2
# çift ise 4 ile çarpsın, tek ise 9 ile toplasın
#
# sayi = int( input( "Sayıyı gir" ) )
#
# if sayi % 2 == 0:
#     print( "Sayi çifttir" )
#     print( sayi * 4 )
# else:
#     print( "Sayı tektir" )
#     print( sayi + 9 )
#
# # Kullanıcıdan alınan sayının aralığını belirleyiniz
#
# sayi = int( input( "Sayıyı gir" ) )
#
# if (sayi > 0 and sayi < 11):
#     print( "Sayı 0 ile 10 arasında" )
# elif sayi > 10:
#     print( "Sayi 10'dan büyüktür" )

# Klavyeden girilen 4 sayıdan tek ve çift olanları
# ayrı ayrı toplayarak ekrana yazdırınız..


ciftlerin_toplamı = 0
teklerin_toplamı = 0

sayi1 = int( input( "1. Sayıyı gir" ) )

if sayi1 % 2 == 0:
    ciftlerin_toplamı += sayi1
else:
    teklerin_toplamı += sayi1

sayi2 = int( input( "2. Sayıyı gir" ) )

if sayi2 % 2 == 0:
    ciftlerin_toplamı += sayi2
else:
    teklerin_toplamı += sayi2

sayi3 = int( input( "3. Sayıyı gir" ) )

if sayi3 % 2 == 0:
    ciftlerin_toplamı += sayi3
else:
    teklerin_toplamı += sayi3

sayi4 = int( input( "4. Sayıyı gir" ) )

if sayi4 % 2 == 0:
    ciftlerin_toplamı += sayi4
else:
    teklerin_toplamı += sayi4

print( "Çift sayıların toplamı : ", ciftlerin_toplamı )
print( "Tek sayıların toplamı : ", teklerin_toplamı )


## Kullanıcıdan 1.vize ve 2.vize  final not girilmesi istensin not aralığı 0 ile 100 arasında olmalıdır.
## vize ve finalin ortalaması alınsın.
## 0-44 : Kaldınız
## 45-69: Geçtiniz
## 70-84: İyi
## 85-100: Pekiyi


# ÖDEV: Kullanıcıdan isim,yaş,maaşve çocuk sayısı alalım
"""
    Eğer kullanıcının yaşı 45'in altındaysa;
        çocuk sayısına bakılacak ve çocuk sayısı 3^ten az ise çocuk başına 250₺, değilse çocuk başına 200₺ maaşa eklenecek
    Eğer kullanıcının yaşı 45 ve üzerinde ise:
        çocuk başına para verilmeyecek direk 500₺ maaşa eklenecek.

    Ekrana "Nesrin Yılmaz Maaşınız: 4000₺" yazılacak. 
"""

# ÖDEV: Kullanıcı Gİriş Paneli Tasarlayınız.
"""
    Kullanıcıadı/Email ve şifre ile giriş sağlanacak
        Giriş Başarılı ise ekrana "Giriş Başarılı" yazsın
        Değilse
            Kullanıcıya kayıt olmak ister misiniz? 
                Hayır ise PEKİ!!! 
                Evet Kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı alarak kayıt yapalım.
                    şifre ve şifretekrarın aynı olması 
"""
# Aritmatik Operatörler

"""
    +,-,* :toplama,çıkarma,çarpma
    /     :ondalıklı bölme (10/4=2.5)
    //    :bölümün tamsayı kısmını verir (10//4=2)
    %     : Moda alma
"""

kontrol = 15
b = 654

# print( kontrol + b )
# print( kontrol - b )
# print( kontrol / b )
# print( kontrol // b )
# print( kontrol % b )

# Tek mi çiftmi
# print(20%2)

# Karşılaştırma Operatörleri

# 1.  Eşit mi ?  ==
# 2. Eşit değil mi ? !=
# 3.  > Büyüktür
# 4. < Küçüktür
# 5. >=  Büyük Eşit (Büyük veya Eşit)
# 6. <= Küçük Eşit (Küçük veya Eşit)
#
# print( kontrol == b )
# print( kontrol != b )
# print( b > kontrol )
# print( kontrol < b )
# print( b >= kontrol )
# print( kontrol <= b )

# Mantıksal Operatörler AND (VE)
# 00 = 0
# 01 = 0
# 10 = 0
# 11 = 1
#
# kullanici_adi = "mehmet"
# sifre = "123"
#
# kontrol = kullanici_adi == "mehmet" and sifre == "123"
# print( kontrol )

# MANTIKSAL VEYA (OR) (VEYA)
# 00 = 0
# 01 = 1
# 10 = 1
# 11 = 1

# sayi = 36
#
# # kontrol = sayi > 85 or sayi > 35
# # print( kontrol )
#
# kontrol = not sayi > 2 or sayi > 35 and sayi == 36 # not  keyword'u önüne gelen ifadeyi tersine çevirir
# print( kontrol )
#
# sayi = 21
# sayi = not sayi
# print(sayi)
#
# sayi =  25
# sayi2 = 25
#
# kontrol =  sayi is sayi2
# kontrol =  sayi == sayi2
# print(kontrol)

## SORU: Kullanıcıdan alınan 1.sayının kullanıcının girdiği
# 2. sayıya kuvvetini hesaplayarak ekrana yazdıran prog.
# sayi1**sayi2

taban = int(input("Tabanı girin:"))
us = int(input("Üssü girin:"))

print(taban, " sayısının ", us, ".kuvveti : ", (taban**us))


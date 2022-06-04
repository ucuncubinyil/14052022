##### ALIŞTIRMALAR ########

from random import randint

#
# # SORU:
# # 1 1-15 arasında 5'er adet sayı üretip 2 farklı kümeye kaydediniz.
# # Daha Sonra iki kümeyi ekrana yazdırınız.
#
# kume1 = set( )
# kume2 = set()
# #
# # for i in range(5):
# #
# #     while True:
# #         sayi = randint(1,15)
# #         if sayi not in kume1  and  sayi not  in kume2:
# #             kume1.add(sayi)
# #             break
# #         else:
# #             print("Bu sayı 1. kümede var ", sayi)
# #
# #     while True:
# #         sayi = randint( 1, 15 )
# #         if sayi not in kume2:
# #             kume2.add( sayi )
# #             break
# #         else:
# #             print( "Bu sayı 2. kümede var ", sayi )
# #
# #
# # print(kume1)
# # print(kume2)
#
# while len(kume1) <5:
#     kume1.add(randint(1,15))
#
#
# while len(kume2) <5:
#     kume2.add(randint(1,15))
#
# print(kume1)
# print(kume2)

# SORU: 1-100 arasında rastgele 10 sayı üretip bir listeye atayın.
# Daha sonra bu listedeki en büyük ve en küçük elemanları hazır fonksiyon kullanmadan bulun.
# (liste ile çözün-max(),min(),sort(),reverse())

liste = list( )

for i in range( 10 ):
    liste.append( randint( 1, 100 ) )

# while len(liste) < 10:
#     liste.append( randint( 1, 100 ) )


kucuk = 100
buyuk = 0
print( liste )

for eleman in liste:
    if eleman > buyuk:
        buyuk = eleman

    if eleman < kucuk:
        kucuk = eleman

print( "Küçük eleman ", kucuk )
print( "Büyük eleman ", buyuk )

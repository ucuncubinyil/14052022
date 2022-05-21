##### FOR DONGUSU #####

# i=1
# while(i<=10):
#     print(i)
#     i+=1

## Aralık tanımlama

# range  aralık tanımlar varsayılan olarak  0 dan başlar
#
# print(range(5)) # 0,1,2,3,4,5
# print(range(1,5)) # 1,2,3,4,5
# print(range(1,9,3)) #1,4,7

"""
for i in range(aralik):
    çalıştırılacak kod
"""

# for i in range(1,6):
#     print(i)
#
# for sayi in range( 1, 9, 3 ):
#     print( sayi )

# ILCE =  "kadıköy" # K + A+ D+
#
# for karakter in ILCE:
#     print(karakter)

# 1 ile 40 arasındaki sayıları toplayan programı yazınız. 40 dahil.

# toplam = 0
#
# for sayi in range(1,41):
#     toplam += sayi
#
# print(toplam)


## SORU 20-40 arasındaki çift ve tek
# sayıların toplamlarını ayrı ayrı ekrana yazdırınız.

# cift_toplam = 0
# tek_toplam = 0
#
# for sayi in range( 20, 41 ):
#
#     if sayi % 2 == 0:
#         cift_toplam += sayi
#     else:
#         tek_toplam += sayi
#
# print( f"Tek sayıların toplamı {tek_toplam}" )
# print( f"Çift sayıların toplamı {cift_toplam}" )

# print("Ahmet"*2)

#
# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     print("*"*i)


"""
*****************
*               *
*               *
*               *
*               *
*****************

"""

# for i in range(1,7):
#     if(i ==1 or i ==6):
#         print("*"*15)
#     else:
#         print("*",(" "*13),"*",sep="")


"""
            *
           ***
          *****
         *******
        *********
"""

#
# sayac =  1
# for satir in range(1,6):
#     print(" "*(5-satir), end="")
#     print("*"*sayac)
#     sayac +=2


# range(0,10)
#range (10,0,-1)
#
# for i in range(10,0,-1):
#     print(i)

## ÇARPIM TABLOSU
"""
1 x 1 = 1 1 x 2 = 2 1 x 3 =3
2 x 1 = 2 ....
3 x 1 = 3 """

for i in range(1,10):

    for j in range(1,10):
        print(i,"x", j,"=", (i*j), end="      " )

    print()

#SORU: Kullanıcıdan personel sayısını alınız.
# Personelin kaç çocuğu olduğunu isteyelim.
# Program her çocuk için "Çocuğunuz adına 1 ağaç dikilmiştir" yazsın
# Toplam dikilen ağaç sayısınıda ekrana yazdıralım.
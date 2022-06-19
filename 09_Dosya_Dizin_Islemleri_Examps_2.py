import datetime
import os
import random

zaman =  datetime.date.today()
klasor_adi = str(zaman)
dosyaYolu =  "C:\\MEHMET\\"+ klasor_adi

if ( os.path.exists("C:\\MEHMET") == False):
    os.mkdir("C:\\MEHMET")

if (os.path.exists(dosyaYolu) == False):
    os.mkdir(dosyaYolu)
os.chdir(dosyaYolu)

### SORU: 1 - 10 sayıların karelerini kare.txt isimli bir dosyaya aşağıdaki formatla yazdırınız.

"""
    1 sayısının karesi: 1
    2 sayısının karesi: 4
    3 sayısının karesi: 9
    ....
    ....
"""

# dosya = open(dosyaYolu+"\\kare.txt", "a+")
#
# for i in range(1,11):
#
#     dosya.write(f"{i} sayısının karesi: {i**2} \n")
#
# dosya.close()


# SORU: 1-100 arası üretilen
# 10 adet sayıyı Rastgele.txt isimli bir
# dosyaya aşağıdaki formatta yazdıran program.
#
# """
#     Zaman                   OlaySırası          RastgeleSayı
#     20.01.2020 19:16:45         1                       98
#     20.01.2020 19:16:46         2                       15
#     20.01.2020 19:16:47         3                       45
#     20.01.2020 19:16:48         4                       87
# """
#
# dosya =  open(dosyaYolu+"\\Rastgele.txt", "a+")
#
# dosya.write("""
#         ZAMAN                           OLAY SIRASI                 RASTGELE SAYI
#         -----                           -----------                 -------------
# """)
#
# for i in range(1,11):
#     sayi =  random.randint(1,100)
#     zaman =  datetime.datetime.now()
#     dosya.write(f"""
#         {str(zaman)}                     {str(i)}                    {str(sayi)}
#     """)
# dosya.close()


# SORU: Kullanıcının girdiği küçük sayıdan büyük sayıya kadar olan sayıları txt
# dosyasında alt alta yazınız.

dosya =  open(dosyaYolu+"\\sayilar.txt", "a+")

kucuk_sayi =  int(input("Lütfen küçük sayıyı girin"))
buyuk_sayi =  int(input("Lütfen büyük sayıyı girin"))

# a,b,c = 1,2,3

if kucuk_sayi > buyuk_sayi:
    kucuk_sayi,buyuk_sayi =  buyuk_sayi, kucuk_sayi

for i in range(kucuk_sayi,buyuk_sayi+1):
    dosya.write(str(i) + "\n")

dosya.close()


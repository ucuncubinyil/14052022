### DOSYA OKUMA İŞLEMLERİ ###
import os

# dosya_yolu = "C:\MEHMET\\2022-06-19\\mehmet.txt"
#
# dosya =  open(dosya_yolu, mode="r+", encoding='utf-8')
#
# # print(dosya.readline()) #1. satırı okur
# # print(dosya.readline()) #2. satırı okur
# # print(dosya.readline()) #3. satırı okur
# # print(dosya.readline()) #4. satırı okur
# # print(dosya.readline()) #5. satırı okur
# # print(dosya.readline()) #5. satırı okur
#
# metin =  dosya.readlines()
# print(type(metin))
# dosya.write("\nTÜRKÇE LASTİK GİBİ")
# dosya.close()
#
# for i in metin:
#     print(i)

#
# dosya_yolu = "C:\\MEHMET\\2022-06-19\\personel.txt"
# dosya =  open(dosya_yolu, mode="r+", encoding="utf-8")
#
# metin =  dosya.readlines() # len(metin) dizinin boyutunu verir
#
# yeni_liste =  list()
#
# yeni_liste.append("AHMET KAYA")
# yeni_liste.append("ZEKİ MÜREN")
# yeni_liste.append("TARKAN")
# yeni_liste.append("ZERRİN ÖZER")
#
# for i in yeni_liste:
#     dosya.write(f"\n{str(i)}")
#
# dosya.close()



### DOSYA RENAME ###

#Dolaylı yol
import os
# from shutil import copy
#
dosya_yolu = "C:\\MEHMET\\2022-06-19\\personel.txt"
# copy(dosya_yolu, "C:\\MEHMET\\2022-06-19\\personel_yeni.txt")
# os.remove(dosya_yolu)


#Kısa Yol
os.rename("C:\\MEHMET\\2022-06-19\\personel_yeni.txt", dosya_yolu)





















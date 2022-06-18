# import os # işletim sistemi ile alakalı işlemleri yapar
# import platform

# print(os.getcwd())
#
# os.chdir("C:\\") # farklı klasöre geçmek
# print(os.getcwd())
#
# print(os.listdir())
#
# # os.mkdir(os.getcwd() +"MEHMET")  # C:\MEHMET
# print(platform.system())
# import os
# from os import *
#
# print("Hangi klasördeyiz : ", os.getcwd())
#
# klasor_varmi =  path.exists(os.getcwd()+"\\test")
#
# if klasor_varmi == False:
#     mkdir(os.getcwd() +"\\test")

"""
open()      => Dosya açma komutu
system()    => Kullanırken çok dikkat edeceğimiz bir methoddur.
getcwd()    => Sistemin şuan işlem yaptığı dizin döndürülür.
chdir()     => Farklı bir dizine geçmemizi sağlar.
listdir()   => Bulunduğumuz dizinde mevcut dosyaları getirir.
mkdir()     => Bulunduğumuz dizinde yeni klasör açar.
rmdir()     => İçi boş olan bir klasörü siler.
rename()    => İsim değiştirir
path()      => Bir dosya veya klasörün var olup olmadığını
                kontrol etmek istediğimizde path.exists()
                komutu kullanırız.
"""

#SORU1: C:\TEST\YIL-AY-GUN ismi ile bir klasör oluşturunuz
from os import *
import datetime
import time
zaman =  datetime.date.today()
print(zaman)
klasor_adi = str(zaman)
dosyaYolu =  "C:\\MEHMET\\"+ klasor_adi

if ( path.exists("C:\\MEHMET") == False):
    mkdir("C:\\MEHMET")

if (path.exists(dosyaYolu) == False):
    mkdir(dosyaYolu)
    print(klasor_adi + " isimli klasör oluşturuldu")
    print("Oluşturma Tarihi:", path.getctime(dosyaYolu)) #klasör oluşturma tarihi

    gunRaw = time.ctime(path.getctime(dosyaYolu)) # Formatlamak için aldık
    print(gunRaw)
    parsed = time.strptime(gunRaw)
    print(parsed)
    formatli = time.strftime("%Y-%m-%d %H:%M:%S",parsed)
    print(formatli)




















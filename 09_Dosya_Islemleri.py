#### DOSYA İŞLEMLERİ ####
"""
Dosya Yetki Modları
w:  sadece yazma yetkisi ile açar. (dosya var ise siler yeniden oluşturur.yoksa oluşturur.)
r:  sadece okuma yetkisi ile açar.
a:  sona ekleme yetkisi ile açar. (dosya yoksa oluşturur.)
x:  yazma yetkisi ile açar. (yoksa oluşturur. varsa hata verir.)

w+: yazma + okuma yetkisi ile açar. (dosya var ise siler yeniden oluşturur.yoksa oluşturur.)
r+  okuma + yazma yetkisi ile açar.
a+  ekleme + okuma yetkisi ile açar. (dosya yoksa oluşturur.)
"""

import datetime
import os
import time
zaman =  datetime.date.today()
print(zaman)
klasor_adi = str(zaman)
dosyaYolu =  "C:\\MEHMET\\"+ klasor_adi

if ( os.path.exists("C:\\MEHMET") == False):
    os.mkdir("C:\\MEHMET")

if (os.path.exists(dosyaYolu) == False):
    os.mkdir(dosyaYolu)
    print(klasor_adi + " isimli klasör oluşturuldu")
    print("Oluşturma Tarihi:", os.path.getctime(dosyaYolu)) #klasör oluşturma tarihi

    gunRaw = time.ctime(os.path.getctime(dosyaYolu)) # Formatlamak için aldık
    print(gunRaw)
    parsed = time.strptime(gunRaw)
    print(parsed)
    formatli = time.strftime("%Y-%m-%d %H:%M:%S",parsed)
    print(formatli)


os.chdir(dosyaYolu)

if (os.path.exists(dosyaYolu)):
    print(os.getcwd())
    dosya = open(dosyaYolu+"\\mehmet.txt", "a+")

    for i in range(1,11):
        dosya.write(str(i)+"\t")

    dosya.close()




####################  HAZIR STRING FONKSİYONLAR  ########################

"""
capitalize() İlk karakteri büyük harfe çevirir.
count()      Bir dizide belirtilen değerin kaç defa gerçekleştiğini döndürür.
endswith()   Dize belirtilen değer ile bitmiş ise true döndürür.
find()       Dizede belirli bir değeri arar ve bulunduğu yeri döndürür.
format()     bir dizede belirtilen değerleri formatlar.
index()
isalpha()    Dizedeki bütün karakterleri alfabede ise True döndürür.
isdecimal()  Dizedeki bütün karakterler ondalıksa True döndürür.
isdigit()
islower()
isupper()
isnumeric()
isspace()    Dizede boşluk varsa True döndürür.
ljust()      Dizeyi sola dayalı bir sürüm döndürür.
rjust()
lstrip()     Dizenin sol tirm versiyonunu döndürür.
rstriip()
strip()
replace()
split()      Dizeyi belirtilen ayrıcıya böler.
isalnum()    Dizedeki değerler Alfabe ve numara olması durumunda True döner
"""

metin =  " mehmet nuri "
print(metin.lstrip())
print(metin.rstrip())
print(metin.capitalize())

# metin parçalama

kelime = "bu.gun.hava.cok.sıcak"

kelimeler =  kelime.split(".")
kelimeler2 =  kelime.split(".", 3)

print(kelimeler)
print(kelimeler2)

metin =  "MehmetNuri445566"

if metin.isalpha():
    print("Metin alfabetik ve numara içeriyor")
else:
    print("Normal")
# int ve float örneği
# bir öğrencinin iki notunun ortalamasını ekrana yazdıran program.

# birinci_not = 51
# iki_not = 53
# sonuc = (birinci_not+iki_not)/2
#
#
# # + - / *
#
# print("Sonuc :", sonuc)
# print(sonuc)

# ad = "Mehmet Nuri"
# soyad = "ÖZTÜRK"
# print(ad+" "+soyad)

# Çoklu değişken tanımlama

# c1 = c2 = c3 = 12
# print(c2)
# print(c3)
#
# c2 = True
# print(c2)
# print(c3)

# Çoklu değişkene çoklu değer atama
# d1, d2, d3, d4 = 12, 654, 12, True
# print(d1, d2, d3, d4)

# yas, ad_soyad = 28, "Mehmet Nuri  ÖZTÜRK"
#
# print("Yaş", yas)
# print("Soyad", ad_soyad)

### Değerler karşılıklı olarak değişsin

# x1 = 5
# x2 = 7
#
# print("Önceki Hali")
# print("X1", x1)
# print("X2", x2)
#
# x1, x2 = x2, x1
#
#
# print("Sonraki Hali")
# print("X1", x1)
# print("X2", x2)

##### KAÇIŞ KARAKTERLERİ #####

# \n new line (yeni satır)
# \t tab 4 karakter boşluk bırakır TAB tuşunun yaptığı işi yapar
# \ sonraki karakteri manüpile eder
# \a Zil çalar
# \r Satır başına gider
# \v Düşey sekmeye getirir
# \b backscape tuşunun işini yapar

my_custom_value = "Merhaba Dünya"
print(my_custom_value)

my_custom_value = "Merhaba \nDünya"
print(my_custom_value)

my_custom_value = "Merhaba \tDünya"
print(my_custom_value)

my_custom_value = """
    Ahmet bu gün  "Ben hastayım !" dedi
"""

print(my_custom_value)

my_custom_value = "Ahmet bu gün  \"Ben hastayım!\" dedi"
print(my_custom_value)

my_custom_value = "Merhaba \a"
print(my_custom_value)

my_custom_value = "Merhaba \rDünya"
print(my_custom_value)

my_custom_value = "Merhaba \vDünya"
print(my_custom_value)

my_custom_value = "Merhaba Dünya\b"
print(my_custom_value)

print("Kaçış dizileri: \\, \\n, \\t, \\a, \\\, r")

print("Merhaba", "Ben", "Python", sep=" ")

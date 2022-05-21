import random as kutuphane


print(kutuphane.random()) # 0 -1 arasında rastgele bir sayı verir
print(kutuphane.randint(0,100)) # 0  ile 100 arasında rastgele bir sayı verir
print(kutuphane.uniform(0,100))# 0  ile 100 arasında noktalı bir sayı verir
print(kutuphane.randrange(1,100))  #1 - 100 aralığında tam sayı üretir. min ve max değerleri dahil değildir..
print(kutuphane.randrange(1,100,3)) # 1-100 arasında 3'e bölündüğünde 1 kalan sayı verir.

print( kutuphane.uniform( 100000.0000, 999999.9999 ) )
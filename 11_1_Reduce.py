##### Reduce() ######

"""
Reduce fonksiyonu,döngüye sokabileceğiniz herhangi bir veri tipi içinde, veri tpinin içindeki
 bütün elemanları azaltarak dolaşan ve karşılaştırma yapmaya imkan tanıyan bir yapıdır.
"""

from functools import reduce
#
# numbers = [ 11, 3, 44, 23, 96, 101, 65 ]
#
# def findMax(a,b):
# 	if a >b:
# 		return a
# 	else:
# 		return b
#
#
# # for i in range(len(numbers)-1):
# #     print(findMax(numbers[i],numbers[i+1]))
#
# print( reduce( findMax, numbers ) )

# def faktoryel(s1, s2):
# 	return s1*s2
#
# sayilar = range(1,11)
# print(sayilar)
#
#
#
# liste = [1,2,3,4,5,6,7,8,9,10,11]
# print(reduce(faktoryel, liste))
#
# print(reduce(lambda x,y: x*y, liste)) # tercih
#
#
# print(reduce(lambda x,y: x*y, range(1,101)))


metinler=  ["Mehmet Nuri  Öztürk", "Python", "Dersi","Anlatıyor"]
# print(" ".join(metinler)) # tercih
#
# def birlestir(s1,s2):
# 	return  str(s1) +" "+ str(s2)
#
#
# print(reduce(birlestir, metinler))
#
# print([x*x for x in range(1,10) if x >5])
#
# print(list(map(lambda x: x*x, filter(lambda x:x>5, range(1,10)))))

import  timeit

print(timeit.timeit("[x*x for x in range(1,10) if x >5]"))

print(timeit.timeit("list(map(lambda x: x*x, filter(lambda x:x>5, range(1,10))))"))
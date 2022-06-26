###### Map() ######
'''
iterable(sayılabilen) tipteki değişkenin içindeki elemanlara matematiksel işlem yapmaya yarar.
Sorgu işlemi yapılamaz, yapılırsa True-False değer döner.

map(func,iter)
'''
#
# liste = [ 2, 3, 4 ]
#
#
# def kare_al( sayi ):
# 	return sayi ** 2
#
#
# kare_list = list( )
#
# for i in liste:
# 	kare_list.append( kare_al( i ) )
#
# print( kare_list )
#
# sonuc = list( map( kare_al, liste ) )
# print( sonuc )
#
# listem = list( map( lambda x: x ** 2, liste ) )  # tercih
# print( listem )
#
# dd = [ 1, 32, True, "Mehmet", 56, 64, 78, 65 ]
#
# ints = list( filter( lambda item: type( item ) == int or type( item ) == float, dd ) )
# print( ints )
#
# y = list( map( lambda sayi: sayi / 2, ints ) )
# print( y )
#
#
# sayilar =  list(map(lambda s:s/2, (filter( lambda item: type( item ) == int or type( item ) == float, dd ))))
# print(sayilar)

# list_1 = [ "A", "B", "C" ]
# list_2 = [ 1, 2, 3 ]
#
# list_merged = list( map( lambda x, y: (x + "_" + str( y )), list_1, list_2 ) )
# print( list_merged )

# Map içinde sözlük ve lambda kullanımı

dict_1 = {
		1: 'A',
		2: 'B',
		3: 'C',
		4: 'd'
		}
print(dict_1.items())

dict_2 =  dict( map(lambda  x: (x[0],x[1]+ '_'+ str(x[0])), dict_1.items() ))
print(dict_2)
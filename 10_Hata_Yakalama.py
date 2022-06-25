#### TRY CATCH - TRY EXCEPT ####

"""
try:
	# hata vermesi olası kodların barındıgı alan
except:
	#hata mesajı, hata varsa ne yapılacak ise buraya yazılır
"""
#
# try:
# 	sayi = int(input("Sayı gir:"))
# except:
# 	print("Sayi yalnızca rakam olmalıdır")

# while True:
# 	try:
# 		dosya = open("C:\\TEST\\try.txt", "w")
# 		sayi = int(input("Sayi gir"))
# 		dosya.write(str(sayi))
# 		break
# 	except ValueError:
# 		print("Girilen değer rakam olmalı")
# 	except FileNotFoundError:
# 		print("Dosya Yok !")
# 	finally:
# 		dosya.close()
# 		print("Sistem hata versede vermesede burası çalışacak")

# try:
# 	sonuc =  12/0
# except :
# 	print("Hiç bir sayı sıfıra bölünemez")

# while True:
# 	try:
# 		sayi = int( input( "Sayı gir" ) )
# 		break
# 	except ValueError:
# 		print("Sadece rakam girilebilir")
# 	except MemoryError:
# 		print("Bilgisayarınızda yeterli ram kalmadı")
# 	except ImportError:
# 		print("Modül dahil edilemedi")
# 	except OverflowError:
# 		print("Değişkenin kapasitesi aşıldı")
# 	except IndexError:
# 		print("Kolleksiyon index uzunluğunun dışında bir deper girildi")
# 	except ZeroDivisionError:
# 		print("Hiç bir sayı sıfıra bölünemez")
# 	except FileNotFoundError:
# 		print("Dosya bulunamadı")
# 	except FileExistsError:
# 		print("Dosya zaten var")
# 	except ModuleNotFoundError:
# 		print("Modül bulunamadı")
# 	except SyntaxError:
# 		print("Programda yazılımsal hata var")
# 	except:
# 		print("Hata yakalandı")

# try:
# 	a =  2
# 	b = 55+"a"
# except TypeError:
# 	print("Yazımsal hata var")

###### HATA FIRLATMA:TANIMLAMA raise() #######


# not1 =  int(input("Vize notunu girin"))
# try:
# 	if not1 < 0 or not1 > 100:
# 		raise OverflowError()
# except OverflowError:
# 	print("Vize notu 0-100 arasında olmalııdr" )

### ASSERT => iddaa edilen
# try:
# 	eposta = input("Eposta")
# 	assert eposta == "info@mehmetnuri.net" # eposta  info@mehmetnu ... değil ise AssertionError
# except AssertionError:
# 	print("E-Posta doğrulanamadı")


####### ALIŞTIRMALAR #########
# Kullancıdan 2 sayı 1'de işlem alıp önceden tanımladığınız methodlara alınan değerleri göndereceğiz.
# işlem topla,çıkar,çarp ve böl'den birisi değilse assert fırlatsın,
# Kullanıcıdan veri alınırken ValueError verdiğinde tekrar veri istensin
# ZeroDivisionError için tekrar veri istenmesin!

# def topla (s1,s2):
# 	print(s1+s2)
#
# def IslemYap():
# 	s1 = int(input("S1:"))
# 	s2 = int(input("S2:"))
# 	islem =  input("Işlem(topla,çıkar,çarp,böl):")
# 	assert islem == "topla" or islem == "cikar" or islem == "bol" or islem == "carp"
#
# 	if islem == "topla":
# 		topla(s1,s2)
# 	elif islem == "cikar":
# 		print(s1-s2)
# 	elif islem == "carp":
# 		print(s1*s2)
# 	elif islem == "bol":
# 		print(s1/s2)
#
# try:
# 	IslemYap()
# except ValueError:
# 	print("Sadece rakamlar kabul ediliyor")
# except ZeroDivisionError:
# 	print("Hiç bir sayı sıfıra bölünemez")
# except AssertionError:
# 	print("Hatalı seçim")
#

try:
	sayi = int(input("sss"))
except Exception as e:
	print(e.__class__.__name__)

	
	
	
	
	
	
	
	
	
	
	
	
	


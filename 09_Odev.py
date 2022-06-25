### ÖDEV: Bir Şirket Otomasyonu tasarlayınız. İnsan Kaynakları,
# Muhasebe ve Bilgi İşlem birimleri olsun.
# Her personeli kendi birim adıyla oluşturulan txt dosyasına isim
# soyisim doğumyılı başlıkları altında personel bilgileri tutulsun.
# Personel ekleme, Güncelleme, Silme, Birime göre personel listeleme
# işlemlerini yapan bir menü tasarlayarak işlemler bu  menü üzerinden ilerlesin.

import Fonksiyonlar

while True:
	print( "*************************************XXX YAZILIMI XXX*************************************" )
	secim = int( input( """
				1- Personel Ekleme
				2- Personel Güncelleme
				3- Personel Silme
				4- Personel Listeleme
				5- Çıkış"""))
	
	if secim == 5:
		break
	elif secim == 1:
		while True:
			print( "*******PERSONEL EKLEME*******" )
			bolum = int( input( """
			1- İnsan Kaynakları
			2- Bilgi İşlem
			3- Muhasebe
			4- Çıkış
			"""))
			
			if bolum == 4:
				break
			elif bolum == 1:
				Fonksiyonlar.personel_ekle( "InsanKaynaklari" )
			elif bolum == 2:
				Fonksiyonlar.personel_ekle( "BilgiIslem" )
			elif bolum == 3:
				Fonksiyonlar.personel_ekle( "Muhasebe" )
			else:
				print( "Hatalı Seçim" )
			
			cevap = input( "Devam etmek ister misiniz? (E/H)" ).upper( )
			if cevap == "E":
				continue
			else:
				break
	
	elif secim == 2:
		while True:
			print( "*******PERSONEL GÜNCELLEME*******" )
			bolum = int( input( """
			1- İnsan Kaynakları
			2- Bilgi İşlem
			3- Muhasebe
			4- Çıkış
			"""))
			if bolum == 4:
				break
			elif bolum == 1:
				Fonksiyonlar.personel_guncelle( "InsanKaynaklari" )
			elif bolum == 2:
				Fonksiyonlar.personel_guncelle( "BilgiIslem" )
			elif bolum == 3:
				Fonksiyonlar.personel_guncelle( "Muhasebe" )
			else:
				print( "Hatalı seçim" )
			cevap = input( "Devam etmek ister misiniz? (E/H)" ).upper( )
			if cevap == "E":
				continue
			else:
				break
				
	elif secim == 3:
		while True:
			print( "*******PERSONEL SİLME*******" )
			bolum = int( input("""
			1- İnsan Kaynakları
			2- Bilgi İşlem
			3- Muhasebe
			4- Çıkış
			"""))
			
			if bolum == 4:
				break
			elif bolum == 1:
				Fonksiyonlar.personel_sil("InsanKaynaklari")
			elif bolum == 2:
				Fonksiyonlar.personel_sil("BilgiIslem")
			elif bolum ==3:
				Fonksiyonlar.personel_sil("Muhasebe")
			else:
				print("Hatalı Seçim")
			cevap = input( "Devam etmek ister misiniz? (E/H)" ).upper( )
			if cevap == "E":
				continue
			else:
				break
				
	elif secim == 4:
		while True:
			print( "*******PERSONEL LİSTELEME*******" )
			bolum = int( input( """
			1- İnsan Kaynakları
			2- Bilgi İşlem
			3- Muhasebe
			4- Çıkış
			"""))
			
			if bolum == 4:
				break
			elif bolum == 1:
				print(Fonksiyonlar.personel_listele("InsanKaynaklari"))
			elif bolum == 2:
				print(Fonksiyonlar.personel_listele("BilgiIslem"))
			elif bolum == 3:
				print(Fonksiyonlar.personel_listele("Muhasebe"))
			else:
				print("Hatalı Seçim")
				
			cevap = input( "Devam etmek ister misiniz? (E/H)" ).upper( )
			if cevap == "E":
				continue
			else:
				break
	
	else:
		print("Hatalı Seçim")
		cevap = input( "Tekrar denemek ister misiniz (E/H)" ).upper( )
		if cevap == "E":
			continue
		else:
			break


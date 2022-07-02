"""
Personel isimli bir class tanımlayın
Nesne Nitelikleri: ad,soyad,tc,telefon,adres,maas
__init__ fonksiyonu ile kullanıcıdan bu özellikler sorularak doldurulsun

Kaydet() isimli method Personel.txt adında bir dosyaya kaydetsin
Bir tane sınıf üzerinden erişebilir Listele() adında bir method tanılayın dosyadaki verileri okuma işlemi gerçekleştirsin

"""

from Personel import Personel

while True:
	secim = input("""
		1- Kayıt İşlemi
		2- Listeleme
		3- Çıkış
	""")
	
	if secim == "1":
		per = Personel()
		per.kaydet()
	elif secim == "2":
		Personel.Listele()
	elif secim == "3":
		break
	else:
		print("Hatalı Seçim")
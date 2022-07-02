class Ders:
	
	# 2. yöntem
	def __init__(self, ders_adi, ders_saati, ders_ogretmeni, ders_baslama_tarihi):
		self.ders_adi = ders_adi
		self.ders_saati =  ders_saati
		self.ders_ogretmeni =  ders_ogretmeni
		self.ders_baslama_tarihi = ders_baslama_tarihi
	
	# Birinci yömtem
	# def __init__(self):
	# 	self.ders_adi = input("Ders Adı")
	# 	self.ders_saati =  input("Ders Saati")
	# 	self.ders_ogretmeni =  input("Ders Öğretmeni")
	# 	self.ders_baslama_tarihi = input("Ders Başlama Tarihi")
	
	
		
	def ders_kaydet( self ):
		try:
			import os
			dizin =  "C:\\UBY\\"
			kayit_dosyasi =  dizin+"Dersler.txt" # C:\UBY\Dersler.txt
			if (not os.path.exists(dizin)):
				os.mkdir(dizin)
			dosya =  open(kayit_dosyasi, "a+")
			
			yazi =  f"""
Ders Adi            :{self.ders_adi}
Ders Saati          :{self.ders_saati}
Ders Öğretmeni      :{self.ders_ogretmeni}
Ders Başlama Tarihi :{self.ders_baslama_tarihi}
			"""
			dosya.write(yazi)
			dosya.close()
			print("Ders başarıyla kayıt edildi")
			
		except:
			print("Dosya kayıt edilirken hata oluştu")
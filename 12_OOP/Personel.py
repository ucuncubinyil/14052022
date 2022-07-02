class Personel:
	
	def __init__(self):
		self.ad = input("Ad")
		self.soyad =  input("Soyad")
		self.tc =  input("T.C.")
		self.telefon =  input("Telefon")
		self.adres =  input("Adres")
		self.maas = input("Maaş")
		
	def kaydet( self ):
		import  os
		try:
			dizin = "C:\\UBY\\"
			if not os.path.exists( dizin ):
				os.mkdir( dizin )
			
			dosya = dizin + "Personel.txt"
			dosya = open( dosya, "a+" )
			yazi = f"""
Ad: {self.ad}
Soyad: {self.soyad}
TC: {self.tc}
Telefon : {self.telefon}
Adres : {self.adres}
Maaş :  {self.maas}"""
			dosya.write( yazi )
			dosya.close( )
		except:
			print("Hata oluştu")
			
	@classmethod
	def Listele( cls ):
		
		try:
			import  os
			dosya = "C:\\UBY\\Personel.txt"
			dosya =  open(dosya,"r")
			satirlar = dosya.readlines()
			dosya.close()
			for satir in satirlar:
				print(satir)
		except:
			print("Hata oluştu")
		
		
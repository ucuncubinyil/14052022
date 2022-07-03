class BeyazEsya:
	def __init__(self):
		self.marka = ""
		self.model = ""
		self.renk = ""
		self.fiyat = 0.0
		self.enerji_sinifi = ""
	
	def bilgi_yaz( self ):
		print(f"Bilgiler"
		      f"\nMarka:{self.marka}"
		      f"\nModel: {self.model}"
		      f"\nRenk: {self.renk}"
		      f"\nFiyat: {self.fiyat}"
		      f"\nEnerji Sınıfı: {self.enerji_sinifi}")
		
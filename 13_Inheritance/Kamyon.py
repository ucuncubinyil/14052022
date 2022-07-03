from  Arac import Arac

class Kamyon(Arac):
	
	def __init__(self):
		super().__init__()
		self.tasima_kapasitesi = 0
		self.yakit_depo_sayisi =  0
		
	def bilgi_yazdir( self ):
		super().bilgi_yazdir()
		print(f"Taşıma Kapasitesi: {self.tasima_kapasitesi}"
		      f"\nDepo Sayısı: {self.yakit_depo_sayisi} ")
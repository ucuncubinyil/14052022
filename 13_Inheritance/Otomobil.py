from Arac import Arac

class Otomobil(Arac):
	
	def __init__(self):
		super( ).__init__( )
		self.kasa_tipi = str( )
		self.vites_tipi = str()
		
	def bilgi_yazdir( self ):
		super().bilgi_yazdir()
		print(f"Kasa Tipi: {self.kasa_tipi}"
		      f"\nVites Tipi: {self.vites_tipi}")

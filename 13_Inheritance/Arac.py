from datetime import datetime as dt
class Arac:
	def __init__(self):
		self.marka = str()
		self.model =  str()
		self.renk =  str()
		self.uretim_tarihi = 0
		self.fiyat =  0.0
		self.ilan_tarihi =  dt.today().date()
		
	def bilgi_yazdir( self ):
		print(f"""Araç Bilgileri
Marka: {self.marka}
Model: {self.model}
Renk: {self.renk}
Üretim Yılı: {self.uretim_tarihi}
Fiyat : {self.fiyat}
İlan Tarihi: {self.ilan_tarihi}""")
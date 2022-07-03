from BeyazEsya import BeyazEsya
import os


class BuzDolabi( BeyazEsya ):
	
	def __init__( self ):
		super( ).__init__( )
		self.kapak_sayisi = 1
		self.hacim = 0
	
	def kaydet( self ):
		dizin = "C:\\DERS13\\"
		dosya = dizin + "BuzDolabi.txt"  # "C:\\DERS13\\BuzDolabi.txt\"
		
		if (not os.path.exists( dizin )):
			os.mkdir( dizin )
		
		if (not os.path.exists( dosya )):
			text = open( dosya, "a+" )
			yazi = f"""
             Marka: {self.marka},
             Model: {self.model},
             Renk: {self.renk},
             Fiyat: {self.fiyat},
             Enerji Sınıfı: {self.enerji_sinifi}
             Kapak Sayısı: {self.kapak_sayisi},
             Hacim: {self.hacim}
             """
			text.write( yazi )
		else:
			text = open( dosya, "a+" )
		
		yazi = f"""
                     Marka: {self.marka},
                     Model: {self.model},
                     Renk: {self.renk},
                     Fiyat: {self.fiyat},
                     Enerji Sınıfı: {self.enerji_sinifi}
                     Kapak Sayısı: {self.kapak_sayisi},
                     Hacim: {self.hacim}
                     """
		text.write( yazi )
		text.close( )

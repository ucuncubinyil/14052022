#CONSTRUCTOR METHOD

"""
Kurucu method: class'tan instance alındığında otomatik olarak çalışan bir methoddur.
__init__ ismiyle tanımlanır.
Eğer kurucu metodu tanımlamazsak görünmez olrak default da def __init__(self): şeklinde kendisi otomatik tanımlar.
"""

class Insan():
	
	# def __init__(self): #constructure
	# 	print("Selam")
	# 	# her zaman çalışır
	#
	# def __init__( self ):
	# 	pass
	
	def __init__( self ):
		self.ad =  ""
		self.soyad = ""
	
	@classmethod
	def konus( cls, insan ):
		try:
			if insan.ad == "":
				raise RuntimeError( "Boş nesne var" )
			print( f"AD: {insan.ad}, SOYAD: {insan.soyad}" )
		except RuntimeError:
			print("Ad boş geliyor")
	
	def konusma( self ):
		print( f"AD: {self.ad}, SOYAD: {self.soyad}" )
	
	@classmethod
	def yazdir( cls, liste ):
		
		for insan in liste:
			print( insan.ad, insan.soyad )
	
	@classmethod
	def kaydet( cls, liste ):
		a = Insan( )
		a.ad = input( "Ad:" )
		a.soyad = input( "Soyad" )
		liste.append( a )


mehmet = Insan() # constructor metot çalışır.


Insan.konus(mehmet)
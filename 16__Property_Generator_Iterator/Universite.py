class Universite():
	def __init__(self):
		self.__vize =0
		self.__final =0
		
	def get_vize( self ):
		return  self.__vize
	
	def set_vize( self, parametre ):
		if(parametre <0 or parametre >100):
			while True:
				print("Hatalı Vize Notu Girişi")
				vizenot =  int(input("Vize Notunuz: "))
				if vizenot <0 or vizenot >100:
					continue
				else:
					self.__vize =  vizenot
					break
		else:
			self.__vize =  parametre
	
	vize = property(get_vize, set_vize)

# Üstteki property oluşturmanın kısa yöntemi
	
	@property
	def  final( self ):
		return  self.__final
	
	@final.setter
	def final( self, parametre ):
		if (parametre < 0 or parametre > 100):
			while True:
				print( "Hatalı Final Notu Girişi" )
				finalnot = int( input( "Final Notunuz: " ) )
				if finalnot < 0 or finalnot > 100:
					continue
				else:
					self.__final = finalnot
					break
		else:
			self.__final = parametre
			
	def ortalama( self ):
		print(f"Ders Ortalaması:  { ( (self.__vize*0.4) + (self.__final*0.6)  )  }")
	
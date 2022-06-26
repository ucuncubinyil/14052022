class Insan():
	ad = ""
	soyad =""
	
	@classmethod
	def konus( cls, insan ):
		print(f"AD: {insan.ad}, SOYAD: {insan.soyad}")
	
	def konusma( self ):
		print(f"AD: {self.ad}, SOYAD: {self.soyad}")
	
	@classmethod
	def yazdir( cls, liste ):
		
		for insan in liste:
			print(insan.ad, insan.soyad)
			
	@classmethod
	def kaydet( cls, liste ):
		a =  Insan()
		a.ad =  input("Ad:")
		a.soyad =  input("Soyad")
		liste.append(a)
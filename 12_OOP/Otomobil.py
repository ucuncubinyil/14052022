class Otomobil:
	def __init__( self, marka, model, renk, motor_hacmi, uretim_yili ):
		self.marka = marka
		self.model = model
		self.renk = renk
		self.motor_hacmi = motor_hacmi
		self.uretim_yili = uretim_yili
		self.kaydet( )
	# None ve null
	
	def kaydet( self ):
		import os, datetime
		dizin = "C:\\UBY\\"
		
		try:
			if not os.path.exists( dizin ):
				os.mkdir( dizin )
			
			dosya = dizin + str( datetime.date.today( ) ) + ".txt"
			acik_dosya = open( dosya, "a+" )
			
			yazi = f"""
			MARKA           :{self.marka}
			MODEL           :{self.model}
			RENK            :{self.renk}
			MOTOR HACMİ     :{self.motor_hacmi}
			ÜRETİM YILI     :{self.uretim_yili}
					"""
			acik_dosya.write( yazi )
			acik_dosya.close( )
		except FileNotFoundError:
			print( "Dosya Bulunamadı" )
		except IOError:
			print( "Yazma hatası oluştu" )

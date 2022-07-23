############# KAPSULLEME (Encapsulation) #############

# getter methodlerı private özellikleri değerlerini okumamızı sağlar. readonly
# setter methodlar private özelliklere değer atamamızı sağlar.
#
# class Kapsul():
#
# 	def __init__(self):
# 		self.__gizliOzellik = "Varsayolan Değer"
# 		self.__gizli2 =  "Gizli 2 Varsayılan Değer"
#
# 	def getGizli2( self ):
# 		return self.__gizli2
#
# 	def setGizli2( self, deger=5 ):
# 		self.__gizli2 =  deger
#
# 	def getGizliOzellik( self ):
# 		return self.__gizliOzellik
#
# 	def setGizliOzellik( self, deger ):
# 		self.__gizliOzellik =  deger
#
#
# k = Kapsul()
# print(k.getGizli2())
# k.setGizli2()
# print(k.getGizli2())


### Bir Banka müşteri kayıt sistemi oluşturulurken kayıt esnasında ad,soyad,tc(11 hane) ve
# Iban(TR+12) bilgileri alınıyor. Gerekl kontrolleri sağlayarak müşteri kayıt platformunu oluşturunuz.


# class BankaKayit:
#
# 	isim = ""
# 	soyisim = ""
# 	__tc = ""
# 	__iban = ""
#
# 	def kaydet( self ):
#
# 		self.isim = input( "İsim: " )
# 		self.soyisim = input( "Soyisim: " )
#
# 		while True:
# 			TC = input( "TC: " )
# 			if (len( TC ) == 11 and TC.isnumeric( )):
# 				self.__tc = TC
# 				break
# 			else:
# 				print( "Lütfen TC nizi doğru giriniz" )
# 				continue
# 		while True:
# 			IBAN = input( "IBAN: " )  # TR3546534354353654
# 			tr = IBAN[0].upper()+IBAN[1].upper()
# 			if(tr == "TR"):
# 				iban =  IBAN[2:]
#
# 				if(len(iban) == 12 and iban.isnumeric()):
# 					self.__iban = IBAN
# 					break
# 				else:
# 					print("IBAN bilginizi 12 hane olacak şekilde giriniz")
# 					continue
# 			else:
# 				print("IBAN nın başında 'TR' ifadesi olmak zorundadır")
# 				continue
#
# 	def yaz( self ):
# 		print(f"""
# 			İSİM        {self.isim}
# 			SOYİSİM     {self.soyisim}
# 			TC          {self.__tc}
# 			IBAN        {self.__iban}
# 		""")
#
# ahmetinHesabi =  BankaKayit()
# ahmetinHesabi.kaydet()
# ahmetinHesabi.yaz()


class BankaKayit:
	
	def __init__( self ):
		self.isim = input( "İsim: " )
		self.soyisim = input( "Soyisim: " )
		self.__iban = ""
		self.__tc = ""
		self.__setIBAN( )
		self.__setTC( )
	
	def getIBAN( self ):
		return self.__iban
	
	def __setIBAN( self ):
		while True:
			IBAN = input( "IBAN: " )  # TR3546534354353654
			tr = IBAN[ 0 ].upper( ) + IBAN[ 1 ].upper( )
			if (tr == "TR"):
				iban = IBAN[ 2: ]
				
				if (len( iban ) == 12 and iban.isnumeric( )):
					self.__iban = IBAN
					break
				else:
					print( "IBAN bilginizi 12 hane olacak şekilde giriniz" )
					continue
			else:
				print( "IBAN nın başında 'TR' ifadesi olmak zorundadır" )
				continue
	
	def getTC( self ):
		return self.__tc
	
	def __setTC( self ):
		while True:
			TC = input( "TC: " )
			if (len( TC ) == 11 and TC.isnumeric( )):
				self.__tc = TC
				break
			else:
				print( "Lütfen TC nizi doğru giriniz" )
				continue
	
	def yaz( self ):
		print(f"""
İSİM        {self.isim}
SOYİSİM     {self.soyisim}
TC          {self.__tc}
IBAN        {self.__iban}
""")


ahmetinHesabi =  BankaKayit()
ahmetinHesabi.yaz()
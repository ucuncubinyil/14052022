'''
## ACCESS MODIFIER: public,private,protected

#public: Yazılım dillerinde genel erişime açık anlamına gelir.
# Herhangi bir erişim belirteci verilemezse default olarak hem class hem field'lar
public tanımlanmış olur.
'''


# class Muhendis:
# 	ad = 'Mehmet Nuri'
# 	soyad = "Öztürk"
#
# 	def ekrana_yaz( self ):
# 		print(self.ad)
# 		print(self.soyad)
#
#
# muhendis = Muhendis()
# print(muhendis.ad)
# muhendis.ekrana_yaz()

# private: Yazılım dillerinde SADECE TANIMLANDIĞI CLASS içerisinde erişilebilir
# anlamına gelir. '__' iki adet alt çizgi ile belirtilir.

# class Muhendis:
# 	ad = 'Mehmet Nuri'  # Public
# 	__soyad = "Öztürk"  # private
#
# 	def ekrana_yaz( self ):
# 		print( self.ad )
# 		print( self.__soyad )
#
#
# muhendis = Muhendis( )
# print( muhendis.ad )
# # print(muhendis.__soyad) # Hata verecektir
# muhendis.ekrana_yaz( )

# class Uye:
# 	isim =""
# 	soyisim=""
# 	__tc =""
#
# 	def kaydet( self ):
# 		self.isim =  input("AD:")
# 		self.soyisim = input("SOY İSİM")
# 		TC = input("TC:")
# 		if (len(TC) == 11 and  TC.isnumeric()):
# 			self.__tc = TC
# 		else:
# 			self.__tc =  "00000000000"
#
# 	def yaz( self ):
# 		print(f"AD: {self.isim}, SOYAD:{self.soyisim}, TC: {self.__tc}")
#
#
# print("TC bilginizi 11 hane olacak şekilde giriniz: ")
# uye = Uye()
# uye.kaydet()
# uye.yaz()


#protected: Sınıf içinde public ama sınıf dışında sadece miras alınan(inheritance)
# classlarda erişilebilir. '_' tek alt çizgi ile tanımlanır.

# class Muhendis:
# 	ad ="Mehmet"
# 	soyad="Öztürk"
#
# 	def _ekranayaz( self ): # protected
# 		print(self.ad)
# 		print(self.soyad)
#
#
# class YazilimMuhendisi(Muhendis):
#
# 	def __init__(self):
# 		self._ekranayaz()
#
# muhendis =  Muhendis()
# muhendis._ekranayaz()
#
# yazilim = YazilimMuhendisi()
# yazilim._ekranayaz()











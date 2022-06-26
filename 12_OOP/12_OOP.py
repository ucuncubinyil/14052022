###################################################################
############### OOP: Object Oriented Programming ##################
################ Nesneli Yöneliklik Programlama ###################
###################################################################
'''
OOP: büyük projeler yazılacağı zamanlarda, proje temelini oluşturma aşamasından başlayarak analiz
sentez kodlama sınama ve onarım gibi yaşam döngüsü adımlarında daimi olarak uyugulanması ve takip
edilmesi gerekli bir yapıdır.
En büyük kazancı proje temelini oluşturan yapıların bir bütün halinde(object) tutulması ve
 yapınların özelliklerinin(field) alt
başlıklar halinde yapıya özel olmasını sağlar. Kayıt güncelleme,silme veya okuma işlemlerinde
 object (nesne) sayesinde veri bütünlüğü
sağlanmış ve tek bir işlemle manipüle edeilmiş olur.
'''


## Bir okulunuz oolduğunu ve öğrenci kaydı yapılacağını düşünelim.
# Her öğrencinin ad,soyad,tc,dogumtarihi gibi bilgileri kayıt edilecektir.

# ad = "Mehmet"
# soyad = "Ötürk"
# tc_no = "123"
# dogum_tarihi = "20.11.1993"
#
# ad = "Yusuf"
# soyad = "Çağlayan"
# tc_no = "12"
# dogum_tarihi = "11.05.1999"


class Ogrenci:
	# Sınıfın field(Alan-Nitelik)leri
	ad = ""
	soyad = ""
	tc_no = ""
	dogum_tarihi = ""
	numara = 0
	
	# self=> nesneyi temsil ediyor ve bu methodun nesne üzerinden kullanılabileceğini gösteriyor.
	def bilgi_yaz( self ):
		print( f"Ad: {self.ad}, Soyad: {self.soyad}" )
		
	@classmethod  # cls => cls ifadesi Class üzerinden çağrılabileceğini belirtir.
	def  ara( cls, ad, liste ):
		for i in liste:
			if (i.ad == ad):
				print(f"Ad {i.ad}, Soyad {i.soyad}")


# Instance: Bir classtan örneklem almaya denir. Alınan örnek(object) class'taki tanımlı
# olan özelliklere sahip olacaktır.
mehmet = Ogrenci( )  # Instance aldık
mehmet.ad = "Mehmet Nuri"
mehmet.soyad = "Öztürk"
mehmet.tc_no = "123"
mehmet.dogum_tarihi = "20.11.1993"
mehmet.numara = 35
# mehmet.bilgi_yaz( )

ahmet = Ogrenci( )
ahmet.ad = "Ahmet"
ahmet.soyad = "Durmaz"
ahmet.tc_no = "55"
ahmet.dogum_tarihi = "11.11.1995"
# ahmet.bilgi_yaz()


liste =  list()
liste.append(mehmet)
liste.append(ahmet)

Ogrenci.ara("Ahmet", liste)

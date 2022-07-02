############## KALITIM-INHERITANCE ###############

'''
Inheritance veya kalıtım bir sınıfın başka bir sınıfan özelliklerini(attribute) ve metodlarını miras almasıdır.
Bu yapı aslında bizim kend anne babamızdan değişik özelliklerive davranışları miras almamıza benzetilebilir.

Örneğin, bir şirketin çalışanlarını tasarlamak için sınıflar oluşturuyoruz. Bunun için Yönetici, Proje Direktörü, İşçi gibi sınıflar oluşturmamız gerekiyor.
Aslında baktığımız zaman bu sınıfların hepsinin belli ortak metodları ve özellikleri bulunuyor.
O zaman bu ortak özellikleri ve metotları tekrar tekrar bu sınfıların içinde tanımlamak yerine, bir tane ana-temel(base) class tanımlayıp ortak özellik ve metotları bu class'ta yazıp diğer classların bu base classı miras almasını sağlayabiliriz. Inheritance'ın temel amacı budur.
'''


class Calisan():
	def __init__(self, isim, maas, departman):
		self.isim = isim
		self.maas =  maas
		self.departman = departman
	
	def bilgi_goster( self ):
		print("Çalışan sınıfının bilgileri....")
		print(f"İsim: {self.isim}, Maaş: {self.maas}, Departman:{self.departman}")
	
	@classmethod
	def departman_degistir( cls, yeni_departman, object ):
		print("Departman değiştiriliyor...")
		object.departman =  yeni_departman
		
		
class Yonetici(Calisan):
	
	def __init__(self, isim, maas, departman, unvan):
		self.isim = isim
		self.maas = maas
		self.departman = departman
		self.unvan = unvan
		
	
	def zam_yap( self, zam_miktari ):
		print("Maaşa Zam Yapılıyor")
		self.maas = str(int(self.maas)+zam_miktari)
		
	def bilgi_goster( self ):
		print(f"İsim: {self.isim}, Maaş: {self.maas}, Departman:{self.departman}, Ünvan {self.unvan}")
	
		

yonetici1 = Yonetici("Ahmet", "300", "IK","MÜDÜR")
print(yonetici1.isim)
print(yonetici1.maas)
yonetici1.bilgi_goster()

Yonetici.departman_degistir("IT", yonetici1)
yonetici1.bilgi_goster()


c =  Calisan("Murat", "100", "Temizlik")
c.bilgi_goster()
Calisan.departman_degistir("MUDUR", c)
c.bilgi_goster()


yonetici1.zam_yap(300)
yonetici1.bilgi_goster()


### OVERRIDING (iptal Etme-Revize)


############## KALITIM-INHERITANCE ###############

'''
Inheritance veya kalıtım bir sınıfın başka bir sınıfan özelliklerini(attribute) ve metodlarını miras almasıdır.
Bu yapı aslında bizim kend anne babamızdan değişik özelliklerive davranışları miras almamıza benzetilebilir.

Örneğin, bir şirketin çalışanlarını tasarlamak için sınıflar oluşturuyoruz. Bunun için Yönetici, Proje Direktörü, İşçi gibi sınıflar oluşturmamız gerekiyor.
Aslında baktığımız zaman bu sınıfların hepsinin belli ortak metodları ve özellikleri bulunuyor.
O zaman bu ortak özellikleri ve metotları tekrar tekrar bu sınfıların içinde tanımlamak yerine, bir tane ana-temel(base) class tanımlayıp ortak özellik ve metotları bu class'ta yazıp diğer classların bu base classı miras almasını sağlayabiliriz. Inheritance'ın temel amacı budur.
'''

#
# class Calisan():
# 	def __init__(self, isim, maas, departman):
# 		self.isim = isim
# 		self.maas =  maas
# 		self.departman = departman
#
# 	def bilgi_goster( self ):
# 		print("Çalışan sınıfının bilgileri....")
# 		print(f"İsim: {self.isim}, Maaş: {self.maas}, Departman:{self.departman}")
#
# 	@classmethod
# 	def departman_degistir( cls, yeni_departman, object ):
# 		print("Departman değiştiriliyor...")
# 		object.departman =  yeni_departman
#
# 	##SUPER Anahtar Kelimesi
# 	"""
# 	super anahtar kelimesi: türemiş sınıfta base sınıftan de miras alınan bir methodu tekrar tanımladığımızda override işlemi gerçekleşiyordu.
# 	 Super keyword ü ile bu methodu override edip yok etmek yerine basedeki gerçekleşen işlemi alıp sadece türemiş sınıfta atanan özelliği eklemizi sağlar.
# 	  Böyle Base classdaki method komple yok sayılmak yerine yeni özellikle revize edilmiş olur.
# 	"""
#
#
# class Yonetici(Calisan):
#
# 	def __init__(self, isim, maas, departman, unvan):
# 		super().__init__(isim, maas, departman) #super anahtarı base class'ı temsil eder.
# 		self.departman = departman
# 		self.unvan = unvan
#
#
# 	def zam_yap( self, zam_miktari ):
# 		print("Maaşa Zam Yapılıyor")
# 		self.maas = str(int(self.maas)+zam_miktari)
#
# 	def bilgi_goster( self ):
# 		print(f"İsim: {self.isim}, Maaş: {self.maas}, Departman:{self.departman}, Ünvan {self.unvan}")
#
#
#
# yonetici1 = Yonetici("Ahmet", "300", "IK","MÜDÜR")
# print(yonetici1.isim)
# print(yonetici1.maas)
# yonetici1.bilgi_goster()
#
# Yonetici.departman_degistir("IT", yonetici1)
# yonetici1.bilgi_goster()
#
#
# c =  Calisan("Murat", "100", "Temizlik")
# c.bilgi_goster()
# Calisan.departman_degistir("MUDUR", c)
# c.bilgi_goster()
#
#
# yonetici1.zam_yap(300)
# yonetici1.bilgi_goster()


### OVERRIDING (iptal Etme-Revize)
# from Otomobil import Otomobil
# from Kamyon import Kamyon
#
# oto = Otomobil( )
# oto.marka = "Volswagen"
# oto.model = "Possat"
# oto.kasa_tipi = "Manda"
# oto.uretim_tarihi = 2022
# oto.renk = "Siyah"
# oto.fiyat = 750000
# oto.vites_tipi = "Otomatik"
#
# oto.bilgi_yazdir( )
#
# print( "****************************" )
#
# kamyon = Kamyon( )
# kamyon.marka = "Ford"
# kamyon.model = "CX-120"
# kamyon.uretim_tarihi = 1999
# kamyon.renk = "Beyaz"
# kamyon.fiyat =  5000000
# kamyon.yakit_depo_sayisi = 2
# kamyon.tasima_kapasitesi = 40000
# kamyon.bilgi_yazdir()


#
# from  BuzDolabi import BuzDolabi as bd
#
# bud = bd()
# bud.marka = "Bosh"
# bud.model = "lakjsdlkahs"
# bud.renk = "Gri"
# bud.fiyat = 7500
# bud.enerji_sinifi = "A+++"
# bud.kapak_sayisi = 4
# bud.hacim =  960
# bud.kaydet()


from CamasirMakinesi import CamasirMakinesi

cm = CamasirMakinesi( )
cm.marka = "Arçelik"
cm.model = "AX-45a"
cm.renk = "Kırmızı"
cm.fiyat = 12000
cm.yikama_kapasitesi = 9
cm.hizli_yikama = True
cm.enerji_sinifi = "B+"

cm.bilgi_yaz()
# cm.kaydet()
#
# ÖDEV
#
# 1- Elektronik bir mağaza olduğunu düşün
# 2-  Benzer özellikleri olan 2 ürün seç yada daha fazla
# 3- Bu ürünlerin ortak özelliklerini bir sınıftan miras almasını sağla
# 4- Ürünlerin bilgilerini txt dosyasında barındır
# 5- Ürünleri listele
# 6- Ürünleri sil
# 7- Güncelle
# 8- Özelliklerini yaz
# 9- Özelliklerini Güncelle
# 10- Özelliklerini Sil


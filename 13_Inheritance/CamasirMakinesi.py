from texttable import Texttable
from BeyazEsya import BeyazEsya
import os
class CamasirMakinesi(BeyazEsya):
	
	def __init__(self):
		super().__init__()
		self.yikama_kapasitesi = 0
		self.hizli_yikama =  False
		
	def bilgi_yaz( self ):
		super().bilgi_yaz()
		hizli = ""
		
		if self.hizli_yikama == True:
			hizli = "VAR"
		else:
			hizli = "YOK"
		
		metin =  f"Yıkama Kapasitesi: {self.yikama_kapasitesi}\n" \
		         f"Hızlı Yıkama: {hizli}"
		print(metin)
		
		
		liste = [ self.marka, self.model, self.enerji_sinifi, str(self.fiyat), str(self.yikama_kapasitesi)]
		en_uzun = len(max( liste, key=len ))
		
		# custom_char =  str("-"*en_uzun)
		# tab_char = str("\t"*(int(en_uzun/4)))
		
		t = Texttable( )
		t.set_cols_align( [ "c", "c", "c","c", "c", "c" ] )
		t.set_deco( Texttable.HEADER )
		t.add_rows( [ [ 'Marka', 'Model', 'Enerji Sınıfı', 'Fiyat', 'Yıkama Kapasitesi', 'Hızlı Yıkama' ],
		              [ self.marka,self.model, self.enerji_sinifi,self.fiyat,self.yikama_kapasitesi,hizli ] ] )
		print( t.draw( ) )
		
		
		
		# t = PrettyTable( [ 'Marka', 'Model', 'Enerji Sınıfı', 'Fiyat', 'Yıkama Kapasitesi', 'Hızlı Yıkama' ] )
		# t.add_row( [ {self.marka},{self.model}, {self.enerji_sinifi},{self.fiyat},{self.yikama_kapasitesi},{self.hizli_yikama}] )
		# print( t )
		# print( f"Marka{tab_char}Model{tab_char}Enerji{tab_char}Fiyat{tab_char}Yıkama Kapasitesi{tab_char}Hızlı Yıkama" )
		# print( f"\n{custom_char}{tab_char}{custom_char}{tab_char}{custom_char}{tab_char}{custom_char}{tab_char}{custom_char}{tab_char}{custom_char}" )
		#
		# print(f"\n{self.marka}{tab_char}{self.model}{tab_char}{self.enerji_sinifi}{tab_char}{self.fiyat}{tab_char}{self.yikama_kapasitesi}{tab_char}{self.hizli_yikama}")
		#
		#
		
		
	def kaydet( self ):
		dizin = "C:\\DERS13"
		dosya =  dizin+"\\CamasirMakinesi.txt"
		
		if not os.path.exists(dizin):
			os.mkdir(dizin)
			
		if not os.path.exists(dosya):
			text = open(dosya, "a+")
			liste =  [self.marka,self.model,self.enerji_sinifi,self.fiyat, self.yikama_kapasitesi,self.hizli_yikama]
			en_uzun  = len(max(liste, key=len))
			
			seperator =  str("-"*en_uzun)
			
			text.write("Marka\t\tModel\t\tEnerji\t\tFiyat\t\tYıkama Kapasitesi\t\tHızlı Yıkama")
			text.write("\n--------\t\t--------\t\t--------\t\t--------\t\t--------\t\t--------\t\t")
			print(dosya, " dosyası oluşturuldu")
		else:
			text = open(dosya, "a+")
			
		text.write(f"\n{self.marka}\t\t{self.model}\t\t{self.enerji_sinifi}\t\t{self.fiyat}\t\t{self.yikama_kapasitesi}\t\t{self.hizli_yikama}")
		text.close()
		
	
		
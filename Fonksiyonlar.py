def personel_ekle(bolum_adi):
	personel_sayi =  int(input("Kaç personel kayıt edilecek?"))
	dosya =  open("C:\\TEST\\PersonelKayitlari\\"+ str(bolum_adi)+ ".txt", "a+")
	for i in range(personel_sayi):
		ad = input("Personel Adı:")
		soyad = input("Personel Soyadı:")
		dogum_yili = input("Personel Doğum Tarihi: ")
		dosya.write(ad+"    "+soyad+"   "+dogum_yili+"\n")
	dosya.close()
	

def personel_listele(bolum_adi):
	dosya =  open("C:\\TEST\\PersonelKayitlari\\"+ str(bolum_adi)+ ".txt", "r+")
	return  dosya.read()


def personel_guncelle(bolum_adi):
	dosya =  open("C:\\TEST\\PersonelKayitlari\\"+ str(bolum_adi)+ ".txt", "r+")
	personel_listesi =  dosya.readlines()
	dosya.seek(0)
	print(dosya.read())
	satir =  int(input("Kaçıncı Sırada: "))
	dosya.close()
	print(personel_listesi)
	del personel_listesi[satir-1]
	ad = input( "Personel Adı:" )
	soyad = input( "Personel Soyadı:" )
	dogum_yili = input( "Personel Doğum Tarihi: " )
	personel_listesi.insert(satir-1, ad+"    "+soyad+"   "+dogum_yili+"\n")
	yeni_dosya =  open("C:\\TEST\\PersonelKayitlari\\"+ str(bolum_adi)+ ".txt", "w+")
	yeni_dosya.writelines(personel_listesi)
	print(personel_listesi)
	yeni_dosya.close()

def personel_sil(bolum_adi):
	dosya =  open("C:\\TEST\\PersonelKayitlari\\"+ str(bolum_adi)+ ".txt", "r+")
	personel_listesi = dosya.readlines()
	dosya.seek(0)
	print(dosya.read())
	silinecek_personel =  int(input("Silinecek personelin sıra numarasını girin: "))
	del personel_listesi[silinecek_personel-1]
	dosya.close()
	yeni_personel_listesi =  open("C:\\TEST\\PersonelKayitlari\\"+ str(bolum_adi)+ ".txt", "w+")
	yeni_personel_listesi.writelines(personel_listesi)
	yeni_personel_listesi.close()
	


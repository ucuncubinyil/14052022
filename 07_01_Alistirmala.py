# sozluk = dict( )
#
# list1 = [ 1, 2, 3, 4, 5 ]
# list2 = [ 6, 7, 8, 9, 10 ]
# list3 = [ 11, 22, 33 ]
#
# sozluk[ "x" ] = list1
# sozluk[ "y" ] = list2
# sozluk[ "z" ] = list3
#
# print(sozluk)


#  sozluk = {'x': [1, 2, 3, 4, 5], 'y': [6, 7, 8, 9, 10], 'z': [11, 22, 33]}

#### SORU: Kullanıcıdan alınan ad,soyad,yas,cinsiyet bilgilerini
# Personel isimli bir sözlükte saklayın ve
# ad soyad bilgisini sözlükten alarak ekrana yazdırınız.

# personel = dict()
# personel["ad"] = input("Personel Adı: ")
# personel["soyad"] = input("Personel Soyad: ")
# personel["yasi"] = int(input("Personel Yaş: "))
# personel["cinsiyet"] = input("Personel Cinsiyet: ")
#
# print(personel)


# ad =  "Ayşe Işpir Ömür"
# ad =  ad.replace("ş","s").replace("Ö", "O").replace("ü", "u")
#
# print(ad)


# SORU: Bir firmanın İnsan kaynakları,Bilgi İşlem ve
# Muhasebe departmanlarının çalışan listelerini yöneticiden isteyerek bir dict atınız
# ve ekrana istenilen bölümdeki çalışanları listeyiniz.
#
# IK = list( )
# IT = list( )
# MHSB = list( )
# firma = dict( )
#
# for i in range( 1 ):
#     IK.append( input( "IK personel ad soyad bilgilerini girin: " ) )
#     IT.append( input( "IT personel ad soyad bilgilerini girin: " ) )
#     MHSB.append( input( "Muhasabe personel ad soyad bilgilerini girin: " ) )
#
# firma[ "ik" ] = IK
# firma[ "it" ] = IT
# firma[ "mhsb" ] = MHSB
#
# secim = input( "İnsan Kaynakları(ik) - Bilgi İşlem(it)- Muhasebe(mhsb) bölüm kodunu giriniz" )
#
# if secim != "ik" and secim != "it" and secim != "mhsb":
#     print( "Hatalı seçim" )
# else:
#     for i in firma[ secim ]:
#         print( i )
#
# print(firma)


yasakli_kemeler = ['ı', 'ş', 'ğ', 'ö', 'ü', 'ç']
uygun_kelimeler = ['i', 's', 'g', 'o', 'u', 'c']

metin =  input("Metninizi giriniz :")

for i in metin:

    if i in yasakli_kemeler:
        indx = yasakli_kemeler.index(i)
        krktr =  uygun_kelimeler[indx]
        print(krktr)
        metin =  metin.replace(i, krktr)

print(metin)

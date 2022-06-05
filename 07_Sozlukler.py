# ################## DICTIONARY (SOZLUK) ########################
# # sozluk = { }
# # sozluk2 = dict( )
# #
# # sozluk = { "renk": "Kırmızı", "renk2": "Mor", "renk3": "Turuncu" }
# #
# # print( sozluk )
# # print( type( sozluk ) )
# # print( sozluk[ "renk" ] )
# #
# # mehmetin_bilgileri = {
# #         "adi": "Mehmet Nuri",
# #         "soyadi": "Öztürk",
# #         "dogumYili": 1993,
# #         "unvan": "Sn. Sf. Developer",
# #         "yasi": 28,
# #         "medeni_hal": False
# #         }
# #
# # # Anahtardan değer okuma
# # print( mehmetin_bilgileri[ "soyadi" ] )
# #
# # # Sözlüğü temizleme
# # sozluk.clear( )
# #
# # # Sözlüğü bellekten silme
# # del sozluk
# #
# # # Sözlüğün anahtarlarını listeleme
# # print( mehmetin_bilgileri.keys( ) )
# #
# # # Sözlüğün değerlerini listeleme
# # print( mehmetin_bilgileri.values( ) )
# #
# # # Sözlük içindeki öğeleri listeleme
# # print( mehmetin_bilgileri.items( ) )
# #
# # # Sözlüğün uzunluğu görme
# # print( len( mehmetin_bilgileri ) )
# #
# # print( "dogumYili" in mehmetin_bilgileri )
# # print( 1993 in mehmetin_bilgileri.values( ) )
# # print( 1993 not in mehmetin_bilgileri.values( ) )
#
# s1 = { "ad": "Nimet", "soyad": "Ayça" }
# s2 = { "ad": "Ahmet", "soyad": "Turan" }
# s3 = { "ad": "Muzaffer", "soyad": "Kırıcı" }
#
#
# print(s3)
# s4 = s3.copy()
# print(s4)
#
# s2.pop("soyad")
# print(s2)
#
# # s1 = s2
# # print(s1)
# # s2 = s3
# # print(s3)
# # s3 = s1
# # print(s3)
# #
# # s3["ad"] = "Kerem"
# # print(s3)
# #
# # del s3["ad"]
# # print(s3)
#
# # print(s1 == s2)
# # print(s1 != s2)
# #
# # for anahtar in s1.keys():
# #     print(anahtar)
# #
# # for degerler in s1.values():
# #     print(degerler)
# #
# # # sozlüğü güncelleme
# # s2.update(s3)
# # print(s2)
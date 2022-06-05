# meyveler = list( )
# sebzeler = [ ]
# musteriler = list( )
#
# ELMA = 0
# ARMUT = 0
# MUZ = 0
# KIRAZ = 0
# CILEK = 0
# PATLICAN = 0
# DOMAT = 0
# BIBER = 0
# PADDES = 0
# SOGAN = 0
#
# while True:
#     print( "********************** PYTHON MANAVINA HOŞ GELDİNİZ **********************" )
#     print( "Meyve mi istersiniz yoksa sebze mi? (M/S) Çıkmak için(Ç)" )
#
#     secim = input( "Seçiminiz" ).upper( )
#
#     if secim == "M":
#         while True:
#             print( "1-Elma\n2-Armut\n3-Muz\n4-Kiraz\n5-Çilek\n6-Anamenü" )
#             meyve_secim = int( input( "Meyve Seçiminiz: " ) )
#
#             if meyve_secim == 1:
#                 if ("ELMA" not in meyveler):
#                     meyveler.append( "ELMA" )
#                 ELMA += int( input( "Kaç kilo istersiniz: " ) )
#                 donus = input( "Başka bir arzunuz var mı ? (E/H)" ).upper( )
#                 if donus == "E":
#                     continue
#                 else:
#                     break
#
#             elif meyve_secim == 2:
#                 if ("ARMUT" not in meyveler):
#                     meyveler.append( "ARMUT" )
#                 ARMUT += int( input( "Kaç kilo istersiniz: " ) )
#                 donus = input( "Başka bir arzunuz var mı ? (E/H)" ).upper( )
#                 if donus == "E":
#                     continue
#                 else:
#                     break
#
#             elif meyve_secim == 3:
#                 if ("MUZ" not in meyveler):
#                     meyveler.append( "MUZ" )
#                 MUZ += int( input( "Kaç kilo istersiniz: " ) )
#                 donus = input( "Başka bir arzunuz var mı ? (E/H)" ).upper( )
#                 if donus == "E":
#                     continue
#                 else:
#                     break
#
#             elif meyve_secim == 4:
#                 if ("KIRAZ" not in meyveler):
#                     meyveler.append( "KIRAZ" )
#                 KIRAZ += int( input( "Kaç kilo istersiniz: " ) )
#                 donus = input( "Başka bir arzunuz var mı ? (E/H)" ).upper( )
#                 if donus == "E":
#                     continue
#                 else:
#                     break
#
#             elif meyve_secim == 5:
#                 if ("CILEK" not in meyveler):
#                     meyveler.append( "CILEK" )
#                 CILEK += int( input( "Kaç kilo istersiniz: " ) )
#                 donus = input( "Başka bir arzunuz var mı ? (E/H)" ).upper( )
#                 if donus == "E":
#                     continue
#                 else:
#                     break
#             elif meyve_secim == 6:
#                 break
#             else:
#                 print( "Hatalı seçim yapınız ! " )
#
#     elif secim == "S":
#         while True:
#             print("1-Patlıcan\n2-Domat\n3-Biber\n4-Paddes\n5-Soğan\n6-Anamenü")
#             sebze_secim = int(input("Seçiminiz: "))
#
#             if sebze_secim == 1:
#                 if "PATLICAN" not in sebzeler:
#                     sebzeler.append("PATLICAN")
#                 PATLICAN += int(input("Kaç kilo istersiniz ? "))
#                 donus = input("Başka bir isteğiniz var mı? (E/H)").upper()
#                 if donus == "E":
#                     continue
#                 else:
#                     break
#
#             elif sebze_secim == 2:
#                 if "DOMAT" not in sebzeler:
#                     sebzeler.append("DOMAT")
#                 DOMAT += int(input("Kaç kilo istersiniz ? "))
#                 donus = input("Başka bir isteğiniz var mı? (E/H)").upper()
#                 if donus == "E":
#                     continue
#                 else:
#                     break
#             elif sebze_secim == 3:
#                 if "BIBER" not in sebzeler:
#                     sebzeler.append("BIBER")
#                 BIBER += int(input("Kaç kilo istersiniz ? "))
#                 donus = input("Başka bir isteğiniz var mı? (E/H)").upper()
#                 if donus == "E":
#                     continue
#                 else:
#                     break
#
#             elif sebze_secim == 4:
#                 if "PADDES" not in sebzeler:
#                     sebzeler.append("PADDES")
#                 PADDES += int(input("Kaç kilo istersiniz ? "))
#                 donus = input("Başka bir isteğiniz var mı? (E/H)").upper()
#                 if donus == "E":
#                     continue
#                 else:
#                     break
#
#             elif sebze_secim == 5:
#                 if "SOGAN" not in sebzeler:
#                     sebzeler.append("SOGAN")
#                 SOGAN += int(input("Kaç kilo istersiniz ? "))
#                 donus = input("Başka bir isteğiniz var mı? (E/H)").upper()
#                 if donus == "E":
#                     continue
#                 else:
#                     break
#
#             elif sebze_secim == 6:
#                 break
#
#             else:
#                 print("Hatalı seçim yaptınız !")
#
#     elif secim == "Ç":
#         break
#     else:
#         print("Hatalı seçim !")
#

#ÖDEV Otomat sistemi
# Ürünler 'Kola','Fanta','Gazoz','Su'
# Fiyatlar 8.00,7.00,4.00,1.00
# 3 giriş hakkınız var şifre ile giriş olacak
# kaç ürün alınmış ise fiyat ve ürün listesi yazdırılacak



for i in range(3):
    giris =  int(input("Şifre"))

    if giris == 1:
        break
    else:
        continue
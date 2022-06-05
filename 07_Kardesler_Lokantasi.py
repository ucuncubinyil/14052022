masalar = { "Masa-1": "F", "Masa-2": "F", "Masa-3": "F", "Masa-4": "F", "Masa-5": "F" }
corbalar = { "1-Mercimek Çorbası": "7.00", "2-Ezogelin Çorbası": "7.00", "3-Yayla Çorbası": "6.00" }
baliklar = { "1-Mezgit": "27.00", "2-Plamut": "32.00", "3-Çupra": "40.00" }
etler = { "1-Pizola": "56.00", "2-Biftek": "65.00", "3-Lokum": "45.00" }
makarnalar = { "1- Bolanezli": "35.00", "2-Körili": "35.00", "3-Spagetti": "30.00" }
salatalar = { "1-Çoban": "25.00", "2-Sezar": "25.00", "3-Mevsim": "25.00" }
icecekler = { "1-Kola": "7.00", "2-Şalgam": "8.00", "3-Ayran": "7.00" }

siparisler = dict( )

while True:

    menu = int( input( """
        Sipariş Almak İçin      1
        Hesap Almak İçin        2
        Menü Güncelleme İçin    3
        Çıkış İçin              4
    Seçiniz:"""
                       )
                )

    if menu == 1:

        while True:
            print( """
             **************************************************
            *******KARDEŞLER ET LOKANTASINA HOŞGELDİNİZ*******
            **************************************************
            """
                   )

            kisi_sayisi = int( input( "Kaç Kişiyiz? " ) )

            musterimasasi = str( )

            for masa in masalar:
                if masalar[ masa ] == "F":
                    musterimasasi = masa
                    print( musterimasasi )
                    masalar[ masa ] = "T"
                    break

            siparis = dict( )

            for i in range( kisi_sayisi ):
                print( (i + 1), " . müsteri siparişi" )

                print( """
                    1- Çorba Çeşitleri
                    2- Balık Çeşitleri
                    3- Et Çeşitleri
                    4- Makarna Çeşitleri
                    5- Salata Çeşitleri
                    6- İçeçek Çeşitleri
                """
                       )

                secim = int( input( "Seçiminiz: " ) )

                if secim == 1:

                    for i in corbalar:
                        print( i, "\t\t:", corbalar[ i ] )

                    secim = int( input( "Çorba Seçiminiz: " ) )

                    if secim == 1:
                        siparis[ "Mercimek Çorbası" ] = "7.00"
                        cevap = input( "Başka bir arzunuz varmı? (E/H)" ).upper( )
                        if cevap == "E":
                            continue
                        else:
                            break
                    elif secim == 2:
                        siparis[ "Ezo Gelin Çorbası" ] = "7.00"
                    elif secim == 3:
                        siparis[ "Yayla Çorbası" ] = "6.00"
                    else:
                        print( "Hatalı Seçim" )

                elif secim == 2:
                    for i in baliklar:
                        print( i, "\t\t:", baliklar[ i ] )

                    secim = int( input( "Balık Seçimi" ) )

                    if secim == 1:
                        siparis[ "Mezgit" ] = "27.00"
                    elif secim == 2:
                        siparis[ "Palamut" ] = "32.00"
                    elif secim == 3:
                        siparis[ "Çupra" ] = "40.00"
                    else:
                        print("Hatalı Seçim")

    elif menu == 2:
        print("""
        *************************************
        **************HESAP BÖLÜMÜ***********
        """)

        for i in siparisler:
            print(i, "\t\t => ", siparisler[i])

        hesap = 0

        masahesabi = input("Hangi Masada Oturdunuz ?")

        for i in siparisler["Masa-"+masahesabi].values():
            hesap += float(i)

        print(hesap)

        odeme =  input("Hesap Ödendi Mi (E/H)").upper()
        if odeme == "E":
            masalar["Masa-"+masahesabi] = "F"

        for i in masalar:
            print(i, "\t\t:", masalar[i])

    elif menu == 3:
        pass

    elif menu == 4:
        break
    else:
        print("Hatalı giriş")


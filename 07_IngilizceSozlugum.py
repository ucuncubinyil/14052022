"""
# SORU: sözlük uygulaması olsun Tr-Eng
#       sözlük={"siyah":"black"...}
#       kullanıcı 4 seçenekli bir menü verelim
#          1-Arama
           2-Çıkarma
           3-Listeleme
           4-Çıkış

        Kullanıcı 1'e basarsa ->
            - Aranacak kelimeyi giriniz:
            - Bu kelime dict varsa english karşılığını yazılır.
            - Yoksa uygulamayı geliştirmek istermisiniz?
                - E ise bu kelimenin ingilizce karşılığını alırız ve sözlüğe eklenir.
                - H ise Peki..
        Kullanıcı 2'e basarsa ->
            - Çıkarılmak istenen kelime:
            - Kelime sözlükte varsa çıkartılır.
            - Yoksa uyarı verilir.
        Kullanıcı 3'e basarsa ->
            - Tum key value lar listenilir.
            - KEY -> VALUE
        Kullanıcı 4'e basarsa ->
            - Döngü sonlanır..
"""

sozluk = { "araştırma": "surver", "ummak": "expect", "dikkate almak": "consider" }
while True:

    print( "******************** TR-ENG SOZLUK**********" )
    secenekler = int( input( """
                
            1-Arama
            2-Çıkarma
            3-Listeleme
            4-Çıkış
    Seçiniz: """
                             )
                      )

    if secenekler == 1:
        kelime = input( "Aranacak kelimeyi giriniz :" )
        if kelime in sozluk:
            print( sozluk[ kelime ] )
        else:
            print( "Uygulamayı geliştirmek ister misiniz ?" )
            cevap = input( "E/H" ).upper( )

            if cevap == "E":
                kelimeing = input( kelime + " kelimesinin ingilizce karşılığını giriniz :" )
                sozluk[ kelime ] = kelimeing
            else:
                print("Peki...")

    elif secenekler == 2:
        silinecek_kelime =  input("Lütfen sözlükten silinecek kelimeyi giriniz : ")

        if silinecek_kelime in sozluk:
            del sozluk[silinecek_kelime]
            # sozluk.pop[silinecek_kelime]
        else:
            print("Bu kelime sözlükte yok")

    elif secenekler == 3:
        print(sozluk)

    elif secenekler == 4:
        print("Çıkılıyor ....")
        break
    else:
        print("Hatalı seçim")



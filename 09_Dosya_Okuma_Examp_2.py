##SORU: sinif.txt'de kayıtlı olan puan ad soyad
# bu sınıfın ortalamasını,en yüksek ve en düşük puanını
# ekrana yazdıran methodu kodlayınız.

def Oku( ):
    not_listesi = list( )
    dosya = open( "C:\\MEHMET\\2022-06-19\\sinif.txt", mode="r", encoding="utf-8" )
    liste = dosya.readlines( )
    print( liste )

    for i in liste:
        i = i.rstrip( "\n" )
        dd = i.split( " " )
        not_listesi.append( int( dd[ 0 ] ) )

    Ortalama = sum( not_listesi ) / len( not_listesi )
    MinimumPuan = min( not_listesi )
    MaximumPuan = max( not_listesi )

    print( f"""
            Sınıfın Not Ortalaması  :     {Ortalama}
            Sınıfın En Düşük Notu   :        {MinimumPuan}
            Sınıfın En Yüksek Notu  :        {MaximumPuan}
    """
           )


Oku( )

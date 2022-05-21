# ÖDEV: Kullanıcıdan isim,yaş,maaşve çocuk sayısı alalım
"""
    Eğer kullanıcının yaşı 45'in altındaysa;
        çocuk sayısına bakılacak ve çocuk sayısı 3^ten az ise çocuk başına 250₺,
         değilse çocuk başına 200₺ maaşa eklenecek
    Eğer kullanıcının yaşı 45 ve üzerinde ise:
        çocuk başına para verilmeyecek direk 500₺ maaşa eklenecek.

    Ekrana "Nesrin Yılmaz Maaşınız: 4000₺" yazılacak.
"""

name_surname = (input( "Please Enter Your Name and Surname: " ))
age = int( input( "Please Enter Your Age: " ) )
salary = float( input( "Please Enter Your Salary: " ) )
number_of_kids = int( input( "Please Enter How Many Children You Have: " ) )

# Checking the conditions for the extra money

if age < 45 and number_of_kids < 3:
    print( salary + (250 * number_of_kids) )
elif age < 45 and number_of_kids >= 3:
    print( salary + (200 * number_of_kids) )
else:
    print( salary + 500 )

# ÖDEV: Kullanıcı Gİriş Paneli Tasarlayınız.
"""
    Kullanıcıadı/Email ve şifre ile giriş sağlanacak
        Giriş Başarılı ise ekrana "Giriş Başarılı" yazsın
        Değilse
            Kullanıcıya kayıt olmak ister misiniz?
                Hayır ise PEKİ!!!
                Evet Kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı alarak kayıt yapalım.
                    şifre ve şifretekrarın aynı olması
"""

registered_username = "Sefa"
registered_password = "123"
registered_email = "sefabilsel@outlook.com"

username = input( "Please enter your Username or Email: " )
password = input( "Please enter your Password: " )

# Checking if username/email and password matches the registered user's info
# If the info isn't matching, asking to sign up

if (registered_username == username) or (registered_email == username):
    if registered_password == password:
        print( "Login Successful" )
else:
    control = input( "Login Failed! Would you like to register a new Account? Type Yes or No: " )
    if control == "No":
        print( "Okay, have a nice day." )
    elif control == "Yes":
        name = input( "Enter your Real Name: " )
        surname = input( "Enter your surname: " )
        email = input( "Enter your email: " )
        new_username = input( "Enter your Username: " )
        new_password = input( "Enter your password: " )
        password_confirmation = input( "Enter your password again: " )
        if password_confirmation == new_password:
            print( "Good job, account creation completed!" )
        else:
            print( "Passwords are not matching, please try again!" )

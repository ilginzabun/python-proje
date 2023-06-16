def mailcreate(nickname, mailtype=""):
    mailadresi = "@".join([nickname, mailtype])
    return mailadresi
#Bu kod, "mailcreate" adında bir fonksiyon tanımlar. Bu fonksiyon, bir kullanıcı adı (nickname) ve isteğe bağlı olarak bir mail tipi (mailtype) alır. 
#Varsayılan olarak mail tipi boştur.
#Fonksiyon, kullanıcı adı ve mail tipini birleştirerek bir mail adresi oluşturur ve bu mail adresini döndürür.

nickname = input("Please enter your username: ")
mail = input("Please enter the mail type: ")
if mail:
    print("Mail adresi:", mailcreate(nickname, mail))
else:
    print("Mail adresi:", mailcreate(nickname))
#Bu bölüm, kullanıcıdan bir kullanıcı adı (nickname) ve bir mail tipi (mail) girmesini ister. 
#Kullanıcı bir mail tipi girmişse, "mailcreate" fonksiyonunu kullanarak mail adresini oluşturur ve ekrana yazdırır.
#Kullanıcı bir mail tipi girmemişse, sadece kullanıcı adını kullanarak mail adresini oluşturur ve ekrana yazdırır.

response = input("Would you like to modify the email address? (Y/N): ")
if response.lower() == "y":
    new_mail = input("Please enter the new mail type: ")
    print("Modified mail adresi:", mailcreate(nickname, new_mail))
#Bu kısım, kullanıcıya mail adresini değiştirip değiştirmek istemediğini sorar. Kullanıcı "y" veya "Y" girerse,
#yeni bir mail tipi (new_mail) girmesini ister. 
#Ardından, "mailcreate" fonksiyonunu kullanarak yeni mail adresini oluşturur ve ekrana yazdırır.

check_mail = input("Please enter an email address to check: ")
if check_mail == mailcreate(nickname, mail):
    print("This email address is already in use.")
    print("Your email address has been created.")
#Bu bölüm, kullanıcının kontrol etmek istediği bir mail adresini girmesini ister. Eğer girdiği mail adresi, 
#kullanıcı adı ve mail tipinin birleştirilmesiyle oluşan mail adresine eşitse,
#ekrana "Bu mail adresi zaten kullanılıyor" mesajını ve "Mail adresiniz oluşturuldu" mesajını yazdırır.
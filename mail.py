import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def update_email(email):
    new_email = input("Lütfen yeni email adresinizi girin: ")
    if is_valid_email(new_email):
        print("email adresi başarıyla güncellendi!")
        return new_email
    else:
        print("Geçersiz email adresi. Güncelleme başarısız oldu.")
        return email

email = input("Lütfen email adresinizi girin: ")

if is_valid_email(email):
    print("Geçerli email adresi.")
else:
    raise ValueError("Geçersiz email adresi.")

response = input("email adresinizi güncellemek istiyor musunuz? (E/H): ")

if response.lower() == "e":
    email = update_email(email)

print("email adresiniz: ", email)

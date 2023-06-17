import re

class EmailValidator:
    def __init__(self):
        self.pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    def is_valid_email(self, email):
        return re.match(self.pattern, email) is not None

class EmailManager:
    def __init__(self):
        self.email_validator = EmailValidator()
        self.email = ""

    def get_email(self):
        email = input("Lütfen email adresinizi girin: ")
        if self.email_validator.is_valid_email(email):
            self.email = email
            print("Geçerli email adresi.")
        else:
            raise ValueError("Geçersiz email adresi.")

    def update_email(self):
        new_email = input("Lütfen yeni email adresinizi girin: ")
        if self.email_validator.is_valid_email(new_email):
            self.email = new_email
            print("email adresi başarıyla güncellendi!")
        else:
            print("Geçersiz email adresi. Güncelleme başarısız oldu.")

    def display_email(self):
        print(" email adresi:", self.email)

email_manager = EmailManager()
email_manager.get_email()

response = input("email adresinizi güncellemek istiyor musunuz? (Y/N): ")

if response.lower() == "e":
    email_manager.update_email()

email_manager.display_email()

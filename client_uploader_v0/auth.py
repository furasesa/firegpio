import pyrebase
import json
import configparser

"""
TODO:
1. Login
2. Set Database
"""

class Auth:
    def __init__(self):
        config = {
        "apiKey": "AIzaSyCIPc5qGH2ODWjR8Q2_qnG6pyw7OemhzDU",
        "authDomain": "furasesa.firebaseapp.com",
        "databaseURL": "https://furasesa.firebaseio.com/",
        "storageBucket": "furasesa.appspot.com",
        "serviceAccount": "goo_auth_service.json"
        }
        self.firebase = pyrebase.initialize_app(config)
        self.auth = self.firebase.auth()
        self.uid = 'BZsZUFBveYQ5kYzObw2oKOIhIbu2'

    def sign_in_with_token(self):
        print('sign in using token')
        custom_token = self.auth.create_custom_token(self.uid)
        self.user = self.auth.sign_in_with_custom_token(custom_token)
        # self.info = self.auth.get_account_info(self.user['idToken'])
        # print(self.i)
    def sign_in_with_email (self, email, password):
        print('sign in with email')
        self.user = self.auth.sign_in_with_email_and_password(email, password)
        self.info = self.auth.get_account_info(self.user['idToken'])
        # print(self.info)
    def get_database(self):
        self.db = self.firebase.database().child("raspberry")
        return self.db

if __name__ == "__main__":
    print("Nothing")
else :
    print("Auth v0.2.0 : calling Auth class")
    try:
        mauth = Auth().sign_in_with_token()
        # db = sign_in_with_token('BZsZUFBveYQ5kYzObw2oKOIhIbu2')
    except Exception:
        email = input("email :")
        passwd = input("password :")
        mauth = Auth().sign_in_with_email(email, passwd)


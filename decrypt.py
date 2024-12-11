import os
import pyaes

# Abre arquivo alvo
filename = input("Nome do arquivo alvo: ")
file = open(filename, 'rb')
data = file.read()
file.close()

# Key
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypted_data = aes.decrypt(data)

# Remove arquivo criptografado
os.remove(filename)

decrypted_file = filename.split('.rw')[0]
decrypted_file = open(f"{decrypted_file}", 'wb')
decrypted_file.write(decrypted_data)
decrypted_file.close()


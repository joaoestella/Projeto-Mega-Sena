import struct
import os

# Funcao para gerar 6 numeros e colocar na sequencia
def simulacao_real_mega_sena():
    numeros = set()
    while len(numeros) < 6:
        num = struct.unpack('I', os.urandom(4))[0]
        num = (num % 60) + 1
        numeros.add(num)
    return sorted(numeros)
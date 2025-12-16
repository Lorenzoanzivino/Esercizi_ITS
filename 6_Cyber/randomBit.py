import sys
import random

if len(sys.argv)<2:
    print("Usage: python randombit.py <file name>")
    sys.exit(1)

nomeFile = sys.argv[1]
data=None
with open(nomeFile, 'rb') as f:
    data = f.read()

# devo modificare un solo bit!!
# 1) scelgo il byte da modificare
pos = random.randint(0, len(data) - 1)
byte = data[pos]
# 2) scelgo il bit da modificare
bit = random.randint(0, 7)
# Supponiamo di aver scelto il bit 3, come
# faccio a modificare il bit 3 di byte?
byte ^= (1 << bit)
# 3) ricostruisco il byte modificato
data = data[:pos] + bytes([byte]) + data[pos + 1:]

with open(nomeFile, 'wb') as f:
    f.write(data)
print(f"Modified byte at position {pos}, bit {bit} in file {nomeFile}.")
sys.exit(0)
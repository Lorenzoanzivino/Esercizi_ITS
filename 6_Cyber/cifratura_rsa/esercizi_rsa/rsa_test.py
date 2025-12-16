# Riassunto “scheletro” dell’esercizio
# Generi la chiave → FAprivkey.pem
# Guardi i parametri con openssl rsa -text -noout
# Copi n, e, d dentro rsa_test.py
# In Python:
# Converti n e d con int(s,16)
# Converti msg con int.from_bytes(...)
# Cifri con pow(M,e,n)
# Decifri con pow(C,d,n)
# Riconverti con .to_bytes(...).decode("utf-8")

'''rsa_test.py
- Legge n_hex e d_hex da file (n_hex.txt, d_hex.txt) se presenti,
  altrimenti puoi incollare direttamente le stringhe in n_hex_inline/d_hex_inline.
- Legge e da e.txt se presente.
- Cifra e decifra un messaggio (supporta chunking se il messaggio è più lungo di n).
Non usa librerie esterne.'''

# rsa_test.py
# Esercizio: cifrare e decifrare con RSA a partire dai parametri n, e, d

# --- INCOLLA QUI I VALORI DAL keyinfo.txt ---
# MODULUS
n_hex = '''
00:ad:7f:3e:31:0b:f6:36:40:9b:c9:32:d2:3c:e6:
0c:02:89:74:62:2d:c0:0c:ae:ff:ff:0e:7d:d5:6f:
10:7c:0a:54:19:91:a3:20:5b:6f:c1:41:02:46:96:
08:4d:df:52:ce:39:bc:a3:43:ab:a8:5b:51:8b:90:
90:42:f5:89:a3:4f:5a:28:a2:78:70:eb:1f:b7:1f:
ba:62:d9:a6:49:c4:b5:31:82:0e:57:c6:8c:f5:28:
5e:a5:be:94:c6:91:5d:59:8c:75:12:5b:1d:83:e7:
aa:78:4e:7e:1c:2e:b6:f0:31:1c:ea:50:fa:a4:2f:
9b:a1:f9:92:51:47:5e:ac:57:73:2d:39:8f:cb:d9:
68:ee:f6:14:d8:f9:78:6b:41:46:98:ca:7c:35:b2:
ac:92:43:16:75:d8:30:91:e2:83:76:51:d1:cc:1f:
c3:84:0e:e3:a0:41:8f:b8:08:79:3f:8a:1e:37:0f:
f6:45:fd:5a:cd:80:c2:c0:1b:bd:78:ab:ef:d7:c4:
bc:f5:b7:41:0c:d5:a3:ef:40:58:be:c8:47:b9:0d:
54:c7:f0:93:ca:fe:a6:28:f4:c8:00:66:c4:38:55:
62:fe:a0:4c:49:56:e7:6e:18:6c:69:ea:e5:5a:b1:
58:f5:d3:9b:ba:a3:b4:87:95:ce:65:4b:c6:41:af:
23:51'''

# PRIVATEEXPONENT
d_hex = '''
 07:3a:a2:97:60:7f:97:98:06:7d:b7:73:6d:34:40:
80:1b:0f:84:17:3d:55:dc:9f:ff:f5:ef:e8:e4:a0:
af:d5:c3:81:10:bc:21:59:24:a8:0d:60:18:46:40:
58:93:f8:c8:97:bd:31:78:27:27:03:ce:10:7b:5b:
58:1f:90:66:cd:f9:17:06:c5:04:b4:76:a7:a1:52:
6e:c9:11:98:68:32:37:65:6b:43:a8:45:df:8c:59:
46:e7:f0:dd:9b:63:e3:bb:2f:8b:6e:76:90:29:a7:
1a:58:9a:96:81:f2:4a:02:0b:df:18:b5:1c:2c:a6:
7c:15:10:c3:62:f9:47:2e:3d:cd:65:a6:cd:e1:8d:
3a:9f:d2:23:7b:cb:7d:99:25:9d:3c:b5:e8:43:11:
22:be:4f:07:cb:0e:da:52:c2:ba:34:0c:c4:af:94:
a4:ff:40:0f:17:66:e4:7d:d1:b2:13:bf:10:8b:94:
34:83:79:6c:eb:67:b9:00:e8:1c:f2:dc:2e:11:d1:
6a:5f:97:a4:89:4b:83:c5:70:a3:0b:f6:77:21:6a:
83:6d:9e:a1:d8:16:78:1b:90:27:ef:5a:77:d1:9e:
19:20:a6:54:3c:b4:48:2f:f4:ce:72:6b:b5:b5:c2:
e9:43:79:60:be:f5:93:ad:a9:af:75:02:f7:f9:92:
eb'''

# PUBLICEXPONENT
e = 3

# Conversione da stringa hex a intero
def hex_to_int(s: str) -> int:
    return int(s.replace(" ", "").replace("\n", "").replace(":", ""), 16)

n = hex_to_int(n_hex)
d = hex_to_int(d_hex)

print("n =", n)
print("e =", e)
print("d =", d)

# --- Esempio: messaggio da cifrare ---
msg = "Ciao Lorenzo!"
print("\nMessaggio originale:", msg)

# Converti messaggio -> intero
M = int.from_bytes(msg.encode("utf-8"), "big")
print("Messaggio come intero:", M)

# Cifratura
C = pow(M, e, n)
print("Cifrato:", C)

# Decifratura
M2 = pow(C, d, n)
M2_bytes = M2.to_bytes((M2.bit_length() + 7) // 8, "big")
print("Decifrato:", M2_bytes.decode("utf-8"))

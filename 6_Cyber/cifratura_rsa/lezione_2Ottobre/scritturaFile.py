
n:int = 3512
with open("/home/its/vscode_projects/Esercizi_ITS/8_Cyber/cifratura_rsa/lezione_2Ottobre/numero1.dat", "wb") as f:
    f.write(n.to_bytes(4, byteorder="little"))

with open("/home/its/vscode_projects/Esercizi_ITS/8_Cyber/cifratura_rsa/lezione_2Ottobre/numero2.dat", "wb") as f:
    f.write(n.to_bytes(4, byteorder="big"))

s:str = "Ciao"
with open("/home/its/vscode_projects/Esercizi_ITS/8_Cyber/cifratura_rsa/lezione_2Ottobre/numero3.dat", "w") as f:
    f.write(s)


def s2n(s):
    tot = 0
    esp = 0
    for c in s[::-1]:
        tot = tot + 256 ** esp * ord(c)
        esp += 1
    return tot

print(s2n("Ciao"))

def s2ne(s):
    tot = 0
    for c in s:
        tot = (tot << 8) | ord(c)
    return tot

print(s2ne("Ciao"))    

'''-----------------------------------------------------------------'''
n=994395838479439358596594838383930
p=84857392029283847757585

a=1231231
b=312312312

print(pow(pow(p,a,n),b,n)) 
print(pow(pow(p,b,n),a,n))
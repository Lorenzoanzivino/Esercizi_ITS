n:int = 3512

with open("/home/its/vscode_projects/Esercizi_ITS/8_Sicurezza2/write_binary/numero1.dat", "wb") as f:
    f.write(n.to_bytes(4, byteorder="little"))

#     # xxd /home/its/vscode_projects/programmi_esercizi/Cyber/write_binary/numero1.dat
#     # 00000000: b80d 0000                             ....
#     # da sinistra a destra

with open("/home/its/vscode_projects/Esercizi_ITS/8_Sicurezza2/write_binary/numero2.dat", "wb") as f:
    f.write(n.to_bytes(4, byteorder="big"))

    # xxd /home/its/vscode_projects/programmi_esercizi/Cyber/write_binary/numero2.dat
    # 00000000: 0000 0db8                               ....
    # da destra a sinistra


s:str = 'Ciao'

with open('/home/its/vscode_projects/Esercizi_ITS/8_Sicurezza2/write_binary/numero3.dat', 'w') as f:
    f.write(s)

    # xxd /home/its/vscode_projects/programmi_esercizi/Cyber/write_binary/numero3.dat
    # 00000000: 4369 616f                                Ciao

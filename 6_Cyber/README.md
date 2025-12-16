# 🔐 RSA & OpenSSL Cheat Sheet

## 1️⃣ Cos’è RSA?

RSA è un **algoritmo di crittografia asimmetrica**, che utilizza due chiavi distinte:

- **Chiave pubblica (e, n)** → per **cifrare** i messaggi.  
- **Chiave privata (d, n)** → per **decifrare** i messaggi.  

### Caratteristiche principali
- Sicuro grazie alla difficoltà di fattorizzare numeri grandi.  
- Usato in email sicure, HTTPS, firme digitali, autenticazione.  
- Operazioni principali:  
  - Cifratura: `C = M^e mod n`  
  - Decifratura: `M = C^d mod n`

---

## 2️⃣ Generare chiavi RSA con OpenSSL

### ✅ Generare una chiave privata
    ```bash
    openssl genpkey -algorithm RSA -out privkey.pem -pkeyopt rsa_keygen_bits:2048
    • 2048 = lunghezza chiave (bit)
    • Output: privkey.pem (chiave privata)

✅ Estrarre la chiave pubblica
    openssl rsa -pubout -in privkey.pem -out pubkey.pem
    • Output: pubkey.pem (chiave pubblica)

✅ Mostrare i parametri della chiave
    openssl rsa -text -noout -in privkey.pem
    •  Mostra modulus (n), publicExponent (e), privateExponent (d) e altri valori interni

3️⃣ Convertire parametri RSA in Python
    # Conversione da esadecimale -> intero
    n = int(n_hex.replace(":", "").replace("\n", ""), 16)
    d = int(d_hex.replace(":", "").replace("\n", ""), 16)
    e = 3  # valore indicato da OpenSSL

# Cifratura e decifratura
    C = pow(M, e, n)   # cifratura
    M2 = pow(C, d, n)  # decifratura

4️⃣ Cosa fa RSA?
    Cifratura: proteggere messaggi sensibili
    Decifratura: recuperare il messaggio originale
    Autenticazione: firmare messaggi digitalmente per provare l’identità
    Integrità: verificare che il messaggio non sia stato modificato

5️⃣ Comandi OpenSSL rapidi
    Comando	                                                                                    Scopo
    openssl genpkey -algorithm RSA -out privkey.pem -pkeyopt rsa_keygen_bits:2048	            Genera chiave privata
    openssl rsa -pubout -in privkey.pem -out pubkey.pem	                                        Estrae chiave pubblica
    openssl rsa -text -noout -in privkey.pem	                                                Mostra parametri chiave
    openssl rsa -in privkey.pem -check	                                                        Controlla correttezza chiave
    openssl rsautl -encrypt -pubin -inkey pubkey.pem -in msg.txt -out msg.enc	                Cifra file con RSA
    openssl rsautl -decrypt -inkey privkey.pem -in msg.enc -out msg.txt	                        Decifra file RSA

6️⃣ Suggerimenti pratici
    Non condividere mai la chiave privata
    RSA è indicato per messaggi più piccoli del modulo; per testi lunghi usare RSA + AES
    In Python puoi fare tutto senza librerie usando:
    int.from_bytes(...) → stringa → intero
    int.to_bytes(...) → intero → stringa
    pow(M, e, n) → cifratura/decifratura

📌 In breve: RSA protegge i dati tramite due chiavi separate. OpenSSL permette di generarle, visualizzare i parametri e testarle. In Python puoi replicare tutte le operazioni direttamente con numeri interi.
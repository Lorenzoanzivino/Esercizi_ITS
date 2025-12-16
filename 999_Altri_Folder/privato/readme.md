# 🔐 Archivio Credenziali – Guida Completa

Questo documento ti spiega come creare, organizzare e mettere al sicuro il tuo file delle credenziali dentro uno ZIP cifrato AES-256.

---

## 📑 Sommario

- [🔐 OBIETTIVO](#-obiettivo)
- [1️⃣ CREA IL FILE DI TESTO (in chiaro)](#1️⃣-crea-il-file-di-testo-in-chiaro)
- [2️⃣ CREA LO ZIP CIFRATO (AES-256)](#2️⃣-crea-lo-zip-cifrato-aes-256)  
  - [✔️ Linux / Mac (terminale)](#️-linux--mac-terminale)
- [3️⃣ CONSERVAZIONE (come fare il backup serio)](#3️⃣-conservazione-come-fare-il-backup-serio)
- [4️⃣ COME APRIRLO DAL TELEFONO](#4️⃣-come-aprirlo-dal-telefono)
- [5️⃣ LA COSA PIÙ IMPORTANTE](#5️⃣-la-cosa-più-importante)
- [📘 LIBRO PERSONALE DELLE CREDENZIALI](#libro-personale-delle-credenziali)
- [📌 Checklist rapida](#-checklist-rapida-copiala-alla-fine-del-file-se-vuoi)
- [📦 STRUTTURA DEL TUO ARCHIVIO ZIP](#-struttura-del-tuo-archivio-zip-aes-256)

---

## 🔐 OBIETTIVO

Creare UN file .txt con tutte le tue credenziali →
Metterlo dentro UN archivio .zip cifrato AES-256 →
Conservarlo dove ti pare (PC, telefono, cloud) senza rischiare nulla.

[🔝 Torna su](#-sommario)

---

### 1️⃣ CREA IL FILE DI TESTO (in chiaro)

Fai un file chiamato ad esempio:
```bash
credenziali.txt
```

Strutturalo così (semplice, leggibile):
```bash
=====================
  ACCOUNT PERSONALI
=====================

Gmail
user: lorenzo@example.com
pass: '**************'

Instagram
user: lorenzo.ig
pass: '**************'

=====================
  SERVIZI FINANZIARI
=====================

Banca XYZ
user: lorenzo
pass: '**************'

Carta di credito PIN: '****'
```
Metti ciò che vuoi, è il tuo “quaderno digitale”.

[🔝 Torna su](#-sommario)

---

### 2️⃣ CREA LO ZIP CIFRATO (AES-256)
✔️ Metodo universale (7-Zip — super consigliato)
Windows

- Installa 7-Zip (gratis, open source).

- Tasto destro su credenziali.txt

- 7-Zip → Aggiungi ad archivio…

- Imposta:

    - Formato archivio: zip

    - Metodo cifratura: AES-256

    - Inserisci la password

    - Spunta: “Cifrare nomi file” (importantissimo!)

Clicca OK → otterrai:
```bash
credenziali.zip
```

---

### ✔️ Linux / Mac (terminale)
```bash
zip -e credenziali.zip credenziali.txt
```
⚠️ Nota: zip -e usa cifratura “tradizionale”, non AES.
Per AES-256 devi usare 7z anche su Linux/Mac:
```bash
7z a -tzip credenziali.zip credenziali.txt -mem=AES256
```

[🔝 Torna su](#-sommario)

---

### 3️⃣ CONSERVAZIONE (come fare il backup serio)

Hai 3 posti dove metterlo:

#### ✔️ 1. PC (copia principale)

credenziali.zip sempre aggiornato.

#### ✔️ 2. Chiavetta USB

Una copia di sicurezza.
Se perdi la password → fine, non si apre.

#### ✔️ 3. Cloud (opzionale ma comodo)

Puoi caricare solo il file ZIP cifrato, MAI il txt in chiaro.

Posti sicuri:

  - Google Drive
  - Dropbox
  - OneDrive
  - Mega

Se qualcuno lo ruba → non apre nulla senza password.

[🔝 Torna su](#-sommario)

---

### 4️⃣ COME APRIRLO DAL TELEFONO
Android
Installa:
- ZArchiver
- oppure 7Zipper

Apri → selezioni → inserisci la password → apri il .txt.

iPhone
App consigliata:
- iZip
- Zip & RAR File Extractor

[🔝 Torna su](#-sommario)

---

### 5️⃣ LA COSA PIÙ IMPORTANTE

🔴 La password del tuo ZIP deve essere lunga e NON riutilizzata.
Altrimenti vanifichi tutto.

Esempio buono (da ricordare a memoria):
```bash
Pippo!2024@FarfallaRossa
```
Esempio pessimo:
```bash
123456
lorenzo
password
```

[🔝 Torna su](#-sommario)

---

### LIBRO PERSONALE DELLE CREDENZIALI
```bash
============================================================
                LIBRO PERSONALE DELLE CREDENZIALI
               (Conservare SOLO in archivio cifrato)
============================================================

Ultimo aggiornamento: ________________________


=====================
=  SEZIONE: SOCIAL  =
=====================

GMAIL
  Email: _______________________
  Username: ____________________
  Password: ____________________
  Note: _________________________

INSTAGRAM
  Username: ____________________
  Password: ____________________
  Email recupero: ______________
  Note: _________________________

FACEBOOK
  Email/Username: ______________
  Password: ____________________
  Note: _________________________


==========================
=  SEZIONE: FINANZE      =
==========================

CONTO CORRENTE / BANCA
  Istituto: ____________________
  Username: ____________________
  Password: ____________________
  PIN App: _____________________
  Note: _________________________

CARTA DI CREDITO / DEBITO
  Banca: _______________________
  Numero carta: ________________
  PIN: __________________________
  Password area cliente: _______
  Note: _________________________

PAYPAL
  Email: _______________________
  Password: ____________________
  Note: _________________________


=============================
=  SEZIONE: DISPOSITIVI     =
=============================

PC PRINCIPALE
  Sistema: _____________________
  Utente: ______________________
  Password: ____________________

SMARTPHONE
  Marca/Modello: _______________
  PIN: __________________________
  Password sblocco (se diversa): 
  ______________________________
  Note: _________________________

WIFI CASA
  Nome rete (SSID): ____________
  Password: ____________________
  Note: _________________________


==============================
=  SEZIONE: ACCOUNT VARI     =
==============================

SPOTIFY
  Email: _______________________
  Password: ____________________
  Note: _________________________

NETFLIX
  Email: _______________________
  Password: ____________________
  PIN profilo: _________________
  Note: _________________________

AMAZON
  Email: _______________________
  Password: ____________________
  Note: _________________________


===================================
=  SEZIONE: CODICI E RECUPERI     =
===================================

CODICI 2FA DI RECUPERO
  Servizio: _____________________
  Codici backup:
    - ___________________________
    - ___________________________
    - ___________________________
    - ___________________________
    - ___________________________

CHIAVI DI RIPRISTINO
  Servizio: _____________________
  Chiave: _______________________
  Note: _________________________


===============================
=  NOTE PERSONALI IMPORTANTI  =
===============================
(Annotazioni, informazioni di sicurezza, procedure personali)

_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________


============================================================
              FINE DEL FILE – CONSERVARE IN SICUREZZA
============================================================
```

[🔝 Torna su](#-sommario)

---

### 📌 Checklist rapida (copiala alla fine del file se vuoi)
```bash
[ ] Il file è salvato SOLO in un archivio zip AES-256
[ ] Il file in chiaro NON è più sul desktop o in giro
[ ] Password dell’archivio lunga e non riutilizzata
[ ] Copia dell’archivio su chiavetta USB
[ ] Eventuale copia cloud (solo archivio cifrato)
[ ] Ultimo controllo credenziali effettuato il: ___________
```

[🔝 Torna su](#-sommario)

---

### 📦 STRUTTURA DEL TUO ARCHIVIO ZIP (AES-256)
```bash
credenziali.zip   ← archivio cifrato con password robusta (AES-256)
│
└── Libro_Credenziali.txt   ← il tuo file principale (compilato da te)
```

[🔝 Torna su](#-sommario)

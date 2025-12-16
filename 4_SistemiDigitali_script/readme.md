# 💻 Corso Sistemi Digitali

Questa directory raccoglie tutti i materiali relativi allo **studio dei Sistemi Digitali e dei Fondamenti di Reti e Sistemi Operativi**, suddivisi in più lezioni.  

L’obiettivo è passare dalla conoscenza dei componenti hardware, software e sistemi operativi, fino allo sviluppo di competenze sulla rete, protocolli e gestione delle informazioni nei sistemi digitali.

---

## 📁 Struttura della cartella

### 🔹 `Lezioni 1-6` — Fondamenti Hardware e Sistemi Operativi
Questa fase introduce l’architettura di un computer, la memoria, la CPU, i dispositivi di I/O e i concetti base di sistema operativo.

**Contenuti principali:**
- **Componenti hardware**
  - CPU (ALU, Control Unit, Registri)
  - RAM (Heap, Stack, DRAM, SRAM)
  - Memoria secondaria (HDD, SSD)
- **Sistema operativo**
  - Funzioni principali, kernel (monolitico vs microkernel)
- **Comandi base del sistema operativo**
  - `ls`, `cd`, `mkdir`, `touch`, `rm`
- **Struttura standard di progetto**
  - Cartelle `src`, `tests`, file `README.md`, `.gitignore`, `requirements.txt`

**Obiettivo:**  
Conoscere i componenti hardware di base, il funzionamento del sistema operativo e i comandi principali per la gestione dei file e delle directory.

---

### 🔹 `Lezioni 7-10` — Reti di Calcolatori e Gestione delle Informazioni
Questa fase introduce le reti di calcolatori, protocolli, DBMS e rappresentazioni dei dati.

**Contenuti principali:**
- **Reti di Calcolatori**
  - Tipi di reti: cablate, wireless
  - Comunicazione: point-to-point, broadcast
  - Topologie: ad albero, maglia completa
  - Modelli: Client-Server e Peer-to-Peer
  - Classificazione: LAN, MAN, WAN
- **Gestione delle informazioni**
  - DBMS, query, inserimento, aggiornamento, eliminazione dati
- **Codici**
  - Binario, ASCII
- **Dimensioni dei dati**
  - bit, byte, word, bitrate
- **Proprietà e conversioni**
  - Binario-decimale, decimale-binario, addizione e sottrazione binaria
- **Algebra Booleana**
  - Progettazione e ottimizzazione di circuiti digitali
- **Modello di Von Neumann**
  - Memoria condivisa, fetch, execution cycle

**Obiettivo:**  
Comprendere i fondamenti delle reti, la gestione dei dati e la rappresentazione digitale delle informazioni.

---

### 🔹 `Lezioni 11-12` — Architettura Von Neumann, Firmware, OS e Livelli di Rete
Questa fase approfondisce CPU, memoria, I/O, firmware, BIOS/UEFI, driver, sistemi operativi e primi livelli di rete.

**Contenuti principali:**
- **Modello di Von Neumann**
  - CPU, memoria, dispositivi I/O, bus di sistema
  - Ciclo istruzione: FETCH → DECODE → EXECUTE
  - Registri MDR e MAR
  - Operazioni di lettura e scrittura
- **Dispositivi di Input/Output**
  - Tipologie, funzionamento, esempi
- **Firmware e BIOS/UEFI**
  - BIOS: bootstrap, POST, MBR
  - UEFI: GUI, Secure Boot, Boot Manager, GPT
- **Driver**
  - Funzione e aggiornamenti
- **Sistemi Operativi**
  - Tipi, classificazione, interazione con hardware e utenti
- **Modello ISO/OSI**
  - Livelli: Fisico, Data Link
  - Architettura di rete
  - Trasmissione dati, Wi-Fi e Bluetooth
  - Controllo flusso, MAC, LLC, switch

**Obiettivo:**  
Saper descrivere l’architettura di un computer, firmware, BIOS/UEFI, driver, OS e comprendere i primi livelli di rete.

---

### 🔹 `Lezioni 16-17` — Livelli Rete Avanzati e Funzioni del Sistema Operativo
Questa fase approfondisce i livelli superiori del modello ISO/OSI e i servizi e funzioni principali di un sistema operativo.

**Contenuti principali:**
- **Livello di Rete**
  - Routing, Forwarding, Indirizzamento logico, NAT
- **Livello di Trasporto**
  - Segmentazione, controllo errori e connessione end-to-end
- **Socket**
  - Indirizzo IP + porta per identificare comunicazioni
- **Livello di Sessione**
  - Gestione sessioni, half/full duplex
- **Livello di Presentazione**
  - Traduzione dati, crittografia, compressione
- **Livello Applicazione**
  - Servizi di rete per applicazioni: file transfer, email, login remoto
- **Servizi OS**
  - Gestione processi (stati, fork, exec, signal, deadlock)
  - Gestione memoria principale e virtuale
  - Gestione file system e dispositivi periferici
  - Gerarchia della memoria: registri → cache → RAM → dischi → dispositivi rimovibili
  - Protezione e sicurezza: autenticazione, autorizzazione
  - Interfacce utente: terminale, GUI, HCI

**Obiettivo:**  
Conoscere il funzionamento completo dei livelli di rete, gestione dei processi e memoria, e dei servizi offerti dal sistema operativo.

---

## 🧠 Competenze acquisite

- Comprensione dell’**architettura dei computer**: CPU, RAM, memoria secondaria, I/O
- Conoscenza dei **firmware** e del BIOS/UEFI
- Gestione e funzionamento dei **sistemi operativi**
- Comandi base del terminale e struttura dei progetti
- Fondamenti delle **reti di calcolatori**, protocolli e modelli ISO/OSI
- **Gestione della memoria**, processi, paging e file system
- Funzionamento dei **driver e periferiche**
- Comprensione dei livelli di rete, trasporto, sessione, presentazione e applicazione
- Conversioni binario-decimale, algebra booleana e progettazione di sistemi digitali

---

## ⚙️ Strumenti e consigli

- Editor consigliato: **Visual Studio Code**, **PyCharm**
- Utilizzo di terminale/console per comandi OS
- Simulatori per reti e architettura Von Neumann
- Software di visualizzazione diagrammi di rete e flusso dati
- Debugging di sistemi e monitoraggio processi tramite OS

---

## 👨‍💻 Autore
**Lorenzo Anzivino**  
Studente ITS – Corso Application Cloud Developer  
Appassionato di Sistemi Digitali, Reti, Architettura di Computer e Sistemi Operativi.

---

## 🧩 Note finali
La cartella contiene **appunti completi di Sistemi Digitali**, diagrammi, esempi pratici e spiegazioni dettagliate.  
Tutti i materiali sono pensati come **guida completa** per lo studio, la pratica e la comprensione dei sistemi digitali dai fondamenti fino alla gestione di reti e OS avanzati.

# Manuale di Installazione e Avvio - Sistema Gestione Distribuzione Acqua

## Prerequisiti del Sistema

### Software Richiesto
- **Python 3.8 o superiore**
- **Git** per il controllo versione
- **Browser web** moderno (Chrome, Firefox, Safari, Edge)
- **Connessione internet** per il download

### Verifica Installazioni Esistenti

#### Controllo Python
Aprire il Prompt dei Comandi (cmd) premendo `Win + R`, digitare `cmd` e premere Invio.
Digitare:
```cmd
python --version
```

Se non funziona, provare:
```cmd
python3 --version
```

**Risultato atteso**: Visualizzazione versione Python 3.8 o superiore (es: `Python 3.11.0`)

#### Controllo Git
Nel Prompt dei Comandi digitare:
```cmd
git --version
```

**Risultato atteso**: Visualizzazione versione Git (es: `git version 2.40.0`)

### Installazione Python (se necessario)

#### Download e Installazione
1. Andare su https://www.python.org/downloads/
2. Cliccare "Download Python" (versione più recente)
3. Eseguire il file scaricato
4. **IMPORTANTE**: Spuntare "Add Python to PATH" durante l'installazione
5. Selezionare "Install Now"
6. Attendere completamento installazione
7. Riavviare il computer

#### Verifica Post-Installazione
Riaprire il Prompt dei Comandi e ripetere:
```cmd
python --version
```

### Installazione Git (se necessario)

#### Download e Installazione
1. Andare su https://git-scm.com/download/win
2. Scaricare la versione appropriata (32-bit o 64-bit)
3. Eseguire il file scaricato
4. Seguire installazione guidata (lasciare impostazioni predefinite)
5. Riavviare il computer

#### Verifica Post-Installazione
Riaprire il Prompt dei Comandi e digitare:
```cmd
git --version
```

## Download e Configurazione Progetto

### 1. Creazione Cartella di Lavoro
Aprire il Prompt dei Comandi (cmd) premendo `Win + R`,digitare `cmd` e premere Invio. Poi scrivere:
```cmd
cd Desktop
mkdir progetto_django
cd progetto_django
```

### 2. Clonazione Repository da GitHub
Digitare il comando seguente (tutto su una riga):
```cmd
git clone https://github.com/Lucabrg10/una_acies_2.git
```

### 3. Navigazione nella Cartella Progetto
```cmd
cd una_acies_2
```


## Avvio del Progetto

### Metodo 1: Utilizzo File Batch (Consigliato)

#### Esecuzione File BAT
Eseguire il file batch:
```cmd
start_project.bat
```

#### Accesso all'Applicazione
1. Il file batch mostrerà un link (tipicamente `http://127.0.0.1:8000`)
2. Copiare il link mostrato
3. Aprire il browser web
4. Incollare il link nella barra indirizzi
5. Premere Invio


### Metodo 2: Procedura Manuale

#### Installazione Django
Nella cartella `progetto_2_una_acies`, digitare:
```cmd
pip install django
```

Se non funziona:
```cmd
pip3 install django
```

#### Configurazione Database
```cmd
python manage.py migrate
```

#### Avvio Server
```cmd
python manage.py runserver
```

#### Accesso Browser
- Aprire browser web
- Digitare: `http://127.0.0.1:8000`
- Premere Invio

## Risoluzione Problemi Comuni

### Errori di Download GitHub

#### "git: command not found"
**Causa**: Git non installato o non nel PATH
**Soluzione**:
1. Reinstallare Git seguendo procedura precedente
2. Riavviare computer
3. Riprovare comando clone

#### "Repository not found"
**Causa**: URL errato o connessione internet
**Soluzione**:
1. Verificare connessione internet
2. Ricopiare esattamente l'URL: `https://github.com/Lucabrg10/una_acies_2.git`
3. Riprovare download

#### "Permission denied"
**Causa**: Cartella protetta o antivirus
**Soluzione**:
1. Cambiare cartella di destinazione:
```cmd
cd C:\Users\%USERNAME%\Documents
mkdir progetti
cd progetti
```
2. Riprovare clone
3. Temporaneamente disabilitare antivirus

### Errori Python/Django

#### "python: command not found"
**Causa**: Python non installato o non nel PATH
**Soluzione**:
1. Reinstallare Python spuntando "Add to PATH"
2. Riavviare computer
3. Riprovare comandi

#### "pip: command not found"
**Causa**: pip non installato con Python
**Soluzione**:
1. Utilizzare `python -m pip` invece di `pip`:
```cmd
python -m pip install django
```

#### "Django not found"
**Causa**: Django non installato correttamente
**Soluzione**:
1. Reinstallare Django:
```cmd
pip uninstall django
pip install django
```

#### "Port already in use"
**Causa**: Server già attivo su porta 8000
**Soluzione**:
1. Terminare processi Python esistenti (Ctrl+C)
2. Utilizzare porta alternativa:
```cmd
python manage.py runserver 8001
```
3. Accedere con `http://127.0.0.1:8001`

### Errori di Database

#### "Database locked"
**Causa**: File database in uso
**Soluzione**:
1. Chiudere tutte le finestre browser
2. Terminare server (Ctrl+C)
3. Attendere 10 secondi
4. Riavviare server

#### "Migration errors"
**Causa**: Database non sincronizzato
**Soluzione**:
```cmd
python manage.py makemigrations
python manage.py migrate --run-syncdb
```

### Errori del File BAT

#### "File not found"
**Causa**: Posizione errata o file mancante
**Soluzione**:
1. Verificare di essere nella cartella `una_acies_2`
2. Verificare presenza file con:
```cmd
dir start_project.bat
```
3. Se mancante, utilizzare metodo manuale

#### "Access denied"
**Causa**: Permessi insufficienti
**Soluzione**:
1. Eseguire Prompt dei Comandi come Amministratore
2. Navigare nella cartella progetto
3. Riprovare esecuzione


## Aggiornamenti e Manutenzione

### Ripristino in Caso di Problemi
Se il sistema non funziona più:
1. Eliminare cartella `una_acies_2`
2. Ripetere procedura completa di download
3. Il database verrà ricreato automaticamente

---

**Nota Importante**: Mantenere sempre il Prompt dei Comandi aperto durante l'utilizzo del sistema. La chiusura interromperà il server e renderà inaccessibile l'applicazione.
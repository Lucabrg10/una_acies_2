### Manuale di Installazione e Avvio - Distribuzione acqua - UNA ACIES

## Prerequisiti del Sistema

#### Software Richiesto
- **Python 3.8 o superiore**
- **Git** per il controllo versione
- **Browser web** moderno (Chrome, Firefox, Safari, Edge)
- **Connessione internet** per il download


[Verifica Installazioni Esistenti](#verifica-installazioni-esistenti)

## Download e configurazione del progetto

#### 1. Creazione cartella di lavoro
Aprire il Prompt dei Comandi (cmd) premendo `Win + R`, digitare `cmd` e premere Invio. Poi scrivere:
```cmd
cd Desktop
mkdir progetto_django
cd progetto_django
```

#### 2. Clonazione repository da GitHub
Digitare il seguente comando:
```cmd
git clone https://github.com/Lucabrg10/una_acies_2.git
```
Navigare nella cartella:
```cmd
cd una_acies_2
```
## Avvio del Progetto

### Metodo 1: Utilizzo file batch (Consigliato)

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
---
### Metodo 2: Procedura Manuale

#### Installazione Django
Digitare il seguente comando sul terminale:
```cmd
cd progetto_2_una_acies
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
---
### Risoluzione Problemi Comuni

#### 1. "Port already in use"
**Causa**: Server già attivo su porta 8000
**Soluzione**:
1. Terminare processi Python esistenti (Ctrl+C)
2. Utilizzare porta alternativa:
```cmd
python manage.py runserver 8001
```
3. Accedere con `http://127.0.0.1:8001`


#### 2. "Database locked"
**Causa**: File database in uso
**Soluzione**:
1. Chiudere tutte le finestre browser
2. Terminare server (Ctrl+C)
3. Attendere 10 secondi
4. Riavviare server


#### 3. "File not found"
**Causa**: Posizione errata o file bat mancante
**Soluzione**:
1. Verificare di essere nella cartella `una_acies_2`
2. Verificare presenza file con:
```cmd
dir start_project.bat
```
3. Se mancante, utilizzare metodo manuale

#### 4. "Access denied"
**Causa**: Permessi insufficienti
**Soluzione**:
1. Eseguire Prompt dei Comandi come Amministratore
2. Navigare nella cartella progetto
3. Riprovare esecuzione

### Verifica Installazioni Esistenti
#### Controllo Python
Aprire il Prompt dei Comandi (cmd) premendo `Win + R`, digitare `cmd` e premere Invio.
Digitare:
```cmd
python --version
```

**Risultato atteso**: Visualizzazione versione Python 3.8 o superiore (es: `Python 3.11.0`). Se viene visualizzato: 'python' non è riconosciuto come comando interno o esterno, seguire l'installazione qui sotto.
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
---
#### Controllo Git
Nel Prompt dei Comandi digitare:
```cmd
git --version
```

**Risultato atteso**: Visualizzazione versione Git (es: `git version 2.40.0`). Altrimenti seguire installazione qui sotto.
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

## Ripristino in Caso di Problemi
Se il sistema non funziona più:
1. Eliminare cartella `una_acies_2`
2. Ripetere procedura completa di download
3. Il database verrà ricreato automaticamente

---

**Nota Importante**: Mantenere sempre il Prompt dei Comandi aperto durante l'utilizzo del sistema. La chiusura interromperà il server e renderà inaccessibile l'applicazione.
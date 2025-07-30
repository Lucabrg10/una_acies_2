@echo off
echo Avvio configurazione del progetto Django...
cd .

REM Crea la virtualenv
python -m venv venv

REM Attiva la virtualenv
call venv\Scripts\activate.bat

REM Installa Django (e altre dipendenze se presenti in requirements.txt)
IF EXIST requirements.txt (
    pip install -r requirements.txt
) ELSE (
    pip install django
)

REM Avvia il server
cd ./progetto_2_una_acies
python manage.py runserver
pause

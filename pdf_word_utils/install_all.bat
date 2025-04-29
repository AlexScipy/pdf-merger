@echo off
setlocal ENABLEDELAYEDEXPANSION

echo =============================================
echo   PDF TOOLKIT - Setup automatico
echo =============================================

REM Verifica se Python è installato
where python >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Python non trovato. Scarico Python 3.10...
    curl -o python-installer.exe https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_tcltk=1
    del python-installer.exe
) ELSE (
    echo Python è già installato.
)

REM Forza aggiornamento pip
python -m ensurepip --upgrade
python -m pip install --upgrade pip

REM Installa le librerie necessarie
IF EXIST requirements.txt (
    echo Installazione dipendenze da requirements.txt...
    pip install -r requirements.txt
) ELSE (
    echo ERRORE: requirements.txt non trovato!
    pause
    exit /b
)

echo ---------------------------------------------
echo Ambiente pronto.
echo Puoi ora eseguire:
echo    - pdf_to_word_gui.exe  (conversione PDF -> Word)
echo    - sostituisci_pagina.py (sostituzione pagine PDF)
echo ---------------------------------------------

pause

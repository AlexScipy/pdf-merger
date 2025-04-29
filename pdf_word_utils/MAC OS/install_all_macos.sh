#!/bin/bash

echo "=============================================="
echo "   PDF TOOLKIT - Installazione per macOS"
echo "=============================================="

# Controllo Homebrew
if ! command -v brew &> /dev/null; then
    echo "Homebrew non trovato. Vuoi installarlo? [s/N]"
    read install_brew
    if [[ "$install_brew" == "s" || "$install_brew" == "S" ]]; then
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    else
        echo "Interrotto. Homebrew è richiesto per installare Python."
        exit 1
    fi
fi

# Controllo Python 3.10+
if ! command -v python3 &> /dev/null; then
    echo "Installo Python 3..."
    brew install python@3.10
else
    version=$(python3 --version | cut -d " " -f 2)
    echo "Python $version rilevato"
fi

# Crea virtualenv opzionale
# python3 -m venv venv
# source venv/bin/activate

# Aggiorna pip
python3 -m pip install --upgrade pip

# Installa le librerie necessarie
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
else
    echo "ERRORE: requirements.txt non trovato!"
    exit 1
fi

echo "-----------------------------------------------"
echo " Ambiente pronto per eseguire gli script:"
echo "   - pdf_to_word_gui.py"
echo "   - sostituisci_pagina.py"
echo "-----------------------------------------------"

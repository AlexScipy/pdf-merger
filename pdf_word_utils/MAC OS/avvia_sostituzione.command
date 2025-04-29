#!/bin/bash
echo "Sto avviando lo strumento di sostituzione pagina..."
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
python3 sostituisci_foglio.py

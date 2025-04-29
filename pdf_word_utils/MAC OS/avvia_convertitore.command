#!/bin/bash
echo "Sto avviando il convertitore PDF -> Word..."
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
python3 pdf_to_word.py

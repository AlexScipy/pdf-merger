import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter
import os

def select_pdf_and_convert():
    tk.Tk().withdraw()
    pdf_path = filedialog.askopenfilename(
        title="Seleziona il file PDF",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not pdf_path:
        print("Nessun file selezionato.")
        return

    default_name = os.path.splitext(os.path.basename(pdf_path))[0] + ".docx"

    docx_path = filedialog.asksaveasfilename(
        title="Salva file Word",
        initialfile=default_name,
        defaultextension=".docx",
        filetypes=[("Word Documents", "*.docx")]
    )

    if not docx_path:
        print("Nessun percorso di salvataggio selezionato.")
        return

    print("Conversione in corso...")
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()
    print(f"Conversione completata: {docx_path}")

if __name__ == "__main__":
    select_pdf_and_convert()

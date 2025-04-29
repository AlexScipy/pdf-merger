import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from pypdf import PdfReader, PdfWriter
import os

def sostituisci_pagina():
    tk.Tk().withdraw()

    # Seleziona il PDF principale
    file_principale = filedialog.askopenfilename(
        title="Seleziona il PDF principale",
        filetypes=[("PDF files", "*.pdf")]
    )
    if not file_principale:
        messagebox.showinfo("Annullato", "Nessun PDF principale selezionato.")
        return

    # Seleziona il PDF con la nuova pagina
    file_nuova_pagina = filedialog.askopenfilename(
        title="Seleziona il PDF con la pagina da inserire",
        filetypes=[("PDF files", "*.pdf")]
    )
    if not file_nuova_pagina:
        messagebox.showinfo("Annullato", "Nessuna nuova pagina selezionata.")
        return

    # Ottieni il numero della pagina da sostituire
    reader_principale = PdfReader(file_principale)
    totale_pagine = len(reader_principale.pages)

    pagina_index = simpledialog.askinteger(
        "Pagina da sostituire",
        f"Il PDF ha {totale_pagine} pagine.\nInserisci il numero della pagina da sostituire (1-{totale_pagine}):",
        minvalue=1, maxvalue=totale_pagine
    )
    if pagina_index is None:
        messagebox.showinfo("Annullato", "Nessuna pagina selezionata.")
        return

    # Chiedi dove salvare il file finale
    default_name = os.path.splitext(os.path.basename(file_principale))[0] + "_modificato.pdf"
    file_output = filedialog.asksaveasfilename(
        title="Salva il PDF modificato",
        initialfile=default_name,
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )
    if not file_output:
        messagebox.showinfo("Annullato", "Salvataggio annullato.")
        return

    try:
        reader_nuovo = PdfReader(file_nuova_pagina)
        writer = PdfWriter()

        for i in range(totale_pagine):
            if i == pagina_index - 1:
                writer.add_page(reader_nuovo.pages[0])  # Sostituisci
            else:
                writer.add_page(reader_principale.pages[i])

        with open(file_output, "wb") as f_out:
            writer.write(f_out)

        messagebox.showinfo("Successo", f"PDF salvato come:\n{file_output}")
    except Exception as e:
        messagebox.showerror("Errore", f"Errore durante l'elaborazione:\n{str(e)}")

if __name__ == "__main__":
    sostituisci_pagina()

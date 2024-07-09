import os
import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilename, asksaveasfilename

class DirectorySelector:
    def __init__(self, title: str="Seleziona Cartella"):
        self.title = title
        self.root = tk.Tk()
        self.root.withdraw()

    def select_directory(self, custom_title: str=None) -> str:
        if custom_title is not None:
            title = custom_title
        else:
            title = self.title
        self.root.deiconify()
        directory = askdirectory(title=title)
        self.root.withdraw()
        print(f"Cartella selezionata: {os.path.realpath(directory)}")
        return os.path.realpath(directory)
    
class FileSelector:
    def __init__(self, title: str="Seleziona File"):
        self.title = title
        self.root = tk.Tk()
        self.root.withdraw()

    def select_file(self, custom_title: str=None) -> str:
        # questo metodo restituisce il path del file selezionato
        if custom_title is not None:
            title = custom_title
        else:
            title = self.title
        self.root.deiconify()
        file_path = askopenfilename(title=title,  filetypes=[("PDF files", "*.pdf")])
        self.root.withdraw()
        print(f"File selezionato: {os.path.realpath(file_path)}")
        return os.path.realpath(file_path)
    
    def select_save_dir(self, custom_title: str=None, filetypes: list=[("all files", "*.*")]) -> str:
        # questo metodo restituisce il path dove verra` salvato il file
        if custom_title is not None:
            title = custom_title
        else:
            title = self.title
        file_path = asksaveasfilename(title="Salva il file pdf unificato", filetypes=filetypes)
        print(f"File selezionato: {os.path.realpath(file_path)}" + f"{filetypes[0][1].strip('*')}")
        return os.path.realpath(file_path) + filetypes[0][1].strip('*')


# Example usage:
'''
selector = DirectorySelector()
directory = selector.select_directory()
print(f"Cartella selezionata: {directory}")
'''
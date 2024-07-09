import PyPDF2, os
from Tkinter_utils import FileSelector, DirectorySelector
from tkinter import filedialog

class Merger:
    def __init__(self):
        self.merger = PyPDF2.PdfMerger()

    def aggiungi_file(self, path):
        with open(path, 'rb') as f:
            self.merger.append(f)

    def salva_file(self, path):
        with open(path, 'wb') as f:
            self.merger.write(f)

if __name__ == '__main__':
    merger = Merger()
    file_selector = FileSelector()
    dir_selector = selector = FileSelector()
    merger.aggiungi_file(file_selector.select_file())
    merger.aggiungi_file(file_selector.select_file())
    #merger.salva_file(os.path.join(dir_selector, 'Istituzioni_politiche.pdf'))
    output_path = file_selector.select_save_dir()
    merger.salva_file(output_path)
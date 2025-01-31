import os

from pypdf import PdfWriter

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("All-in-One.pdf")
merger.close()
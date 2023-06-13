"""
Created 2023/06/13 - 10:42 PM

@author: MAA
"""

from PyPDF2 import PdfMerger

pdfs = ["1-OnePDF.pdf", "2-TwoPDF.pdf", "3-ThreePDF.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)
    
merger.write("all_merged.pdf")
merger.close()
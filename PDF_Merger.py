# Timestamp: 2:38:20

import PyPDF2

# pdfiles = ["1.pdf", "2.pdf", "3.pdf"]
pdfiles = [
    "Scholarship 3rd year.pdf",
    "Declaration.pdf",
    "Scholarship Documents 3rd year.pdf",
    "feeReceipt.pdf",
    "RATION.pdf",
      
]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile = open(filename, "rb")
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write("merged.pdf")

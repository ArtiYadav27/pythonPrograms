from pypdf import PdfWriter
import os
merger = PdfWriter()

files=os.listdir("pdfs")
print(files)
for pdf in files:
    input=open(f"pdfs\{pdf}", "rb")
    merger.append(input)

merger.write("merged-pdf.pdf")
merger.close()   



# input1 = open("pdfs\pdf1.pdf", "rb")
# input2 = open("pdfs\pdf2.pdf", "rb")
# input3 = open("pdfs\pdf3.pdf", "rb")

# merger.append(fileobj=input1, pages=(0, 3))
# merger.merge(position=2, fileobj=input2, pages=(0, 1))
# merger.append(input3)

# output = open("document-output.pdf", "wb")
# merger.write(output)
# merger.close()
# output.close()
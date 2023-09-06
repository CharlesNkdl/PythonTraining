import os
import PyPDF2

merger = PyPDF2.PdfMerger()
inp = os.getcwd() + "/tomerge"
outp = os.getcwd() + "/merged/merged.pdf"
for file in os.listdir(inp):
	if file.endswith(".pdf"):
		merger.append(inp + "/" + file)

merger.write(outp)



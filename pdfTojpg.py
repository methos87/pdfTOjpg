# import module
from pdf2image import convert_from_path
import os

#path of pdf
path = r"C:\Users\PP-05\OneDrive - PP\Desktop\Desing\Scripts\pdfTojpeg"

#store pdf
for file in os.listdir(path):
    if file.lower().endswith(".pdf"):
        images = convert_from_path(os.path.join(path,file), 500, poppler_path=r"C:\Program Files\poppler-0.68.0_x86\poppler-0.68.0\bin")
        for image in images:
            image.save(os.path.join(path,file.lower().replace(".pdf",".jpg")),'JPEG')

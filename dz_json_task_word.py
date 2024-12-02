from docx import Document


doc = Document()


doc.add_paragraph("Hello Python")


doc.save("hello_python.docx")

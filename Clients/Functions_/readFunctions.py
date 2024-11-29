from PyPDF2 import PdfReader
import docx


def lire_pdf(fichier):
    lecteur_pdf = PdfReader(fichier)
    texte = ""
    for page in lecteur_pdf.pages:
        texte += page.extract_text()
    return texte

def lire_docx(fichier):
    document = docx.Document(fichier)
    texte = ""
    for paragraphe in document.paragraphs:
        texte += paragraphe.text + "\n"
    return texte


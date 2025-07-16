from reportlab.pdfgen import canvas
import PyPDF2

class TextePDFConvertisseur:
    def convertir(self, chemin_entree, chemin_sortie):
        if chemin_entree.lower().endswith('.txt') and chemin_sortie.lower().endswith('.pdf'):
            self.txt_vers_pdf(chemin_entree, chemin_sortie)
        elif chemin_entree.lower().endswith('.pdf') and chemin_sortie.lower().endswith('.txt'):
            self.pdf_vers_txt(chemin_entree, chemin_sortie)
        else:
            raise ValueError("Conversion non supportée pour ces extensions.")

    def txt_vers_pdf(self, chemin_txt, chemin_pdf):
        c = canvas.Canvas(chemin_pdf)
        with open(chemin_txt, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        y = 800
        for line in lines:
            c.drawString(40, y, line.strip())
            y -= 15
            if y < 40:
                c.showPage()
                y = 800
        c.save()

    def pdf_vers_txt(self, chemin_pdf, chemin_txt):
        with open(chemin_pdf, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
        with open(chemin_txt, 'w', encoding='utf-8') as f:
            f.write(text)
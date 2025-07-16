from PIL import Image

class ImageConvertisseur:
    def convertir(self, chemin_entree, chemin_sortie):
        img = Image.open(chemin_entree)
        img.save(chemin_sortie)
from pydub import AudioSegment

class AudioConvertisseur:
    def convertir(self, chemin_entree, chemin_sortie):
        audio = AudioSegment.from_file(chemin_entree)
        ext = chemin_sortie.split('.')[-1].lower()
        audio.export(chemin_sortie, format=ext)
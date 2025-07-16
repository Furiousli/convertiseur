import customtkinter as ctk
from tkinter import filedialog, messagebox
from convertisseurs.image_convertisseur import ImageConvertisseur
from convertisseurs.audio_convertisseur import AudioConvertisseur
from convertisseurs.texte_pdf_convertisseur import TextePDFConvertisseur
from convertisseurs.ppt_pdf_convertisseur import PPTPDFConvertisseur

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Convertisseur de Fichiers")
        self.geometry("500x400")
        self.resizable(False, False)

        ctk.CTkLabel(self, text="Convertisseur de Fichiers", font=("Arial", 22, "bold")).pack(pady=(15, 10))

        self.tabs = ctk.CTkTabview(self, width=480, height=320)
        self.tabs.pack(pady=10)

        # Onglets
        self.tabs.add("Image")
        self.tabs.add("Audio")
        self.tabs.add("Texte/PDF")
        self.tabs.add("PowerPoint")

        self.init_image_tab()
        self.init_audio_tab()
        self.init_text_pdf_tab()
        self.init_ppt_tab()

    def init_image_tab(self):
        tab = self.tabs.tab("Image")
        self.image_input_path = ctk.StringVar()
        self.image_input_format = ctk.StringVar(value="png")
        self.image_output_format = ctk.StringVar(value="jpg")

        ctk.CTkButton(tab, text="Choisir un fichier image", command=self.select_image_file).pack(pady=10)
        ctk.CTkLabel(tab, textvariable=self.image_input_path, font=("Arial", 10)).pack(pady=2)

        ctk.CTkLabel(tab, text="Format d'entrée :").pack()
        ctk.CTkOptionMenu(tab, variable=self.image_input_format, values=["png", "jpg", "bmp"]).pack()

        ctk.CTkLabel(tab, text="Format de sortie :").pack()
        ctk.CTkOptionMenu(tab, variable=self.image_output_format, values=["png", "jpg", "bmp"]).pack()

        ctk.CTkButton(tab, text="Convertir", command=self.convert_image).pack(pady=15)

    def select_image_file(self):
        path = filedialog.askopenfilename(title="Sélectionnez une image", filetypes=[("Images", "*.png *.jpg *.bmp")])
        if path:
            self.image_input_path.set(path)

    def convert_image(self):
        fichier = self.image_input_path.get()
        if not fichier:
            messagebox.showerror("Erreur", "Veuillez choisir un fichier image.")
            return
        ext = self.image_output_format.get()
        sortie = filedialog.asksaveasfilename(defaultextension=f".{ext}", filetypes=[(ext.upper(), f"*.{ext}")])
        if sortie:
            try:
                convertisseur = ImageConvertisseur()
                convertisseur.convertir(fichier, sortie)
                messagebox.showinfo("Succès", "Image convertie avec succès !")
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

    def init_audio_tab(self):
        tab = self.tabs.tab("Audio")
        self.audio_input_path = ctk.StringVar()
        self.audio_input_format = ctk.StringVar(value="mp3")
        self.audio_output_format = ctk.StringVar(value="wav")

        ctk.CTkButton(tab, text="Choisir un fichier audio", command=self.select_audio_file).pack(pady=10)
        ctk.CTkLabel(tab, textvariable=self.audio_input_path, font=("Arial", 10)).pack(pady=2)

        ctk.CTkLabel(tab, text="Format d'entrée :").pack()
        ctk.CTkOptionMenu(tab, variable=self.audio_input_format, values=["mp3", "wav", "ogg"]).pack()

        ctk.CTkLabel(tab, text="Format de sortie :").pack()
        ctk.CTkOptionMenu(tab, variable=self.audio_output_format, values=["mp3", "wav", "ogg"]).pack()

        ctk.CTkButton(tab, text="Convertir", command=self.convert_audio).pack(pady=15)

    def select_audio_file(self):
        path = filedialog.askopenfilename(title="Sélectionnez un fichier audio", filetypes=[("Audio", "*.mp3 *.wav *.ogg")])
        if path:
            self.audio_input_path.set(path)

    def convert_audio(self):
        fichier = self.audio_input_path.get()
        if not fichier:
            messagebox.showerror("Erreur", "Veuillez choisir un fichier audio.")
            return
        ext = self.audio_output_format.get()
        sortie = filedialog.asksaveasfilename(defaultextension=f".{ext}", filetypes=[(ext.upper(), f"*.{ext}")])
        if sortie:
            try:
                convertisseur = AudioConvertisseur()
                convertisseur.convertir(fichier, sortie)
                messagebox.showinfo("Succès", "Audio converti avec succès !")
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

    def init_text_pdf_tab(self):
        tab = self.tabs.tab("Texte/PDF")
        self.text_input_path = ctk.StringVar()
        self.text_input_format = ctk.StringVar(value="txt")
        self.text_output_format = ctk.StringVar(value="pdf")

        ctk.CTkButton(tab, text="Choisir un fichier texte/PDF", command=self.select_text_file).pack(pady=10)
        ctk.CTkLabel(tab, textvariable=self.text_input_path, font=("Arial", 10)).pack(pady=2)

        ctk.CTkLabel(tab, text="Format d'entrée :").pack()
        ctk.CTkOptionMenu(tab, variable=self.text_input_format, values=["txt", "pdf"]).pack()

        ctk.CTkLabel(tab, text="Format de sortie :").pack()
        ctk.CTkOptionMenu(tab, variable=self.text_output_format, values=["txt", "pdf"]).pack()

        ctk.CTkButton(tab, text="Convertir", command=self.convert_text_pdf).pack(pady=15)

    def select_text_file(self):
        path = filedialog.askopenfilename(title="Sélectionnez un fichier texte ou PDF", filetypes=[("Texte/PDF", "*.txt *.pdf")])
        if path:
            self.text_input_path.set(path)

    def convert_text_pdf(self):
        fichier = self.text_input_path.get()
        if not fichier:
            messagebox.showerror("Erreur", "Veuillez choisir un fichier texte ou PDF.")
            return
        ext = self.text_output_format.get()
        sortie = filedialog.asksaveasfilename(defaultextension=f".{ext}", filetypes=[(ext.upper(), f"*.{ext}")])
        if sortie:
            try:
                convertisseur = TextePDFConvertisseur()
                convertisseur.convertir(fichier, sortie)
                messagebox.showinfo("Succès", "Conversion réussie !")
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

    def init_ppt_tab(self):
        tab = self.tabs.tab("PowerPoint")
        self.ppt_input_path = ctk.StringVar()
        self.ppt_output_format = ctk.StringVar(value="pdf")

        ctk.CTkButton(tab, text="Choisir un fichier PowerPoint", command=self.select_ppt_file).pack(pady=10)
        ctk.CTkLabel(tab, textvariable=self.ppt_input_path, font=("Arial", 10)).pack(pady=2)

        ctk.CTkLabel(tab, text="Format de sortie :").pack()
        ctk.CTkOptionMenu(tab, variable=self.ppt_output_format, values=["pdf"]).pack()

        ctk.CTkButton(tab, text="Convertir", command=self.convert_ppt_pdf).pack(pady=15)

    def select_ppt_file(self):
        path = filedialog.askopenfilename(title="Sélectionnez un fichier PowerPoint", filetypes=[("PowerPoint", "*.pptx")])
        if path:
            self.ppt_input_path.set(path)

    def convert_ppt_pdf(self):
        fichier = self.ppt_input_path.get()
        if not fichier:
            messagebox.showerror("Erreur", "Veuillez choisir un fichier PowerPoint.")
            return
        ext = self.ppt_output_format.get()
        sortie = filedialog.asksaveasfilename(defaultextension=f".{ext}", filetypes=[(ext.upper(), f"*.{ext}")])
        if sortie:
            try:
                convertisseur = PPTPDFConvertisseur()
                convertisseur.convertir(fichier, sortie)
                messagebox.showinfo("Succès", "Conversion réussie !")
            except Exception as e:
                messagebox.showerror("Erreur", str(e))

if __name__ == "__main__":
    app = Application()
    app.mainloop()
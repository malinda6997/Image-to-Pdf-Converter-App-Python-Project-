import tkinter as tk
from tkinter import filedialog
from reportlab.pdfgen import canvas
from PIL import Image
import os

class ImageToPdf:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf = tk.StringVar()
        self.selected_images_list = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.initialize_ui()
    
    def initialize_ui(self):
        title_label = tk.Label(
            self.root, 
            text="Image to PDF Converter", 
            font=("Arial", 20, "bold")
        )
        title_label.pack(pady=10)

        select_image_button = tk.Button(
            self.root, 
            text="Select Images", 
            command=self.select_images,
            font=("Arial", 12, "bold")
        )
        select_image_button.pack(pady=(0, 10))

        self.selected_images_list.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(
            self.root, 
            text="Enter PDF file name", 
            font=("Arial", 12, "bold")
        )
        label.pack()

        pdf_name_entry = tk.Entry(
            self.root, 
            textvariable=self.output_pdf, 
            width=40, 
            justify="center"
        )
        pdf_name_entry.pack()  

        convert_button = tk.Button(
            self.root, 
            text="Convert to PDF", 
            command=self.convert_to_pdf,
            font=("Arial", 12, "bold")
        )
        convert_button.pack(pady=(20, 40))

    def select_images(self):
        self.image_paths = filedialog.askopenfilenames(
            title="Select Images", 
            filetypes=[("Image files", "*.jpg; *.png; *.jpeg")]      
        )
        self.update_selected_images_list()

    def update_selected_images_list(self):
        self.selected_images_list.delete(0, tk.END)
        for image_path in self.image_paths:
            _, image_name = os.path.split(image_path)
            self.selected_images_list.insert(tk.END, image_name)

    def convert_to_pdf(self):
        if not self.image_paths:
            return
        output_pdf_path = (
            self.output_pdf.get().strip() + ".pdf"
            if self.output_pdf.get().strip()
            else "output.pdf"
        )
        pdf = canvas.Canvas(output_pdf_path, pagesize=(612, 792))
        for image_path in self.image_paths:
            img = Image.open(image_path)
            available_width = 540
            available_height = 720
            scale_factor = min(available_width / img.width, available_height / img.height)
            new_width = img.width * scale_factor
            new_height = img.height * scale_factor
            x_center = (612 - new_width) / 2
            y_center = (792 - new_height) / 2
            pdf.drawInlineImage(image_path, x_center, y_center, width=new_width, height=new_height)
            pdf.showPage()
        pdf.save()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image to PDF Converter")
    root.geometry("400x600")
    root.resizable(False, False)
    app = ImageToPdf(root)
    root.mainloop()

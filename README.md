# Image to PDF Converter

## Overview
The **Image to PDF Converter** is a simple desktop application that allows users to select multiple image files (JPEG, PNG, JPG) and convert them into a single PDF document. The application uses a graphical user interface (GUI) created with **Tkinter** and the **ReportLab** library to generate the PDF.

## Features
- Select multiple image files from your computer.
- Preview the selected images in the list.
- Enter a custom name for the output PDF file.
- Convert the selected images into a single PDF file.
- Clear input fields after conversion for the next set of images.

## Requirements
- **Python** (version 3.x)
- **Tkinter** (for creating the graphical user interface)
- **Pillow** (for working with image files)
- **ReportLab** (for generating PDF documents)

You can install the required dependencies using the following:

```bash
pip install pillow reportlab
```

## How to Use
1. **Select Images**:
   - Click the "Select Images" button to choose image files from your computer. You can select multiple images at once.
   
2. **Enter PDF File Name**:
   - In the input box below the image list, enter a name for your output PDF. If left blank, the default name "output.pdf" will be used.

3. **Convert to PDF**:
   - After selecting the images and entering the PDF name, click the "Convert to PDF" button.
   - The selected images will be converted into a PDF, and the resulting file will be saved with the name you provided.

4. **Ready for Next Conversion**:
   - Once the PDF is generated, the application will clear the input fields and reset, ready for the next conversion.

## Code Overview
The core of the application is contained within the `ImageToPdf` class. This class is responsible for:

- **Initializing the UI**: Using Tkinter to create buttons, text fields, and a listbox to select images.
- **Selecting Images**: The user selects images via a file dialog, which are displayed in a list.
- **Converting to PDF**: The selected images are resized to fit into a standard letter-sized PDF page and added sequentially to the PDF.
- **Clearing Inputs**: After conversion, the fields are cleared for the next set of images.

## Example Workflow
1. Click "Select Images" to choose images from your file explorer.
2. Enter a custom name (e.g., `my_images`) for the PDF or leave the field blank to use the default `output.pdf`.
3. Click "Convert to PDF".
4. The images are converted into a PDF, and the fields are cleared for the next use.

## License
This project is open-source and available for modification and personal use.

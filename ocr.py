import cv2
import pytesseract
from pdf2image import convert_from_path
import numpy as np

import os
import argparse


#  Perform OCR on an image.
def ocr_image(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Perform OCR on the image
    text = pytesseract.image_to_string(gray)
    return text


# Perform OCR on all pages of a PDF file.
def process_pdf(pdf_path):
    all_text = ""
    try:
        images = convert_from_path(pdf_path)
        for image in images:
            # Convert PIL image to OpenCV format
            open_cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            text = ocr_image(open_cv_image)  # Perform OCR on the page
            all_text += text + "\n"
    except Exception as e:
        raise RuntimeError(f"Error processing PDF: {e}")
    return all_text


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Perform OCR on images or PDFs.")
    parser.add_argument("file_path", type=str, help="Path to the file to be processed")
    args = parser.parse_args()

    file_path = args.file_path
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    extracted_text = ""
    try:
        if file_extension in [".jpeg", ".jpg", ".png"]:
            print(f"Processing {file_extension.upper()}...")
            extracted_text = ocr_image(cv2.imread(file_path))
        elif file_extension == ".pdf":
            print("Processing PDF...")
            extracted_text = process_pdf(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")

        # Save the extracted text to a file
        output_file = f"extracted_{file_extension[1:]}.txt"
        with open(output_file, "w") as f:
            f.write(extracted_text)
        print(f"Extracted text has been saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

import cv2
import pytesseract

def ocr_img(img_pth):
    # Read the image using OpenCV
    image = cv2.imread(img_pth) 

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the image
    text = pytesseract.image_to_string(gray)
    return text

if __name__ == "__main__":
    # Path to the image file
    img_pth = './whitman.png'

    # Perform OCR
    extracted_text = ocr_img(img_pth) 

    print(f"Extracted Text:\n{extracted_text}\n")

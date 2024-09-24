from PIL import Image
import pytesseract
import json


def extract_text_from_image(image):
    # Extract text from the image using pytesseract
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Users\THENIS\ocr_webapp_env\tesseract.exe"
    )
    text = pytesseract.image_to_string(image, lang="eng")
    return {"extracted_text": text}

from PIL import Image
import pytesseract
import json


def extract_text_from_image(image):
    # Extract text from the image using pytesseract
    
    text = pytesseract.image_to_string(image, lang="eng")
    return {"extracted_text": text}

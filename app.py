import streamlit as st
from PIL import Image
from ocr import extract_text_from_image  # Import OCR function from ocr.py

st.title("OCR Web App English Text")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Use OCR function from ocr.py
    extracted_text = extract_text_from_image(image)
    st.write("Extracted Text:")
    st.json(extracted_text)

    # Search for a keyword in the extracted text
    keyword = st.text_input("Enter keyword to search:")
    if keyword:
        # Access the text inside the extracted_text dictionary
        text = extracted_text["extracted_text"]
        if keyword.lower() in text.lower():
            highlighted_text = text.replace(keyword, f"**{keyword}**")
            st.write(highlighted_text)
        else:
            st.write(f"'{keyword}' not found.")

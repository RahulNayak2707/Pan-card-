import streamlit as st
from PIL import Image
import pytesseract
import re

st.title('PAN Card Number Extractor')

uploaded_file = st.file_uploader("Upload your PAN card image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded PAN Card Image.', use_column_width=True)
    
    # Step 2: Process the uploaded image
    # Extract text from the image using Tesseract OCR
    if st.button('Extract Pan Number'):
        text = pytesseract.image_to_string(image)
        
        # Step 3: Extract the PAN card number using regex
        pattern = r'[A-Z]{5}[0-9]{4}[A-Z]'
        match = re.findall(pattern, text)
        


        if match:
            st.write(f"Extracted PAN Card Number: {match[0]}")
        else:
            st.write("Could not extract PAN Card Number. Please try again with a clearer image.")
import streamlit as st
import pyshorteners
import qrcode
from PIL import Image
import io

def shorten_url(long_url):
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(long_url)

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def main():
    st.title("QR Code Generator and URL Shortener")

    # Initialize session state
    session_state = SessionState(shortened_url=None)

    # Input text
    text_qr = st.text_input("Enter URL to encode in QR code")

    if st.button("Shorten URL"):
        if text_qr:
            session_state.shortened_url = shorten_url(text_qr)
            st.success(f"Shortened URL: {session_state.shortened_url}")

    # Determine which text to use for generating the QR code
    if session_state.shortened_url:
        qr_text = session_state.shortened_url
    else:
        qr_text = text_qr

    if st.button("Generate QR Code"):
        qr_img = generate_qr_code(qr_text)

        # Display text and QR code
        st.write("Text to Encode:", qr_text)
        img_bytes = io.BytesIO()
        qr_img.save(img_bytes, format='PNG')
        st.image(img_bytes, caption="Generated QR Code")
        st.download_button(
            label="Download image",
            data=img_bytes,
            file_name=f"qr_{qr_text}.png",
            mime="image/png"
        )

if __name__ == "__main__":
    main()




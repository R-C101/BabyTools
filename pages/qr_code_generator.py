import streamlit as st
import qrcode
import requests
from PIL import Image
from io import BytesIO
import pyshorteners

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)


def generate_qr(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def main():
    st.title("URL Shortener & QR Code Generator")

    # Input URL from user
    url = st.text_input("Enter the URL:")

    if st.button("Shorten URL"):
        if url:
            shortened_url = shorten_url(url)
            st.success(f"Shortened URL: {shortened_url}")

    if st.button("Generate QR Code"):
        if url:
            
                if "Shortened URL" in st.session_state:
                    qr_url = st.session_state["Shortened URL"]
                else:
                    qr_url = url

                qr_img = generate_qr(qr_url)
                st.write("Text to Encode:", qr_url)
                img_bytes = BytesIO()
                qr_img.save(img_bytes, format='PNG')
                st.image(img_bytes, caption="Generated QR Code")
                st.download_button(
                    label="Download QR Code",
                    data=img_bytes,
                    file_name="qr_code.png",
                    mime="image/png"
                )

                # Store shortened URL in session state if it's different from original URL
                if qr_url != url:
                    st.session_state["Shortened URL"] = qr_url


if __name__ == "__main__":
    main()

import os
import PyPDF2
import streamlit as st
from io import BytesIO
def combine_pdfs(input_files):
    pdf_writer = PyPDF2.PdfWriter()
    
    for file in input_files:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
    
    return pdf_writer

if __name__ == "__main__":
    st.title("PDF Concatenator")

    uploaded_files = st.file_uploader("Upload multiple PDF files", accept_multiple_files=True)

    if uploaded_files:
        
        pdf_writer = combine_pdfs(uploaded_files)

        
        if st.button("Generate Combined PDF"):
            combined_pdf_bytes = BytesIO()
            pdf_writer.write(combined_pdf_bytes)
            st.download_button(label="Download Combined PDF", data=combined_pdf_bytes.getvalue(), file_name="combined.pdf", mime="application/pdf")
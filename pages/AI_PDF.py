import streamlit as st
import PyPDF2
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import io
nlp = pipeline('question-answering', model='deepset/roberta-base-squad2', tokenizer='deepset/roberta-base-squad2')
def generate_answer(question, context):
    ques_dict = {
                'question':question, 
                'context': context
               }
    
    return nlp(ques_dict)['answer']
    

# Function to read text from docx file


# Function to read text from pdf file
def read_pdf(file):
    text = []
    with io.BytesIO(file.read()) as f:
        reader = PyPDF2.PdfReader(f)
        for page in range(len(reader.pages)):
            text.append(reader.pages[page].extract_text())
    return '\n'.join(text)

st.title('AI PDF App')

# Allow user to input text or upload file
text_input = st.text_area('Enter your text:', '')

file = st.file_uploader("Upload a file", type=[ 'pdf'])

if file is not None:
    text = read_pdf(file)

    st.text_area("Uploaded file content:", text)

# Input question from the user
question = st.text_input('Enter your question:', '')

if st.button('ASK QUESTION'):
    if text_input or file:
        if text_input:
            processed_text = generate_answer(question,text_input)
        elif file:
            processed_text = generate_answer(question,text)
        
        st.subheader('Answer')
        st.write(processed_text)
    else:
        st.warning('Please enter text or upload a file.')



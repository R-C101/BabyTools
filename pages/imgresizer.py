import streamlit as st
from PIL import Image
from io import BytesIO

def resize_image(image, target_width, target_height, squeeze=True):
    original_width, original_height = image.size
    
    if squeeze:
        
        new_width = target_width
        new_height = target_height
        resized_image = image.resize((new_width, new_height))
        padded_image = Image.new("RGB", (target_width, target_height), (255, 255, 255))
        x_offset = (target_width - new_width) // 2
        y_offset = (target_height - new_height) // 2
        padded_image.paste(resized_image, (x_offset, y_offset))
        resized_image = padded_image
    else:
        width_ratio = target_width / original_width
        height_ratio = target_height / original_height
        ratio = min(width_ratio, height_ratio)
        new_width = int(original_width * ratio)
        new_height = int(original_height * ratio)
        
        # Create padded image
        padded_image = Image.new("RGB", (target_width, target_height), (255, 255, 255))
        x_offset = (target_width - new_width) // 2
        y_offset = (target_height - new_height) // 2
        padded_image.paste(image.resize((new_width, new_height)), (x_offset, y_offset))
        resized_image = padded_image
    
    return resized_image

st.title("Image Resizer")

# Upload image
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Input target width and height
    target_width = st.number_input("Target Width", value=image.width, min_value=1)
    target_height = st.number_input("Target Height", value=image.height, min_value=1)

    # Choose resizing method
    resize_method = st.radio("Resize Method", ("Squeeze", "Padding"))

    resize_clicked = st.button("Resize")
    if resize_clicked:
        if resize_method == "Squeeze":
            resized_image = resize_image(image, target_width, target_height, squeeze=True)
        else:
            resized_image = resize_image(image, target_width, target_height, squeeze=False)
        
        st.image(resized_image, caption="Resized Image")

        # Download button
        img_byte_array = BytesIO()
        resized_image.save(img_byte_array, format='PNG')
        img_byte_array = img_byte_array.getvalue()
        st.download_button(label='Download Resized Image',
                           data=img_byte_array,
                           file_name='resized_image.png',
                           mime='image/png')


import io
import torch
import streamlit as st
from PIL import Image
from predict import load_model, inference
from utils import transform_image
from confirm_button_hack import cache_on_button_press
# how to run: streamlit run app.py 

st.set_page_config(layout='wide')

st.write("hello world")

@cache_on_button_press('Authenticate')
def authenticate(pwd) -> bool:
    st.write(type(pwd))
    return pwd == root_pwd

def main():
    st.title("Trash Classification Model - Github Action Deploy")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = load_model()

    uploaded_file = st.file_uploader("Choose an image", type=["jpg","jpeg","png"])
    if uploaded_file:
        image = Image.open(io.BytesIO(uploaded_file.getvalue()))
        st.image(image)
        st.write('classifying...')
        image = transform_image(image).to(device)
        result = inference(model, image, device)
        st.write(f"Prediction Response : {result}")
    # img = transform_image(img)
    # inference(model, img, device)

root_pwd = 'password'
pwd = st.text_input('password', type='password')


if authenticate(pwd):
    main()
else:
    st.error("Teh password is invalid.")

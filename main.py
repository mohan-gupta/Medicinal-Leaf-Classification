import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

model = load_model('Model/model.h5')
class_dict = np.load("artifacts/class_names.npy")


def predict(image):
    IMG_SIZE = (1, 224, 224, 3)

    img_arr = np.array(image)
    img_arr = np.resize(img_arr, (IMG_SIZE[1:]))
    img_arr = np.reshape(img_arr, IMG_SIZE)

    print(img_arr.shape)
    pred = model.predict(img_arr)

    return pred

if __name__ == '__main__':
    st.markdown(
        f"""
             <style>
             .stApp {{
                 background: url("https://images.unsplash.com/photo-1448375240586-882707db888b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80");
                 background-size: cover
             }}
             </style>
             """,
        unsafe_allow_html=True
    )
    new_title = '<p style="font-family:sans-serif; color:White; font-size: 42px;">Medicinal Leaf Classification</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        img_arr = np.array(img)

        img = img.resize((300, 300))
        st.image(img)

        if st.button("Predict"):
            pred = predict(img_arr)
            name = class_dict[np.argmax(pred)]

            result = '<p style="font-family:sans-serif; color:White; font-size: 16px;">The given image ' \
                        'is '+name+'</p>'
            st.markdown(result, unsafe_allow_html=True)




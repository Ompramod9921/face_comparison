from deepface import DeepFace
from PIL import Image
import numpy as np
import cv2
import streamlit as st

st.set_page_config(page_title='Deepface',page_icon='👽')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Face Comparison")
st.write("Made with ❤️ by om pramod")
st.markdown("*****")

try :
    image_file1 = st.file_uploader("upload first image",type=["png","jpg","jpeg"])
    st.image(image_file1,use_column_width=True)
    st.markdown("****")
    image_file2 = st.file_uploader("upload second image",type=["png","jpg","jpeg"])
    st.image(image_file2,use_column_width=True)
    st.markdown("****")
except :
    pass

if image_file1 and image_file2 is not None:
    submit = st.button("Compare images")

    if submit :
        try:
            image_loaded1 = Image.open(image_file1)
            new_image1 = np.array(image_loaded1.convert('RGB')) #converting image into array
            img1 = cv2.cvtColor(new_image1,1)
            image_loaded2 = Image.open(image_file2)
            new_image2 = np.array(image_loaded2.convert('RGB')) #converting image into array
            img2 = cv2.cvtColor(new_image2,1)
            
            result = DeepFace.verify(img1,img2)
            if result['verified']==True:
                st.success("Both images are of same person....")
            else:
                st.success("Both images are of two different persons.... ")
        except:
            st.error("Face could not be detected. Please confirm that the picture is a face photo")
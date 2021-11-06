import streamlit as st
import tensorflow as tf
import streamlit as st

st.set_page_config(
    page_title='Find your X-men',
    page_icon='icon.png'
)

st.image('icon.png', width=600)
st.title('Find your X-men')
st.subheader("Upload an image and find which X-men character it contains")
st.set_option('deprecation.showfileUploaderEncoding', False)
@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model("final.h5")
  return model
with st.spinner('Model is being loaded..'):
  model=load_model()




import cv2
from PIL import Image, ImageOps
import numpy as np

def import_and_predict(image_data, model):
    
        size = (256,256)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #img_resize = (cv2.resize(img, dsize=(75, 75),    interpolation=cv2.INTER_CUBIC))/255.
        
        img_reshape = img[np.newaxis,...]
    
        prediction = model.predict(img_reshape)
        
        return prediction
    
file = st.file_uploader("Please upload an image file", type=["jpg", "png"])
class_btn = st.button("CLASSIFY!!")
if file is not None:
        image = Image.open(file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
if class_btn:
    if file is None:
        st.text("Please upload an image file")
    else:
        prediction = import_and_predict(image, model)
        class_names=['Angel','Beast','Cyclops', 'Iceman', 'Magneto', 'Mystique', 'Phoenix', 'Professor X', 'Storm', 'Wolverine']
        string="This image is most likely: "+class_names[np.argmax(prediction)]
        st.success(string)
        
st.image('bottom.jpg')
st.markdown('''
    *Built with :heart: by [Pranjal Singh](https://github.com/Pranjal198).*
*Show some love to this project by starring and sharing the repository on [GitHub](https://github.com/Pranjal198/X-men-classifier) !*
    ''')

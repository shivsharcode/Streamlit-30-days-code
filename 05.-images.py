import streamlit as st
import matplotlib.image as mpimg

st.header("Images in streamlit")

# using matplotlib.image
st.subheader("matplotlilb plot")

img = mpimg.imread("./assets/billu-badmaash.png")

st.image(img, caption="Billu Badmaash", width=400) # to show image in Streamlit


# From folder
st.subheader("Image from folder")
st.image("./assets/billu-badmaash.png", caption = "2nd", width = 400)
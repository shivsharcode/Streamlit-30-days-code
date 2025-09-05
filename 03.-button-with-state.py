import streamlit as st

st.header("st.button with state")

# initialize the state if it doesn't exist yet
if "button_state" not in st.session_state:
    st.session_state.button_state = False
    
# when the button is pressed, toggle the state
if st.button("Press it"):
    st.session_state.button_state = not st.session_state.button_state

# show text depending on state
if st.session_state.button_state:
    st.write("ON")
else:
    st.write("OFF")
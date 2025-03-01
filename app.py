import streamlit as st
from PIL  import Image
from pipe import find

st.markdown("""
    <h2 style='text-align: center;'>Disney Movies</h1>
    <h4 style='text-align: center;'>Recommendation System</h3>
""", unsafe_allow_html=True)

tangled, mulan = st.columns(2)

with tangled:
    st.image(Image.open('assets/tangled.jpg'))

with mulan:
    st.image(Image.open('assets/mulan.jpg'))

title = st.text_input('#### Movie Title')

if title != '':
    
    results = find(title)

    for i, movie in enumerate(results):

        st.write(f"""
            ### {i+1}. {movie[1]}
            ###### Type: {movie[3]} {'  '} Runtime: {movie[5]}
            ###### Genre: {movie[4]} 
            #### Synopsis:
            {movie[2]} 
        """)
        
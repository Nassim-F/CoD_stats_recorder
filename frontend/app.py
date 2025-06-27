import streamlit as st
from PIL import Image

import ocr_game_stats

with st.file_uploader("Importer une image", type=['png', 'jpg', 'jpeg']) as uploaded_image:

    if uploaded_image is not None:
        score_board_image = Image.open(uploaded_image)
        st.image(score_board_image)
    else:
        st.write("problème")



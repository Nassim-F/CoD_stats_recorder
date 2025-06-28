import streamlit as st
import cv2
import numpy as np
from PIL import Image
from ocr_game_stats import *

with st.file_uploader("Importer une image", type=['png', 'jpg', 'jpeg']) as uploaded_image:

    try :
        if uploaded_image is not None:

            score_board_image = Image.open(uploaded_image)

            image_bgr = np.array(score_board_image)

            score_board_cv2 = cv2.cvtColor(image_bgr, cv2.COLOR_RGB2BGR)

            st.image(score_board_image)

            player_name = st.text_input("Veuillez renseignez votre pseudo : ")

            map_and_mode_names = get_map_and_mode_name(score_board_cv2)
            list_game_info = get_list_game_information(score_board_cv2)
            game_result = get_game_result(list_game_info)
            player_stats = get_player_stats(list_game_info, player_name)

            all_data = dict(chain.from_iterable(d.items() for d in (map_and_mode_names, game_result, player_stats)))

            st.write(all_data)
            st.dataframe(all_data)

        else:
            st.write("problème")
    except KeyError as e:
        st.write("Veuillez importer une image")


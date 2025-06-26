# pylint: disable=missing-module-docstring

from datetime import datetime

import cv2
import easyocr

start_time = datetime.now()


def get_map_and_mode_name(path_image: str) -> dict:
    """
    Process the score board image in order to take only the map name and the game
    :param path_image : image location to analyse
    :return dict_game_mode_name : dictionary that contains the map name and the mode name
    """
    img = cv2.imread(path_image)

    # Cropping image : 1st image to get the game mode and the map name and the second for the stats
    game_mode = img[80:220, 310:1400]

    reader = easyocr.Reader(["fr"])
    result_game_mode = reader.readtext(game_mode)

    text_result_game_mode = [detection[1] for detection in result_game_mode]

    dict_game_mode_name = {
        "map": text_result_game_mode[0],
        "game_mode": text_result_game_mode[1],
    }

    return dict_game_mode_name


def get_list_game_information(path_image: str) -> list:
    """
    Split the image to get the scoreboard part only
    Then it stores all text information detected by easyocr
    :param path_image:
    :return: list
    """
    img = cv2.imread(path_image)

    # Cropping image : 1st image to get the game mode and the map name and the second for the stats
    score_board = img[360:2050, 370:3470]

    reader = easyocr.Reader(["fr"])
    result_score_board = reader.readtext(score_board)

    list_game_information = [detection[1] for detection in result_score_board]

    return list_game_information


def get_game_result(list_game_information: list) -> dict:
    """
    This method looks for the result and return if its win or defeat with the final score result
    :param list_game_information:
    :return final: dictionary that contains the result (win or defeat) and final score result
    """
    final = {}
    result = ''
    for data in list_game_information[:5]:
        # I don't know if the position will change
        # that's why I check if the value contains only number or not to get the score result
        if data.replace(' ', '').isdigit():
            result = data

    check_result = result.split(' ')

    if int(check_result[0]) > int(check_result[1]):
        final['résultat'] = 'victoire'
        final['résultat_score_final'] = result.replace(' ', ' - ')
    elif int(check_result[0]) < int(check_result[1]):
        final['résultat'] = 'défaite'
        final['résultat_score_final'] = result.replace(' ', ' - ')
    else:
        final['résultat'] = 'égalité'
        final['résultat_score_final'] = result.replace(' ', ' - ')

    return final


map_and_ode_name = get_map_and_mode_name("test_image/ec_win.png")
list_game_info = get_list_game_information("test_image/ec_win.png")

end_time = datetime.now()

print(map_and_ode_name)
print(list_game_info)

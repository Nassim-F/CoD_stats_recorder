# pylint: disable=missing-module-docstring

from datetime import datetime
from itertools import chain

import cv2
import easyocr


def get_map_and_mode_name(path_image: str) -> dict:
    """
    Process the score board image in order to take only the map name and the game by cropping
    the right image part
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


def get_player_stats(list_score_board_stats: list, player_name: str) -> dict:
    """
    Retrieve all the player stats that are in the list depending on the user id of the player
    Return a dictionary with all the stats of the targeted player related to the game mode
    :param list_score_board_stats: list that contains all texts extracted from the scoreboard image
    :param player_name: player user id
    :return dict_stats: dictionary that contains all the remaining stats
    """
    dict_stats = {}
    for data in list_score_board_stats[14:-12]:
        # I split the list in order to make easy the check condition
        # and get the right data in the score board
        if player_name in data:
            # retrieve the position of the player in the list
            # and add scoreboard stats in dictionary
            dict_stats['score'] = list_score_board_stats[list_score_board_stats.index(data) + 1]
            dict_stats['score_objectif'] = list_score_board_stats[list_score_board_stats.index(data) + 2]
            dict_stats['confirmation'] = list_score_board_stats[list_score_board_stats.index(data) + 3]

    for data in list_score_board_stats[-12:]:  # I take only the last line stats
        if player_name in data:
            dict_stats['éliminations/assists'] = list_score_board_stats[-5]
            dict_stats['morts'] = list_score_board_stats[-4]
            dict_stats['ratio'] = round(int(list_score_board_stats[-5]) / int(list_score_board_stats[-4]), 2)
            dict_stats['refus'] = list_score_board_stats[-1].split(' ')[
                0]  # I retrieve only the number, so  it's the first element after splitting the value

    return dict_stats


map_and_mode_names = get_map_and_mode_name("test_image/ec_win.png")
list_game_info = get_list_game_information("test_image/ec_win.png")
game_result = get_game_result(list_game_info)
player_name = input("Renseignez un pseudo : ")
player_stats = get_player_stats(list_game_info, player_name)

all_data = dict(chain.from_iterable(d.items() for d in (map_and_mode_names, game_result, player_stats)))
end_time = datetime.now()


print(all_data)

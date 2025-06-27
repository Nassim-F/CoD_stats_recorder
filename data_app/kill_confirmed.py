from data_app.game import Game
import datetime

class KillConfirmed(Game):

    def __init__(self,
                 game_mode_name : str,
                 map_name : str,
                 score : int,
                 eliminations_assists : int,
                 deaths : int,
                 ratio : float,
                 date_game : datetime,
                 score_objective : int,
                 confirmations : int,
                 denials : int) -> None:
        """
        Initialize kill confirmed game mode
        It is a child class based on Game class
        """

        super().__init__(game_mode_name, map_name, score, eliminations_assists, deaths, ratio, date_game),
        self.score_objective = score_objective
        self.confirmations = confirmations
        self.denials = denials


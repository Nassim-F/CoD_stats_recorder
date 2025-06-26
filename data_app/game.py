import datetime
class Game:
    """
    Create a game that contains :
    - map name
    - the common stats between the different game modes
    - game mode name
    """

    def __init__(self,
                 game_mode_name : str,
                 map_name : str,
                 score : int,
                 eliminations_assists : int,
                 deaths : int,
                 ratio : float,
                 date_game : datetime) -> None:
        """ Initialize game"""
        self.game_mode_name = game_mode_name
        self.map_name = map_name
        self.score = score
        self.eliminations_assists = eliminations_assists
        self.deaths = deaths
        self.ratio = ratio
        self.date_game = date_game


    def get_all_stats(self) -> dict:
        """
        Return all the stats
        """
        stats = {"eliminations_assists": self.eliminations_assists,
                 "deaths": self.deaths,
                 "score": self.score,
                 "ratio": self.ratio}

        return stats

    def game_information_and_stats(self) -> dict:
        """
        Return all the information about the game with the player stats
        :return :
        """
        game_information = {"game_mode_name": self.game_mode_name,
                            "map": self.map_name,
                            "eliminations_assists": self.eliminations_assists,
                            "deaths": self.deaths,
                            "ratio": self.ratio,
                            "date" : self.date_game}

        return game_information

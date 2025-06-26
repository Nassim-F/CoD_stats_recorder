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
                 eliminations_assists : int,
                 deaths : int,
                 ratio : float) -> None:
        """ Initialize game"""
        self.game_mode_name = game_mode_name
        self.map_name = map_name
        self.eliminations_assists = eliminations_assists
        self.deaths = deaths
        self.ratio = ratio


    def get_all_stats(self) -> dict:
        """
        Return all the stats
        """
        stats = {"game_mode_name": self.game_mode_name,
                 "map": self.map_name,
                 "eliminations_assists": self.eliminations_assists,
                 "deaths": self.deaths,
                 "ratio": self.ratio}

        return stats

    def simulates_game(self) -> Game:

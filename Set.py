from Game import Game
from Player import Player

class Set:
    def __init__(self, set_id: str, games: list, set_winner: 'Player'):
        self._set_id = set_id
        self._games = []
        self._set_winner = set_winner

    # Métodos Getter y Setter
    def get_set_id(self) -> str:
        return self._set_id

    def set_set_id(self, set_id: str) -> None:
        self._set_id = set_id

    def get_games(self) -> list:
        return self._games

    def set_games(self, games: list) -> None:
        self._games = games

    def get_set_winner(self) -> 'Player':
        return self._set_winner

    def set_set_winner(self, set_winner: 'Player') -> None:
        self._set_winner = set_winner

    def print_set_data(self) -> None:
        print("Set Data:")
        print("-------------------------------------------------")
        print("| {:<15} | {:<10} |".format("Attribute", "Value"))
        print("-------------------------------------------------")
        print("| {:<15} | {:<10} |".format("Set ID", self._set_id))
        print("| {:<15} |".format("Set Winner"))
        if self._set_winner:
            print("| {:<30} | {:<10} |".format("Player ID", self._set_winner.get_player_id()))
            print("| {:<30} | {:<10} |".format("Points", self._set_winner.get_points()))
        else:
            print("| {:<30} | {:<10} |".format("", "No Winner"))
        print("| {:<15} |".format("Games"))
        for game in self._games:
            print("| {:<30} | {:<10} |".format("Game ID", game.get_game_id()))
            print("| {:<30} |".format("Game Winner"))
            if game.get_game_winner():
                print("| {:<40} | {:<10} |".format("Player ID", game.get_game_winner().get_player_id()))
                print("| {:<40} | {:<10} |".format("Points", game.get_game_winner().get_points()))
            else:
                print("| {:<40} | {:<10} |".format("", "No Winner"))
        print("-------------------------------------------------")


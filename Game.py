from Player import Player
class Game:
    def __init__(self, game_id: str, players: list, game_winner: 'Player'):
        self._game_id = game_id
        self._players = players
        self._game_winner = game_winner

    # Métodos Getter y Setter
    def get_game_id(self) -> str:
        return self._game_id

    def set_game_id(self, game_id: str) -> None:
        self._game_id = game_id

    def get_players(self) -> list:
        return self._players

    def set_players(self, players: list) -> None:
        self._players = players

    def get_game_winner(self) -> 'Player':
        return self._game_winner

    def set_game_winner(self, game_winner: 'Player') -> None:
        self._game_winner = game_winner

    def print_game_data(self) -> None:
        print("Game Data:")
        print("-------------------------------------------------")
        print("| {:<15} | {:<10} |".format("Attribute", "Value"))
        print("-------------------------------------------------")
        print("| {:<15} | {:<10} |".format("Game ID", self._game_id))
        print("| {:<15} |".format("Players"))
        for player in self._players:
            print("| {:<15} | {:<10} |".format("", f"Player ID: {player.get_player_id()}"))
            print("| {:<25} | {:<10} |".format("", f"Luck: {player.get_luck()}"))
            print("| {:<25} | {:<10} |".format("", f"Technique: {player.get_technique()}"))
            print("| {:<25} | {:<10} |".format("", f"Positioning: {player.get_positioning()}"))
            print("| {:<25} | {:<10} |".format("", f"Sets won: {player.get_sets_won()}"))
            print("| {:<25} | {:<10} |".format("", f"Draws won: {player.get_games_won()}"))
            print("| {:<25} | {:<10} |".format("", f"Service faults: {player.get_service_failure()}"))
            print("| {:<25} | {:<10} |".format("", f"Missed serves: {player.get_missed_serves()}"))
            print("| {:<25} | {:<10} |".format("", f"Serves served: {player.get_serves_served()}"))
            print("| {:<25} | {:<10} |".format("", f"Points: {player.get_points()}"))
            print("| {:<25} | {:<10} |".format("", f"Tournament type won: {player.get_type_of_tournament_won()}"))
            print("| {:<25} | {:<10} |".format("", f"Tournaments won: {player.get_tournaments_won()}"))
            print("-------------------------------------------------")
        print("| {:<15} |".format("Game Winner"))
        print("| {:<25} | {:<10} |".format("", f"Player ID: {self._game_winner.get_player_id()}"))
        print("| {:<25} | {:<10} |".format("", f"Points: {self._game_winner.get_points()}"))
        print("-------------------------------------------------")

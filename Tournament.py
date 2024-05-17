from Player import Player
from Set import Set

class Tournament:
    def __init__(self, tournament_id: int, tournament_type: str, tournament_winner: 'Player', sets: list):
        self._tournament_id = tournament_id
        self._tournament_type = tournament_type
        self._tournament_winner = tournament_winner
        self._sets = sets

    # Métodos Getter y Setter
    def get_tournament_id(self) -> int:
        return self._tournament_id

    def set_tournament_id(self, tournament_id: int) -> None:
        self._tournament_id = tournament_id

    def get_tournament_type(self) -> str:
        return self._tournament_type

    def set_tournament_type(self, tournament_type: str) -> None:
        self._tournament_type = tournament_type

    def get_tournament_winner(self) -> 'Player':
        return self._tournament_winner

    def set_tournament_winner(self, tournament_winner: 'Player') -> None:
        self._tournament_winner = tournament_winner

    def get_sets(self) -> list:
        return self._sets

    def set_sets(self, sets: list) -> None:
        self._sets = sets

    def print_tournament_data(self) -> None:
        print("Tournament Data:")
        print("-------------------------------------------------")
        print("| {:<15} | {:<10} |".format("Attribute", "Value"))
        print("-------------------------------------------------")
        print("| {:<15} | {:<10} |".format("Tournament ID", self._tournament_id))
        print("| {:<15} | {:<10} |".format("Tournament Type", self._tournament_type))
        print("| {:<15} |".format("Tournament Winner"))
        print("| {:<30} | {:<10} |".format("Player ID", self._tournament_winner.get_player_id()))
        print("| {:<30} | {:<10} |".format("Sets Won", self.calculate_sets_won()))
        print("| {:<15} |".format("Sets"))
        for i, s in enumerate(self._sets):
            print("| {:<15} | {:<10} |".format(f"Set {i+1}", f"Winner: {s.get_set_winner().get_player_id()}, Sets Won: {s.get_set_winner().get_sets_won()}"))
        print("-------------------------------------------------")

    def calculate_sets_won(self) -> int:
        return sum(s.get_set_winner() == self._tournament_winner for s in self._sets)


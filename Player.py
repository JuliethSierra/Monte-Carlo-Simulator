class Player:
    def __init__(self, player_id: str, luck: float, technique: int, positioning: float, sets_won: int, games_won: int,
                 Tie_Break_won: int, missed_serves: int, serves_served: int, points: int,
                 type_of_tournament_won: str, tournaments_won: int,  service_failure: int, total_points: int, total_games_won: int, total_sets_won:int, total_tournaments_won: int):
        self._id = player_id
        self._luck = luck
        self._technique = technique
        self._positioning = positioning
        self._sets_won = sets_won
        self._games_won = games_won
        self._Tie_Break_won = Tie_Break_won
        self._missed_serves = missed_serves
        self._serves_served = serves_served
        self._points = points
        self._type_of_tournament_won = type_of_tournament_won
        self._tournaments_won = tournaments_won
        self._service = False
        self._subtractor = False
        self._service_failure = service_failure
        self._total_points = total_points
        self._total_games_won = total_games_won
        self._total_sets_won = total_sets_won
        self._total_tournaments_won = total_tournaments_won


    # Métodos Getter
    def get_player_id(self) -> str:
        return self._id
    
    def get_luck(self) -> float:
        return self._luck

    def get_technique(self) -> int:
        return self._technique

    def get_positioning(self) -> float:
        return self._positioning

    def get_sets_won(self) -> int:
        return self._sets_won

    def get_games_won(self) -> int:
        return self._games_won

    def get_TieBreak(self) -> int:
        return self._Tie_Break_won

    def get_missed_serves(self) -> int:
        return self._missed_serves

    def get_serves_served(self) -> int:
        return self._serves_served

    def get_points(self) -> int:
        return self._points

    def get_type_of_tournament_won(self) -> str:
        return self._type_of_tournament_won

    def get_tournaments_won(self) -> int:
        return self._tournaments_won

    def get_service(self) -> bool:
        return self._service

    def get_substractor(self) -> bool:
        return self._subtractor
      
    def get_service_failure(self) -> int:
        return self._service_failure
    
    def get_total_points(self):
        return self._total_points

    def get_total_games_won(self):
        return self._total_games_won

    def get_total_sets_won(self):
        return self._total_sets_won

    def get_total_tournaments_won(self):
        return self._total_tournaments_won
    
    # Métodos Setter
    def set_player_id(self, player_id: str) -> None:
        self._id = player_id
        
    def set_luck(self, luck: float) -> None:
        self._luck = luck

    def set_technique(self, technique: int) -> None:
        self._technique = technique

    def set_positioning(self, positioning: float) -> None:
        self._positioning = positioning

    def set_sets_won(self, sets_won: int) -> None:
        self._sets_won = sets_won

    def set_games_won(self, draws_won: int) -> None:
        self._games_won = draws_won

    def set_TieBreak(self, service_faults: int) -> None:
        self._Tie_Break_won = service_faults

    def set_missed_serves(self, missed_serves: int) -> None:
        self._missed_serves = missed_serves

    def set_serves_served(self, serves_served: int) -> None:
        self._serves_served = serves_served

    def set_points(self, points: int) -> None:
        self._points = points

    def set_type_of_tournament_won(self, type_of_tournament_won: str) -> None:
        self._type_of_tournament_won = type_of_tournament_won

    def set_tournaments_won(self, tournaments_won: int) -> None:
        self._tournaments_won = tournaments_won

    def set_service(self, service: bool) -> bool:
        self._service = service

    def set_substractor(self, substractor: bool) -> bool:
        self._subtractor = substractor

    def set_service_failure(self, service_failure: int) -> int:
        self._service = service_failure

    def set_total_points(self, value):
        self._total_points = value

    def set_total_games_won(self, value):
        self._total_games_won = value

    def set_total_sets_won(self, value):
        self._total_sets_won = value

    def set_total_tournaments_won(self, value):
        self._total_tournaments_won = value

    def print_player_data(self):
        print("Player Data:")
        print("-------------------------------------------------")
        print("| {:<20} | {:<10} |".format("Attribute", "Value"))
        print("-------------------------------------------------")
        print("| {:<20} | {:<10} |".format("ID", self._id))
        print("| {:<20} | {:<10.2f} |".format("Luck", self._luck))
        print("| {:<20} | {:<10} |".format("Technique", self._technique))
        print("| {:<20} | {:<10.2f} |".format("Positioning", self._positioning))
        print("| {:<20} | {:<10} |".format("Sets won", self._sets_won))
        print("| {:<20} | {:<10} |".format("Games won", self._games_won))
        print("| {:<20} | {:<10} |".format("Service faults", self._Tie_Break_won))
        print("| {:<20} | {:<10} |".format("Missed serves", self._missed_serves))
        print("| {:<20} | {:<10} |".format("Serves served", self._serves_served))
        print("| {:<20} | {:<10} |".format("Points", self._points))
        print("| {:<20} | {:<10} |".format("Type tournament won", self._type_of_tournament_won))
        print("| {:<20} | {:<10} |".format("Tournaments won", self._tournaments_won))
        print("| {:<20} | {:<10} |".format("Is service", self._service))
        print("| {:<20} | {:<10} |".format("Service Failure", self._service_failure))
        print("| {:<20} | {:<10} |".format("Is substractor", self._subtractor))
        print("| {:<20} | {:<10} |".format("Total points", self._total_points))
        print("| {:<20} | {:<10} |".format("Total games won", self._total_games_won))
        print("| {:<20} | {:<10} |".format("Total sets won", self._total_sets_won))
        print("| {:<20} | {:<10} |".format("Total tournaments won", self._total_tournaments_won))
        print("-------------------------------------------------")



from Player import Player


class ResultGame:
    def __init__(
            self, 
            tournament_winner_with_score: Player, 
            player_with_most_games_won: 'Player',
            player_with_most_sets_won: 'Player',
            player_with_most_tournaments_won:'Player'
            
            
            #scores_per_game: dict = None,
            #initial_raffle_winner_per_game: dict = None
            ):
        
        self._tournament_winner_with_score = tournament_winner_with_score
        self._player_with_most_games_won = player_with_most_games_won
        self._player_with_most_sets_won = player_with_most_sets_won #player_with_most_sets_won
        self._player_with_most_tournaments_won = player_with_most_tournaments_won #player_with_most_tournaments_won
        
        self._tournament_winner_with_score = None #tournament_winner_with_score if tournament_winner_with_score is not None else {}
        self._scores_per_game = None #scores_per_game if scores_per_game is not None else {}
        self._initial_raffle_winner_per_game = None #initial_raffle_winner_per_game if initial_raffle_winner_per_game is not None else {}

    # Getters
    def get_player_with_most_games_won(self) -> 'Player':
        return self._player_with_most_games_won

    def get_player_with_most_sets_won(self) -> 'Player':
        return self._player_with_most_sets_won

    def get_player_with_most_tournaments_won(self) -> 'Player':
        return self._player_with_most_tournaments_won

    def get_scores_per_game(self) -> dict:
        return self._scores_per_game

    def get_initial_raffle_winner_per_game(self) -> dict:
        return self._initial_raffle_winner_per_game

    def get_tournament_winner_with_score(self) -> dict:
        return self._tournament_winner_with_score

    # Setters
    def set_player_with_most_games_won(self, player: 'Player'):
        self._player_with_most_games_won = player

    def set_player_with_most_sets_won(self, player: 'Player'):
        self._player_with_most_sets_won = player

    def set_player_with_most_tournaments_won(self, player: 'Player'):
        self._player_with_most_tournaments_won = player

    def set_scores_per_game(self, game_id: str, score: str):
        self._scores_per_game[game_id] = score

    def set_initial_raffle_winner_per_game(self, game_id: str, player: 'Player'):
        self._initial_raffle_winner_per_game[game_id] = player

    def set_tournament_winner_with_score(self, tournament_id: str, player: 'Player', score: str):
        self._tournament_winner_with_score[tournament_id] = (player, score)

    # Método para imprimir los resultados en forma de tabla
    def print_results(self):
        print("+------------------------------------------+")
        print("|              Resultados del Juego        |")
        print("+------------------------------------------+")
        print("| {:<36} | {:<10} |".format("Ganador de cada Torneo", str(self._player_with_most_games_won.print_player_data())))
        print("| {:<36} | {:<10} |".format("Jugador con más juegos ganados", str(self._player_with_most_games_won.get_total_games_won())))
        print("| {:<36} | {:<10} |".format("Jugador con más sets ganados", str(self._player_with_most_sets_won.get_total_sets_won())))
        print("| {:<36} | {:<10} |".format("Jugador con más torneos ganados", str(self._player_with_most_tournaments_won.get_total_tournaments_won())))
        print("+------------------------------------------+")

        """print("\n+------------------------------------------+")
        print("|        Puntaje de los jugadores por juego        |")
        print("+------------------------------------------+")
        for game_id, score in self._scores_per_game:
            print("| {:<36} | {:<10} |".format(game_id, score))
        print("+------------------------------------------+")"""

        """print("\n+------------------------------------------+")
        print("|  Jugador que ganó el sorteo inicial por juego |")
        print("+------------------------------------------+")
        for game_id, player in self._initial_raffle_winner_per_game:
            print("| {:<36} | {:<10} |".format(game_id, str(player)))
        print("+------------------------------------------+")"""

        """print("\n+------------------------------------------+")
        print("|         Ganador de cada torneo y puntaje         |")
        print("+------------------------------------------+")
        for tournament_id, player, score in self._tournament_winner_with_score:
            print("| {:<20} | {:<10} | {:<5} |".format(tournament_id, str(player), score))
        print("+------------------------------------------+")"""


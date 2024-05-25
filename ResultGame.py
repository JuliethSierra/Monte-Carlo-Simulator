from Player import Player


class ResultGame:
    def __init__(
            self, 
            tournament_winner_with_score: Player, 
            player_with_most_games_won: 'Player',
            player_with_most_sets_won: 'Player',
            player_with_most_tournaments_won:'Player',
            player_winner_game: 'Player',
            player_loser_game: 'Player'
            ):
        
        self._tournament_winner_with_score = tournament_winner_with_score
        self._player_with_most_games_won = player_with_most_games_won
        self._player_with_most_sets_won = player_with_most_sets_won 
        self._player_with_most_tournaments_won = player_with_most_tournaments_won 
        self._player_winne_game = player_winner_game
        self._player_loser_game = player_loser_game

    # Getters
    def get_tournament_winner_with_score(self) -> 'Player':
        return self._tournament_winner_with_score

    def get_player_with_most_games_won(self) -> 'Player':
        return self._player_with_most_games_won

    def get_player_with_most_sets_won(self) -> 'Player':
        return self._player_with_most_sets_won

    def get_player_with_most_tournaments_won(self) -> 'Player':
        return self._player_with_most_tournaments_won

    def get_player_winner_game(self) -> 'Player':
        return self._player_winne_game

    def get_player_loser_game(self) -> 'Player':
        return self._player_loser_game

    # Setters
    def set_tournament_winner_with_score(self, tournament_winner_with_score: 'Player'):
        self._tournament_winner_with_score = tournament_winner_with_score

    def set_player_with_most_games_won(self, player_with_most_games_won: 'Player'):
        self._player_with_most_games_won = player_with_most_games_won

    def set_player_with_most_sets_won(self, player_with_most_sets_won: 'Player'):
        self._player_with_most_sets_won = player_with_most_sets_won

    def set_player_with_most_tournaments_won(self, player_with_most_tournaments_won: 'Player'):
        self._player_with_most_tournaments_won = player_with_most_tournaments_won

    def set_player_winner_game(self, player_winner_game: 'Player'):
        self._player_winner_game = player_winner_game

    def set_player_loser_game(self, player_loser_game: 'Player'):
        self._player_loser_game = player_loser_game
        
    
    # Método para imprimir los resultados en forma de tabla
    def print_results(self):
        print("+------------------------------------------+")
        print("|              Resultados del Juego        |")
        print("+------------------------------------------+")
        print("| {:<36} | {:<10} |".format("Ganador de cada Torneo", str(self._tournament_winner_with_score.get_player_id())))
        print("| {:<36} | {:<10} |".format("Jugador con más juegos ganados", str(self._player_with_most_games_won.get_total_games_won())))
        print("| {:<36} | {:<10} |".format("Jugador con más sets ganados", str(self._player_with_most_sets_won.get_total_sets_won())))
        print("| {:<36} | {:<10} |".format("Jugador con más torneos ganados", str(self._player_with_most_tournaments_won.get_total_tournaments_won())))
        print("| {:<36} | {:<10} |".format("Jugador ganador", str(self._player_winne_game.get_points())))
        print("| {:<36} | {:<10} |".format("Jugador perdedor", str(self._player_loser_game.get_points())))
        print("+------------------------------------------+")


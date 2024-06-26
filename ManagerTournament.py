import random
from Player import Player
from Game import Game
from ResultGame import ResultGame
from Set import Set
from Tournament import Tournament

class ManagerTournament:

    def __init__(self):
        self.finalResults = []
        pass
    
    #Metodo para crear un torneo
    def create_tournament(self):
        tournament = Tournament(tournament_id=0, tournament_type= "", tournament_winner= None, sets= None)
        return tournament
    
    #Metodo para crear un Juego
    def create_game(self):
        game = Game(game_id=0, players= [], game_winner= None)
        return game
    
    #Metodo para crear un Set
    def create_set(self):
        set = Set(set_id=0, games= [], set_winner= None)
        return set
    
    #Metodo para determinar el tipo de torneo que se va a jugar
    def assign_tournament_type(self, tournament: Tournament) -> None:
        tournament.set_tournament_type(random.choice(["Best of 5", "Best of 3"]))

    #Metodo para crear a los jugadores
    def create_players(self):
        player1 = Player(luck=random.uniform(1, 3), technique=random.randint(10, 30), positioning=random.uniform(1, 3), sets_won=0, games_won=0,
                         Tie_Break_won=0, missed_serves=0, serves_served=0, points=0,
                         type_of_tournament_won="", tournaments_won=0, player_id="001", service_failure=0, total_points=0, total_games_won=0, total_sets_won=0, total_tournaments_won=0)

        player2 = Player(luck=random.uniform(1, 3), technique=random.randint(10, 30), positioning=random.uniform(1, 3), sets_won=0, games_won=0,
                         Tie_Break_won=0, missed_serves=0, serves_served=0, points=0,
                         type_of_tournament_won="", tournaments_won=0, player_id="002",service_failure=0,total_points=0, total_games_won=0, total_sets_won=0, total_tournaments_won=0)

        return player1, player2
    
    #Metodo para realizar el sorteo del servicio al iniciar el juego
    def raffle(self, player1: Player, player2: Player) -> Player:
        player_service = None
        player_subtractor = None

        if player1.get_luck() > player2.get_luck():
            player_service = player1
            player_subtractor = player2
        elif player2.get_luck() > player1.get_luck():
            player_service = player2
            player_subtractor = player1
        else:
            # Si tienen la misma suerte, se realiza el sorteo de nuevo
            self.raffle(player1, player2)

        player_service.set_service(True)
        player_subtractor.set_substractor(True)
        
        player_service.set_substractor(False)
        player_subtractor.set_service(False)
        
        return player_service, player_subtractor
    
  # Método para simular la anotación de un punto
    def get_winner_points(self, player1: Player, player2: Player) -> Player:
        self.set_position_player(player1)
        self.set_position_player(player2)
        score = self.launch()
        if score == 1:
            self.add_player_points(player1)
        else:
            if(self.is_good_position_(player1)):
                if (self.ball_return() == 0):
                    score1 = self.launch()
                    if score1 == 0:
                        if(self.is_good_position_(player2)):
                            if (self.ball_return()==0):
                                self.get_winner_points(player1,player2)
                            elif(self.ball_return()==1):
                                self.add_player_points(player2)
                            else:
                                self.add_player_points(player1)
                        else:
                           self.add_player_points(player1) 
                    else:
                        self.add_player_points(player2)
                elif(self.ball_return() == 1):
                    self.add_player_points(player1)
                else:
                    self.add_player_points(player2)
            else:
                self.add_player_points(player2)


        return player1 if player1.get_points() > player2.get_points() else player2
 
    #Metodo para Simular un juego
    def start_game(self, player1: 'Player', player2: 'Player') -> 'Player':
        player_service: Player = player1
        player_subtractor: Player = player2

        self.set_technique_player(player1)
        self.set_technique_player(player2)

        self.set_position_player(player1)
        self.set_position_player(player2)

        isPlaying = True

        while isPlaying:

            if(self.is_successful_service(player_service) == True):
                self.get_winner_points(player_service,player_subtractor)
            else:
                player_service.set_service_failure(player_service.get_service_failure()+1)

                if(self.double_failure_service(player_service) == True):
                    self.subtract_points(player_service, player_subtractor)

            if player_service.get_points() == 4 or player_subtractor.get_points() == 4:
                if abs(player_service.get_points() - player_subtractor.get_points()) == 2:
                    self.establish_winner_game(player1, player2)
                    break
                elif player_service.get_points() == 4 and player_subtractor.get_points() == 4:
                    self.get_winner_game(player_service, player_subtractor)
                    if abs(player_service.get_points() - player_subtractor.get_points()) == 2:
                        self.establish_winner_game(player1, player2)
                        isPlaying = False

            if player_service.get_points() >= 4 or player_subtractor.get_points() >= 4:
                if abs(player_service.get_points() - player_subtractor.get_points()) >= 2:
                    self.establish_winner_game(player1, player2)
                    isPlaying = False
        player_service, player_subtractor = player_subtractor, player_service    
        return player1 if player1.get_points() > player2.get_points() else player2
        
    #Metodo para añadir puntos a unjugador
    def add_player_points(self, player: 'Player'):
        player.set_points(player.get_points() + 1)
        player.set_total_points(player.get_total_points() + 1)

    #Metodo para definir la tecnica de unn jugador cada vez que va a realizar un servicio
    def set_technique_player(self, player: 'Player'):
        player.set_technique(random.randint(10, 30))
    
    #Metodo para determinar si un servicio es exitoso o no
    def is_successful_service(self, player_service: Player) -> bool:
        self.set_technique_player(player_service)

        if player_service.get_technique() >= 10:
            player_service.set_serves_served(player_service.get_serves_served()+1)
            return True
        else:
            player_service.set_missed_serves(player_service.get_missed_serves()+1)
            return False
    
    #Metodo para definir la posición de unn jugador cada vez que va a realizar un servicio
    def set_position_player(self, player: 'Player'):
        player.set_positioning(random.uniform(1, 3))
    
    #Metodo para determinar si la posición de un jugador es buena o no
    def is_good_position_(self, player_service: Player) -> bool:
        self.set_position_player(player_service)
        if player_service.get_positioning() >= 2:
            return True
        else:
            return False
        
    #Metodo para descontar un punto si un Jugador falla dos veces en el servicio
    def double_failure_service(self, player_service: 'Player'):
        if(player_service.get_service_failure() == 2):
            return True
        else:
            return False

    #Metodo para restr un punto si un jugador falla dos veces en el servicio
    def subtract_points(self, player_service: 'Player', player_substractor: 'Player'):
        player_substractor.set_points(player_substractor.get_points()+1)
        player_service.set_service_failure(0)

    #Metodo para especificar el lugar de la cancha en el que cae la pelota
    def launch(self) -> int:
        field_position = [0.32, 0.07, 0.25, 0.36] 
        scores = [1, 1, 0, 0] 
        # Generamos un número aleatorio entre 0 y 1 para determinar la categoría de precisión
        random_number = random.random()
        score = 0  # Valor predeterminado
        for i in range(len(field_position)):
            if random_number <= field_position[i]:
                score = scores[i]
                break
        return score
    
    #Metodo para definir la calidad de la devolución
    def ball_return(self)->int:
            quality_return = [0.42, 0.27, 0.31] 
            scores = [1, 0, -1] 
            # Generamos un número aleatorio entre 0 y 1 para determinar la categoría de precisión
            random_number = random.random()
            score = 0  # Valor predeterminado
            for i in range(len(quality_return)):
                if random_number <= quality_return[i]:
                    score = scores[i]
                    break
            return score
    
    #Metodo para definir un ganador en caso de empate en un juego
    def get_winner_game(self, player_service: 'Player', player_subtractor: 'Player') -> 'Player':
        advantage_player = None
        self.set_technique_player(player_service)
        self.set_technique_player(player_subtractor)
        while True:
            if advantage_player is None:
                player_service, player_subtractor = player_subtractor, player_service
            else:
                player_service, player_subtractor = advantage_player, player_service if advantage_player == player_subtractor else player_subtractor
            
            if self.is_successful_service(player_service):
                self.get_winner_points(player_service, player_subtractor)
                if advantage_player is None:
                    advantage_player = player_service
                elif advantage_player == player_service:
                    return player_service
                else:
                    advantage_player = None
            else:
                self.subtract_points(player_service, player_subtractor)
                advantage_player = player_subtractor


    #Metodo para Establecer el ganador de un Juego
    def establish_winner_game(self, player1: 'Player', player2: 'Player'):
        if player1.get_points() > player2.get_points():
            player1.set_games_won(player1.get_games_won()+1)
            player1.set_total_games_won(player1.get_total_games_won()+1)
        elif player2.get_points() > player1.get_points():
            player2.set_games_won(player2.get_games_won()+1)
            player2.set_total_games_won(player2.get_total_games_won()+1)


    #Metodo para definir el ganador de un set
    def define_set_winner(self, player1: 'Player', player2: 'Player') -> 'Player':
        player1: Player
        player2: Player
        isPlaying = True

        while isPlaying:
            self.create_game
            self.start_game(player1, player2)

            if (player1.get_games_won() >= 6 or player2.get_games_won() >= 6):
                if abs(player1.get_games_won() - player2.get_games_won()) >= 2:
                    self.establish_winner_Set(player1, player2)
                    isPlaying = False
            if( player1.get_games_won() == 6 and player2.get_games_won() == 6):
                self.tie_break(player1, player2)
                self.establish_winner_Set(player1, player2)
                isPlaying = False
        return player1 if player1.get_games_won() > player2.get_games_won() else player2

    #Metodo para Establecer el ganador de un Set
    def establish_winner_Set(self, player1: 'Player', player2: 'Player')-> None:
        if player1.get_games_won() > player2.get_games_won():
            player1.set_sets_won(player1.get_sets_won()+1)
            player1.set_total_sets_won(player1.get_total_sets_won()+1)
        elif player2.get_games_won() > player1.get_games_won():
            player2.set_sets_won(player2.get_sets_won()+1)
            player2.set_total_sets_won(player2.get_total_sets_won()+1)

    #Metodo para Establecer el ganador de un Set en caso de empate
    def tie_break(self, player1: 'Player', player2: 'Player') -> 'Player':
        player1: Player
        player2: Player
        isPlaying = True

        self.set_technique_player(player1)
        self.set_technique_player(player2)

        while isPlaying:
            if(self.is_successful_service(player1) == True):
                self.get_winner_points(player1,player2)
            else:
                player1.set_service_failure(player1.get_service_failure()+1)

                if(self.double_failure_service(player1) == True):
                    self.subtract_points(player1, player2)

            if player1.get_points() == 7 or player2.get_points() == 7:
                if abs(player1.get_points() - player2.get_points()) == 2:
                    self.establish_winner_game(player1, player2)
                    isPlaying = False

            if player1.get_points() >= 7 or player2.get_points() >= 7:
                if abs(player1.get_points() - player2.get_points()) >= 2:
                    self.establish_winner_game(player1, player2)
                    isPlaying = False
        #player1, player2 = player2, player1
            
        return player1 if player1.get_points() > player2.get_points() else player2
        
    #Metodo para definir el ganador de un Torneo
    def define_tournament_winner(self, player1: 'Player', player2: 'Player', tournament: 'Tournament') -> 'Player':
        self.final_tournament(player1,player2)
        player1: Player
        player2: Player

        self.generate_luck(player1, player2)

        player1, player2 = self.raffle(player1, player2)
        isPlaying = True
        self.assign_tournament_type(tournament)
        while isPlaying:
            
            if tournament.get_tournament_type() == "Best of 5":
                self.define_set_winner(player1, player2)
                if player1.get_sets_won() == 3 or player2.get_sets_won() == 3:
                    self.establish_winner_tournament(player1, player2, tournament)
                    isPlaying = False

            elif tournament.get_tournament_type() == "Best of 3":
                self.define_set_winner(player1, player2)
                if player1.get_sets_won() == 2 or player2.get_sets_won() == 2:
                    self.establish_winner_tournament(player1, player2, tournament)
                    isPlaying = False
            
        return player1 if player1.get_sets_won() > player2.get_sets_won() else player2

    #Metodo para Establecer el ganador de un Torneo
    def establish_winner_tournament(self, player1: 'Player', player2: 'Player', tournament: 'Tournament')-> None:
        if player1.get_sets_won() > player2.get_sets_won():
            player1.set_tournaments_won(player1.get_tournaments_won()+1)

            player1.set_total_tournaments_won(player1.get_total_tournaments_won()+1)
            player1.set_type_of_tournament_won(tournament.get_tournament_type())
            
        elif player2.get_sets_won() > player1.get_sets_won():
            player2.set_tournaments_won(player2.get_tournaments_won()+1)
 
            player2.set_total_tournaments_won(player2.get_total_tournaments_won()+1)
            player2.set_type_of_tournament_won(tournament.get_tournament_type())


    #Metodo para generar la suerte de los jugadores 
    def generate_luck(self, player1: 'Player', player2: 'Player'):
        player1.set_luck(random.uniform(1, 3))
        player2.set_luck(random.uniform(1, 3))

    #Metodo para reestablecer los valores
    def final_tournament(self, player1: 'Player', player2: 'Player'):
        player1.set_points(0)
        player2.set_points(0)
    
        player1.set_sets_won(0)
        player2.set_sets_won(0)

        player1.set_games_won(0)
        player2.set_games_won(0)

        player1.set_serves_served(0)
        player2.set_serves_served(0)

        player1.set_tournaments_won(0)
        player2.set_tournaments_won(0)

        player1.set_TieBreak(0)
        player2.set_TieBreak(0)

        player1.set_missed_serves(0)
        player2.set_missed_serves(0)

        player1.set_serves_served(0)
        player2.set_serves_served(0)

        player1.set_type_of_tournament_won("")
        player2.set_type_of_tournament_won("")

        player1.set_service(False)
        player1.set_substractor(False)
        player2.set_service(False)
        player2.set_substractor(False)

        player1.set_service_failure(0)
        player2.set_service_failure(0)

    #Metodo para Jugar varios torneos
    def playRounds(self, player1: 'Player', player2: 'Player',tournament: 'Tournament'):
        self.final_tournament(player1, player2)
        winner = self.define_tournament_winner(player1, player2, tournament)
        return winner

    #Metodo para Encontrar al jugador con más juagos ganados en cada torneo
    def get_player_more_victories_game(self, player1: 'Player', player2: 'Player') -> 'Player':
        if player1.get_total_games_won() > player2.get_total_games_won():
            return player1
        else:
            return player2

    #Metodo para Encontrar al jugador con más sets ganados
    def get_player_more_victories_set(self, player1: 'Player', player2: 'Player') -> 'Player':
        if player1.get_total_sets_won() > player2.get_total_sets_won():
            return player1
        else:
            return player2
    #Metodo para Encontrar al jugador con más Torneos ganados
    def get_player_more_victories_tournament(self, player1: 'Player', player2: 'Player') -> 'Player':
        if player1.get_total_tournaments_won() > player2.get_total_tournaments_won():
            return player1
        else:
            return player2
    #Metodo para Obtener los puntajes de los jugadores en cada unos de los juegos
    def get_player_winner_and_loser_game(self, player1: 'Player', player2: 'Player'):
        if player1.get_points() > player2.get_points():
            winner = player1
            loser = player2
            return winner, loser
        else:
            winner = player2
            loser = player1
            return winner, loser

    # Método para simular múltiples juegos
    def simulacion(self, player1: 'Player', player2: 'Player', tournament: 'Tournament', num):
        resultados = []

        for _ in range(num):
            resultado = self.simulacion_round(player1, player2, tournament)
            resultados.append(resultado)
        return resultados


    # Función para simular un juego
    def simulacion_round(self, player1: 'Player', player2: 'Player', tournament: 'Tournament') -> ResultGame:

        tournament_winner_with_score: Player = self.playRounds(player1, player2, tournament)
        player_with_most_games_won: Player = self.get_player_more_victories_game(player1, player2)
        player_with_most_sets_won: Player = self.get_player_more_victories_set(player1, player2)
        player_with_most_tournaments_won: Player = self.get_player_more_victories_tournament(player1, player2)
        player_winner_game, player_loser_game = self.get_player_winner_and_loser_game(player1, player2)

        resultGame = ResultGame(
            Player(tournament_winner_with_score.get_player_id(),tournament_winner_with_score.get_luck(), tournament_winner_with_score.get_technique(), tournament_winner_with_score.get_positioning(), tournament_winner_with_score.get_sets_won(), tournament_winner_with_score.get_games_won(), tournament_winner_with_score.get_TieBreak(), tournament_winner_with_score.get_missed_serves(), tournament_winner_with_score.get_serves_served(), tournament_winner_with_score.get_points(), tournament_winner_with_score.get_type_of_tournament_won(), tournament_winner_with_score.get_tournaments_won(), tournament_winner_with_score.get_service_failure(), tournament_winner_with_score.get_total_points(), tournament_winner_with_score.get_total_games_won(), tournament_winner_with_score.get_total_sets_won(), tournament_winner_with_score.get_total_tournaments_won()),
            Player(player_with_most_games_won.get_player_id(),player_with_most_games_won.get_luck(), player_with_most_games_won.get_technique(), player_with_most_games_won.get_positioning(), player_with_most_games_won.get_sets_won(), player_with_most_games_won.get_games_won(), player_with_most_games_won.get_TieBreak(), player_with_most_games_won.get_missed_serves(), player_with_most_games_won.get_serves_served(), player_with_most_games_won.get_points(), player_with_most_games_won.get_type_of_tournament_won(), player_with_most_games_won.get_tournaments_won(), player_with_most_games_won.get_service_failure(), player_with_most_games_won.get_total_points(), player_with_most_games_won.get_total_games_won(), player_with_most_games_won.get_total_sets_won(), player_with_most_games_won.get_total_tournaments_won()),
            Player(player_with_most_sets_won.get_player_id(),player_with_most_sets_won.get_luck(), player_with_most_sets_won.get_technique(), player_with_most_sets_won.get_positioning(), player_with_most_sets_won.get_sets_won(), player_with_most_sets_won.get_games_won(), player_with_most_sets_won.get_TieBreak(), player_with_most_sets_won.get_missed_serves(), player_with_most_sets_won.get_serves_served(), player_with_most_sets_won.get_points(), player_with_most_sets_won.get_type_of_tournament_won(), player_with_most_sets_won.get_tournaments_won(), player_with_most_sets_won.get_service_failure(), player_with_most_sets_won.get_total_points(), player_with_most_sets_won.get_total_games_won(), player_with_most_sets_won.get_total_sets_won(), player_with_most_sets_won.get_total_tournaments_won()),
            Player(player_with_most_tournaments_won.get_player_id(),player_with_most_tournaments_won.get_luck(), player_with_most_tournaments_won.get_technique(), player_with_most_tournaments_won.get_positioning(), player_with_most_tournaments_won.get_sets_won(), player_with_most_tournaments_won.get_games_won(), player_with_most_tournaments_won.get_TieBreak(), player_with_most_tournaments_won.get_missed_serves(), player_with_most_tournaments_won.get_serves_served(), player_with_most_tournaments_won.get_points(), player_with_most_tournaments_won.get_type_of_tournament_won(), player_with_most_tournaments_won.get_tournaments_won(), player_with_most_tournaments_won.get_service_failure(), player_with_most_tournaments_won.get_total_points(), player_with_most_tournaments_won.get_total_games_won(), player_with_most_tournaments_won.get_total_sets_won(), player_with_most_tournaments_won.get_total_tournaments_won()),
            Player(player_winner_game.get_player_id(),player_winner_game.get_luck(), player_winner_game.get_technique(), player_winner_game.get_positioning(), player_winner_game.get_sets_won(), player_winner_game.get_games_won(), player_winner_game.get_TieBreak(), player_winner_game.get_missed_serves(), player_winner_game.get_serves_served(), player_winner_game.get_points(), player_winner_game.get_type_of_tournament_won(), player_winner_game.get_tournaments_won(), player_winner_game.get_service_failure(), player_winner_game.get_total_points(), player_winner_game.get_total_games_won(), player_winner_game.get_total_sets_won(), player_winner_game.get_total_tournaments_won()),
            Player(player_loser_game.get_player_id(),player_loser_game.get_luck(), player_loser_game.get_technique(), player_loser_game.get_positioning(), player_loser_game.get_sets_won(), player_loser_game.get_games_won(), player_loser_game.get_TieBreak(), player_loser_game.get_missed_serves(), player_loser_game.get_serves_served(), player_loser_game.get_points(), player_loser_game.get_type_of_tournament_won(), player_loser_game.get_tournaments_won(), player_loser_game.get_service_failure(), player_loser_game.get_total_points(), player_loser_game.get_total_games_won(), player_loser_game.get_total_sets_won(), player_loser_game.get_total_tournaments_won())
        )
        return resultGame

    def print_player_data(self, player: 'Player') -> None:
        player.print_player_data()

    def print_set_data(self, set_obj: 'Set') -> None:
        set_obj.print_set_data()

    def print_game_data(self, game: 'Game') -> None:
        game.print_game_data()

    def print_tournament_data(self, tournament: 'Tournament') -> None:
        tournament.print_tournament_data()




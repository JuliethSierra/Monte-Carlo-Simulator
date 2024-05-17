import random
from Player import Player
from Game import Game
from Set import Set
from Tournament import Tournament

class ManagerTournament:
    def __init__(self):
        pass
#Metodo para determinar el tipo de torneo que se va a jugar
    def assign_tournament_type(self, tournament: Tournament) -> None:
        tournament.set_tournament_type(random.choice(["Best of 5", "Best of 3"]))

#Metodo para crear a los jugadores
    def create_players(self):
        player1 = Player(luck=3, technique=20, positioning=3, sets_won=0, games_won=0,
                         Tie_Break_won=0, missed_serves=0, serves_served=0, points=0,
                         type_of_tournament_won="", tournaments_won=0, player_id="001", service_failure=0)

        player2 = Player(luck=1, technique=0, positioning=3, sets_won=0, games_won=0,
                         Tie_Break_won=0, missed_serves=0, serves_served=0, points=0,
                         type_of_tournament_won="", tournaments_won=0, player_id="002",service_failure=0)

        return player1, player2
    
#Metodo para realizar el sorteo del servicio al iniciar el juego
    def raffle(self, player1: Player, player2: Player) -> Player:
        if player1.get_luck() > player2.get_luck():
            player_service = player1
            player_subtractor = player2

            player_service.set_service(True)
            player_subtractor.set_substractor(True)

            player_service.set_substractor(False)
            player_subtractor.set_service(False)

        elif player2.get_luck() > player1.get_luck():
            player_service = player2
            player_subtractor = player1

            player_service.set_service(True)
            player_subtractor.set_substractor(True)

            player_service.set_substractor(False)
            player_subtractor.set_service(False) 
        else:
            # Si tienen la misma suerte, se realiza el sorteo de nuevo
            self.raffle(player1, player2)
        return player_service, player_subtractor


  # Método para simular la anotación de un punto
    def start_game(self, player_service: Player, player_subtract: Player) -> Player:
        print("juego")
        #------------ pendiente player_service, player_subtract = self.raffle(player1, player2)
        if self.is_successful_service(player_service):
            score = self.launch()
            print("score",score)
            if score == 1:
                player_service.set_points(player_service.get_points() + 1)
            else:
                if (self.ball_return()==0):
                    print("Regular1111111111")
                    score1 = self.launch()
                    print("score", score1)
                    if score1 == 0:
                        print("Hola")
                        if (self.ball_return()==0):
                            print("Regular")
                            self.start_game(player1,player2)
                        elif(self.ball_return()==1):
                            print("Buena")
                            player_subtract.set_points(player_subtract.get_points() + 1)
                        else:
                            print("Error")
                            player_service.set_points(player_service.get_points() + 1) 
                    else:
                        player_subtract.set_points(player_subtract.get_points() + 1)
                elif(self.ball_return()==1):
                    print("Buena111111111111")
                    player_service.set_points(player_service.get_points() + 1)
                else:
                    print("Error1111111111")
                    player_subtract.set_points(player_subtract.get_points() + 1)        
        else:
            player_service.set_service_failure(player_service.get_service_failure() + 1)
            #Retorna el jugador que anotó punto
        return player1 if player1.get_points() > player2.get_points() else player2
 
 #Metodo para Simular un juego
    """   def start_game(self, player1: 'Player', player2: 'Player') -> 'Player':
        player_service, player_subtractor = self.raffle(player1, player2)
        if(self.is_successful_service(player_service) == True):
            self.launch()
        else:
            player_service.set_service_failure(player_service.get_service_failure()+1)
        return player1
        """
    
#Metodo para determinar si un servicio es exitoso o no
    def is_successful_service(self, player_service: Player) -> bool:
        #la tecnica se genera de forma aleatoria!!!
        player_service.set_technique(20)
        if player_service.get_technique() >= 15:
            player_service.set_serves_served(player_service.get_serves_served()+1)
            return True
        else:
            player_service.set_missed_serves(player_service.get_missed_serves()+1)
            return False
        
    
#Metodo para descontar un punto si un Jugador falla dos veces en el servicio
    def double_failure_service(self, player_service: 'Player',  player_subtractor: 'Player') -> None:
        if(player_service.get_service_failure() == 2):
            player_subtractor.set_points(player_subtractor.get_points()+1)
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
        
    def print_player_data(self, player: 'Player') -> None:
        player.print_player_data()

    def print_set_data(self, set_obj: 'Set') -> None:
        set_obj.print_set_data()

    def print_game_data(self, game: 'Game') -> None:
        game.print_game_data()

    def print_tournament_data(self, tournament: 'Tournament') -> None:
        tournament.print_tournament_data()


# Ejemplo de uso
manager = ManagerTournament()
player1, player2 = manager.create_players()

manager.start_game(player1, player2)
# Imprimir datos del jugador 1
print("Player 1 Data:")
manager.print_player_data(player1)
# Imprimir datos del jugador 1
print("Player 2 Data:")
manager.print_player_data(player2)

# Crear un set y un juego de muestra
game1 = Game(game_id="Game1", players=[player1, player2], game_winner=player1)
set1 = Set(set_id="Set1", games=[game1], set_winner=player1)

tournament = Tournament(tournament_id=1, tournament_type="", tournament_winner=player1, sets=[])
manager.assign_tournament_type(tournament)

# Imprimir datos del juego
print("\nGame 1 Data:")
manager.print_game_data(game1)

# Imprimir datos del set
print("\nSet 1 Data:")
manager.print_set_data(set1)

# Imprimir datos del Torneo
print("\nTournament 1 Data:")
manager.print_tournament_data(tournament)




import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from ResultGame import ResultGame
from ManagerTournament import ManagerTournament

class TournamentInterface:
    resultsGame = [] 

    def __init__(self, root):
        self.root = root
        self.root.title("Tournament Interface")
        
        # Establecer tamaño de la ventana
        self.root.geometry("600x400")
        
        # Centrar la ventana en la pantalla
        self.center_window()

        # Configurar el diseño
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=5)

        # Crear y colocar entrada de número
        self.number_label = tk.Label(self.frame, text="Ingrese un número de tonrneos:")
        self.number_label.grid(row=0, column=0, pady=5, padx=5)

        self.number_entry = tk.Entry(self.frame)
        self.number_entry.grid(row=0, column=1, pady=5, padx=5)

        # Crear botón para enviar el número
        self.submit_button = tk.Button(self.frame, text="Jugar Torneo", command=self.start_tournament)
        self.submit_button.grid(row=1, columnspan=2, pady=5)

        # Crear botón para salir de la aplicación
        self.exit_button = tk.Button(self.frame, text="Salir", command=self.root.quit)
        self.exit_button.grid(row=2, columnspan=2, pady=5)

        # Crear etiqueta para mostrar resultado
        self.result_label = tk.Label(self.frame, text="")
        self.result_label.grid(row=3, columnspan=2, pady=5)

        # Instancia de ManagerTournament
        self.manager_tournament = ManagerTournament()

        # Crear marco para la imagen
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(side="bottom", pady=5)

        # Cargar imagen de raqueta de tenis
        self.load_image()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def load_image(self):
        image_path = "tennis_racket.jpg"
        self.image = Image.open(image_path)
        
        # Redimensionar la imagen a un tamaño más grande
        self.image = self.image.resize((300, 300), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)

        # Crear y colocar etiqueta de imagen
        self.image_label = tk.Label(self.image_frame, image=self.photo)
        self.image_label.pack(pady=5)

    def start_tournament(self):
        number = self.number_entry.get()
        if number.isdigit():
            tournament = self.manager_tournament.create_tournament()
            player1, player2 = self.manager_tournament.create_players()
            self.resultsGame = self.manager_tournament.simulacion(player1, player2, tournament, int(number))  # Llamada a un método de ManagerTournament
            self.show_results_panel(self.resultsGame)
        else:
            self.result_label.config(text="Por favor, ingrese un número válido.")

            
    def show_results_panel(self, result):
        # Ocultar el frame actual
        self.frame.pack_forget()
        self.image_frame.pack_forget()
        
        # Crear un nuevo frame para mostrar los resultados
        self.results_frame = tk.Frame(self.root)
        self.results_frame.pack(pady=5)
        
        # Crear y colocar los botones con los resultados
        buttons_texts = [
            "Ganador de cada Torneo",
            "Jugador con más juegos ganados",
            "Jugador con más sets ganados",
            "Jugador con más torneos ganados",
            "Puntajes finales",
            "Mostrar grafica de puntajes"
        ]
        
        methods = [
            self.show_tournament_winner,
            self.show_most_games_won,
            self.show_most_sets_won,
            self.show_most_tournaments_won,
            self.show_game_winner_and_loser,
            self.show_points_graph
        ]
        
        for i, text in enumerate(buttons_texts):
            button = tk.Button(self.results_frame, text=text, command=methods[i])
            button.grid(row=i, column=0, pady=5)
        
        # Botón para volver al panel original
        back_button = tk.Button(self.results_frame, text="Volver", command=self.show_main_panel)
        back_button.grid(row=len(buttons_texts), columnspan=2, pady=5)

    def show_main_panel(self):
        # Ocultar el frame de resultados
        self.results_frame.pack_forget()
        
        # Mostrar el frame original
        self.frame.pack(pady=5)
        self.image_frame.pack(side="bottom", pady=5)

    def show_tournament_winner(self):
        # Ocultar el frame de resultados
        self.results_frame.pack_forget()

        # Crear un nuevo frame para el detalle
        self.detail_frame = tk.Frame(self.root)
        self.detail_frame.pack(pady=5)

        # Crear y colocar el título
        title_label = tk.Label(self.detail_frame, text="Ganador de cada Torneo", font=("Helvetica", 16))
        title_label.pack(pady=5)

        # Crear el frame para la tabla y las barras de desplazamiento
        tree_frame = tk.Frame(self.detail_frame)
        tree_frame.pack(pady=5)

        # Crear la tabla
        tree = ttk.Treeview(tree_frame, columns=("ID", "Sets won", "Games won", "Points", "Type of tournament won", "Tournaments won"))
        tree.heading("#0", text="Player")
        tree.heading("ID", text="ID")
        tree.heading("Sets won", text="Sets won")
        tree.heading("Games won", text="Games won")
        tree.heading("Points", text="Points")
        tree.heading("Type of tournament won", text="Type of tournament won")
        tree.heading("Tournaments won", text="Tournaments won")
        tree.column("#0", width=0, stretch=tk.NO) 

        # Agregar los resultados a la tabla
        for result in self.resultsGame:
            player_data = result.get_tournament_winner_with_score()
            
            tree.insert("", "end", text=player_data.get_player_id(), values=(
                player_data.get_player_id(), 
                player_data.get_sets_won(), 
                player_data.get_games_won(), 
                player_data.get_points(),
                player_data.get_type_of_tournament_won(), 
                player_data.get_tournaments_won()
            ))

        # Configurar las barras de desplazamiento vertical y horizontal
        vsb = tk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        hsb = tk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Colocar la tabla en el frame
        tree.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Botón para volver al panel de resultados
        back_button = tk.Button(self.detail_frame, text="Volver", command=self.show_results_panel_from_detail)
        back_button.pack(pady=5)



    def show_most_games_won(self):
        # Ocultar el frame de resultados
        self.results_frame.pack_forget()

        # Crear un nuevo frame para el detalle
        self.detail_frame = tk.Frame(self.root)
        self.detail_frame.pack(pady=5)

        # Crear y colocar el título
        title_label = tk.Label(self.detail_frame, text="Jugador con más juegos ganados", font=("Helvetica", 16))
        title_label.pack(pady=5)

        # Crear el frame para la tabla y las barras de desplazamiento
        tree_frame = tk.Frame(self.detail_frame)
        tree_frame.pack(pady=5)

        # Crear la tabla
        tree = ttk.Treeview(tree_frame, columns=("ID", "Total Games won"))
        tree.heading("ID", text="ID")
        tree.heading("Total Games won", text="Total Games won")
        tree.column("#0", width=0, stretch=tk.NO)  # Eliminar la columna "Player"

        # Agregar el último resultado a la tabla
        if self.resultsGame:
            last_result = self.resultsGame[-1]
            player_data = last_result.get_player_with_most_games_won()
            
            tree.insert("", "end", values=(
                player_data.get_player_id(), 
                player_data.get_total_games_won(), 
            ))

        # Configurar las barras de desplazamiento vertical y horizontal
        vsb = tk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        hsb = tk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Colocar la tabla en el frame
        tree.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Botón para volver al panel de resultados
        back_button = tk.Button(self.detail_frame, text="Volver", command=self.show_results_panel_from_detail)
        back_button.pack(pady=5)



    def show_most_sets_won(self):
        # Ocultar el frame de resultados
        self.results_frame.pack_forget()

        # Crear un nuevo frame para el detalle
        self.detail_frame = tk.Frame(self.root)
        self.detail_frame.pack(pady=5)

        # Crear y colocar el título
        title_label = tk.Label(self.detail_frame, text="Jugador con más sets ganados", font=("Helvetica", 16))
        title_label.pack(pady=5)

        # Crear el frame para la tabla y las barras de desplazamiento
        tree_frame = tk.Frame(self.detail_frame)
        tree_frame.pack(pady=5)

        # Crear la tabla
        tree = ttk.Treeview(tree_frame, columns=("ID", "Total Sets won"))
        tree.heading("#0", text="Player")
        tree.heading("ID", text="ID")
        tree.heading("Total Sets won", text="Total Sets won")
        tree.column("#0", width=0, stretch=tk.NO) 

        # Agregar el último resultado a la tabla
        if self.resultsGame:
            last_result = self.resultsGame[-1]
            player_data = last_result.get_player_with_most_sets_won()
            
            tree.insert("", "end", text=player_data.get_player_id(), values=(
                player_data.get_player_id(), 
                player_data.get_total_sets_won(), 
            ))

        # Configurar las barras de desplazamiento vertical y horizontal
        vsb = tk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        hsb = tk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Colocar la tabla en el frame
        tree.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Botón para volver al panel de resultados
        back_button = tk.Button(self.detail_frame, text="Volver", command=self.show_results_panel_from_detail)
        back_button.pack(pady=5)

    def show_most_tournaments_won(self):
                # Ocultar el frame de resultados
        self.results_frame.pack_forget()

        # Crear un nuevo frame para el detalle
        self.detail_frame = tk.Frame(self.root)
        self.detail_frame.pack(pady=5)

        # Crear y colocar el título
        title_label = tk.Label(self.detail_frame, text="Jugador con más Torneos ganados", font=("Helvetica", 16))
        title_label.pack(pady=5)

        # Crear el frame para la tabla y las barras de desplazamiento
        tree_frame = tk.Frame(self.detail_frame)
        tree_frame.pack(pady=5)

        # Crear la tabla
        tree = ttk.Treeview(tree_frame, columns=("ID", "Total Tournaments won"))
        tree.heading("#0", text="Player")
        tree.heading("ID", text="ID")
        tree.heading("Total Tournaments won", text="Total Tournaments won")
        tree.column("#0", width=0, stretch=tk.NO) 

        # Agregar el último resultado a la tabla
        if self.resultsGame:
            last_result = self.resultsGame[-1]
            player_data = last_result.get_player_with_most_tournaments_won()
            
            tree.insert("", "end", text=player_data.get_player_id(), values=(
                player_data.get_player_id(), 
                player_data.get_total_tournaments_won(), 
            ))

        # Configurar las barras de desplazamiento vertical y horizontal
        vsb = tk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        hsb = tk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Colocar la tabla en el frame
        tree.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Botón para volver al panel de resultados
        back_button = tk.Button(self.detail_frame, text="Volver", command=self.show_results_panel_from_detail)
        back_button.pack(pady=5)

    def show_game_winner_and_loser(self):
        # Ocultar el frame de resultados
        self.results_frame.pack_forget()

        # Crear un nuevo frame para el detalle
        self.detail_frame = tk.Frame(self.root)
        self.detail_frame.pack(pady=5)

        # Crear y colocar el título
        title_label = tk.Label(self.detail_frame, text="Jugadores ganadores y perdedores con puntaje", font=("Helvetica", 16))
        title_label.pack(pady=5)

        # Crear el frame para la tabla y las barras de desplazamiento
        tree_frame = tk.Frame(self.detail_frame)
        tree_frame.pack(pady=5)

        # Crear la tabla con las columnas especificadas
        tree = ttk.Treeview(tree_frame, columns=("ID Ganador", "Puntaje Ganador", "ID Perdedor", "Puntaje Perdedor"))
        tree.heading("#0", text="Juego")
        tree.heading("ID Ganador", text="ID Ganador")
        tree.heading("Puntaje Ganador", text="Puntaje")
        tree.heading("ID Perdedor", text="ID Perdedor")
        tree.heading("Puntaje Perdedor", text="Puntaje")
        tree.column("#0", width=0, stretch=tk.NO) 

        # Insertar los resultados en la tabla
        for i, result in enumerate(self.resultsGame):
            winner_data = result.get_player_winner_game()
            loser_data = result.get_player_loser_game()
            
            tree.insert("", "end", text=f"Juego {i+1}", values=( 
                winner_data.get_player_id(), 
                winner_data.get_sets_won(), 
                loser_data.get_player_id(), 
                loser_data.get_sets_won()
            ))

        # Configurar las barras de desplazamiento vertical y horizontal
        vsb = tk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        hsb = tk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Colocar la tabla en el frame
        tree.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Botón para volver al panel de resultados
        back_button = tk.Button(self.detail_frame, text="Volver", command=self.show_results_panel_from_detail)
        back_button.pack(pady=5)



    def show_detail_panel(self, title):
        # Ocultar el frame de resultados
        self.results_frame.pack_forget()

        # Crear un nuevo frame para el detalle
        self.detail_frame = tk.Frame(self.root)
        self.detail_frame.pack(pady=5)

        # Crear y colocar el título
        title_label = tk.Label(self.detail_frame, text=title, font=("Helvetica", 16))
        title_label.pack(pady=5)

        # Botón para volver al panel de resultados
        back_button = tk.Button(self.detail_frame, text="Volver", command=self.show_results_panel_from_detail)
        back_button.pack(pady=5)

    def show_results_panel_from_detail(self):
        # Ocultar el frame de detalle 
        self.detail_frame.pack_forget()
        
        # Mostrar el frame de resultados
        self.results_frame.pack(pady=5)

    def show_points_graph(self):
        # Recolectar datos para la gráfica
        tournament_ids = list(range(1, len(self.resultsGame) + 1))
        player1_points = [result.get_player_winner_game().get_tournaments_won() for result in self.resultsGame]
        player2_points = [result.get_player_loser_game().get_tournaments_won() for result in self.resultsGame]

        # Crear la gráfica
        plt.figure(figsize=(10, 5))
        plt.plot(tournament_ids, player1_points, marker='o', label='Player 1 Points')
        plt.plot(tournament_ids, player2_points, marker='o', label='Player 2 Points')

        plt.title('Puntos de Jugadores en Cada Torneo')
        plt.xlabel('ID Torneo')
        plt.ylabel('Puntos')
        plt.legend()
        plt.grid(True)

        # Mostrar la gráfica
        plt.show()
        


# Clase principal de la aplicación
def main():
    root = tk.Tk()
    app = TournamentInterface(root)
    root.mainloop()
if __name__ == "__main__":
    main()

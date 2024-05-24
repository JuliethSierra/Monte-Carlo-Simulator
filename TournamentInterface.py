import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ResultGame import ResultGame

# Asumiendo que ManagerTournament está definido en otro archivo llamado ManagerTournament.py
from ManagerTournament import ManagerTournament

class TournamentInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Tournament Interface")
        
        # Establecer tamaño de la ventana
        self.root.geometry("600x400")
        
        # Centrar la ventana en la pantalla
        self.center_window()

        # Configurar el diseño
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # Crear y colocar entrada de número
        self.number_label = tk.Label(self.frame, text="Ingrese un número:")
        self.number_label.grid(row=0, column=0, pady=10)

        self.number_entry = tk.Entry(self.frame)
        self.number_entry.grid(row=0, column=1, pady=5)

        # Crear botón para enviar el número
        self.submit_button = tk.Button(self.frame, text="Jugar Torneo", command=self.start_tournament)
        self.submit_button.grid(row=1, columnspan=2, pady=20)

        # Crear etiqueta para mostrar resultado
        self.result_label = tk.Label(self.frame, text="")
        self.result_label.grid(row=2, columnspan=2, pady=20)

        # Instancia de ManagerTournament
        self.manager_tournament = ManagerTournament()

        # Crear marco para la imagen
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(side="bottom", pady=20)

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
        self.image_label.pack(pady=20)

    def start_tournament(self):
        number = self.number_entry.get()
        if number.isdigit():

            tournament = self.manager_tournament.create_tournament()
            player1, player2 = self.manager_tournament.create_players()
            print("------------------------------------------------------------------------")

            print("Fin Torneo")
            result = self.manager_tournament.simulacion(player1, player2, tournament, int(number))  # Llamada a un método de ManagerTournament
            for i in range(len(result)):
                print("Resultado final torneoooooooooooooooooooooooooooooooooo")
                result[i].print_results()

            print("--------------------------------------------------------------------------")
            #self.result_label.config(text=f"Resultado: {result}")
        else:
            self.result_label.config(text="Por favor, ingrese un número válido.")

# Clase principal de la aplicación
def main():
    root = tk.Tk()
    app = TournamentInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()

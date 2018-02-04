from .Matrix import Matrix 
import re 


class Game: 
    def __init__(self): 
        self.matrix = Matrix(3, 3) 
        self.turn_index = 0 

    def run(self): 
        self.compose_frame()
        self.update_model()

    def compose_frame(self):
        self.matrix.print()

    def update_model(self):
        def set_symbol(coordinate):
            self.matrix[coordinate] = ["X", "O"][self.turn_index % 2]

        while True:
            input_string = input("Enter coordinate: ")

            match = re.match(r"^\(?(?P<x>[1-3]),? ?(?P<y>[1-3])\)?$", input_string)

            if match:
                set_symbol((int(match.group("x")) - 1, int(match.group("y")) - 1))
                break

            match = re.match("^(?P<index>[1-9])$", input_string)

            if match:
                set_symbol(int(match.group("index")) - 1)
                break

            print("Invalid input. Please try again.")

        self.turn_index += 1
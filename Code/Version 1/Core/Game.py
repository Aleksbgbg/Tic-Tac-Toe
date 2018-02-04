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
        while True:
            match = re.match(r"^\(?(?P<x>[1-3]),? ?(?P<y>[1-3])\)?$", input("Enter coordinate: "))

            if match:
                break

            print("Invalid input. Please try again.")

        self.matrix[int(match.group("x")) - 1, int(match.group("y")) - 1] = ["X", "O"][self.turn_index % 2]
        self.turn_index += 1

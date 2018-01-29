from .Matrix import Matrix

class Game:
    def __init__(self):
        self.matrix = Matrix(3, 3)
        self.coordinate = ""

    def update_model(self):


    def compose_frame(self):
        self.matrix.print()
        self.coordinate = input("Enter coordinate: ")
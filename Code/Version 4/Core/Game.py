from .Matrix import Matrix
import re


class Game:
    def __init__(self):
        self.matrix = Matrix(3, 3)
        self.turn_index = 0

    def run(self):
        self.compose_frame()

        if self.process_game_state():
            return False

        self.update_model()

        return True

    def process_game_state(self):
        def process_succession(iterable, generator):
            for item in iterable:
                symbols = "".join(set(generator(index, item) for index in range(3)))

                if len(symbols) == 1 and symbols != "-":
                    print(f"{symbols} wins!")
                    return True

        if any(
                [
                    process_succession(range(3), lambda column, _: self.matrix[column, 0]),
                    process_succession(range(3), lambda row, _: self.matrix[0, row]),
                    process_succession([0, 2],
                                       lambda index, diagonal: self.matrix[
                                                   index + [diagonal, 0, -diagonal][index], index])
                ]
        ):
            return True

        if all(map(lambda symbol: symbol != "-", self.matrix)):
            print("Draw!")
            return True

        return False

    def compose_frame(self):
        self.matrix.print()

    def update_model(self):
        def check_input(input, regex, transform):
            match = re.match(regex, input)

            if match:
                coordinate = transform(match)

                if self.matrix[coordinate] != "-":
                    return False

                self.matrix[coordinate] = ["X", "O"][self.turn_index % 2]
                return True

            return False

        while True:
            input_string = input("Enter coordinate: ")

            if check_input(input_string, r"^\(?(?P<x>[1-3]),? ?(?P<y>[1-3])\)?$",
                           lambda match: (int(match.group("x")) - 1, int(match.group("y")) - 1)):
                break

            if check_input(input_string, "^(?P<index>[1-9])$", lambda match: int(match.group("index")) - 1):
                break

            print("Invalid input Please try again.")

        self.turn_index += 1
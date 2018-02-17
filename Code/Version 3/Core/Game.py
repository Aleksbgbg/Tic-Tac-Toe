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
        def set_symbol(coordinate):
            self.matrix[coordinate] = ["X", "O"][self.turn_index % 2]

        def is_bad_coordinate(coordinate):
            return self.matrix[coordinate] != "-"

        while True:
            input_string = input("Enter coordinate: ")

            match = re.match(r"^\(?(?P<x>\d+),? ?(?P<y>\d+)\)?$",
                             input_string)

            if match:
                def truncate(coordinate_point):
                    return min(max(coordinate_point, 1), 3)
                
                coordinate = (truncate(int(match.group("x"))) - 1, truncate(int(match.group("y"))) - 1)

                if is_bad_coordinate(coordinate):
                    print("Bad coordinate. Please try again.")
                    continue

                set_symbol(coordinate)
                break

            match = re.match("^(?P<index>\d+)$", input_string)

            if match:
                coordinate = min(max(int(match.group("index")), 1), 9) - 1

                if is_bad_coordinate(coordinate):
                    print("Bad coordinate. Please try again.")
                    continue

                set_symbol(coordinate)
                break

            print("Invalid input. Please try again.")

        self.turn_index += 1

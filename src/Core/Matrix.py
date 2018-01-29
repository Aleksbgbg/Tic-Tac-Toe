class Matrix:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.matrix = ["-" for _ in range(height * width)]

    def __getitem__(self, item):
        return self.matrix[self.map_index(item)]

    def __setitem__(self, key, value):
        self.matrix[self.map_index(key)] = value

    def map_index(self, coordinate):
        x, y = coordinate
        return x + y * self.width

    def print(self):
        print("\n".join(" ".join(self[column, row] for column in range(self.width)) for row in range(self.height)))
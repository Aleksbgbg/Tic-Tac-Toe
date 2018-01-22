from kivy.app import App
from kivy.lang import Builder


class TicTacToe(App):
    def build(self):
        return Builder.load_file("../Views/Main.kv")
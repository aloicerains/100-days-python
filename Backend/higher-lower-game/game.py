"""Game module"""
from random import randint


class Game:
    SCORE = 0
    GAMES = 0
    def __init__(self):
        self.random_number = self.get_random()
        self.continuation = "Try again!"
        self.attempts = 0
    def get_random(self):
        """Gets random number"""
        return randint(1, 10)

    def counter(self):
        if self.attempts >= 2:
            self.continuation = "Game over! Start a new Game"
            self.random_number = self.get_random()
            Game.GAMES += 1
        self.attempts += 1

    def update_score(self, result):
        """Update score"""

        if result > self.random_number:
            self.counter()
            return f'<h3 style="color:red">Too high! {self.continuation}</h3>' \
                   '<img style="height:300px" src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="puppy flying">'
        elif result < self.random_number:
            self.counter()
            return f'<h3 style="color:blue">Too low! {self.continuation}</h3>' \
                   '<img style="height:300px" src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" ' \
                   'alt="puppy low">'
        else:
            Game.SCORE += 1
            Game.GAMES += 1
            return '<h3 style="color:green">Hurrah, You found me! Start a new game</h3>' \
                   '<img style="height:300px" src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="puppy found">'




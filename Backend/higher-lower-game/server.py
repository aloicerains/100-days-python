"""Server Module"""
from flask import Flask
from game import Game

app = Flask(__name__)
game: Game

def score_decorator(fn):
    def wrapper(*args, **kwargs):
        val = fn(kwargs['user_in'])
        return f'<div style="text-align: center">{val}' \
               f'<h4 style="color: magenta">Your Score: {Game.SCORE}</h4>' \
               f'<h4 style="color: magenta">Number of Games: {Game.GAMES}' \
               f'</div>'
    return wrapper
@app.route("/")
def guess_game():
    global game
    game = Game()
    return '<h1 style="text-align: center">Guess a number from 1 to 10</h1>' \
           '<div style="text-align: center"><img src="https://media.giphy.com/media/lKXEBR8m1jWso/giphy.gif" alt="gif">' \
           '</div>'

@app.route("/<int:user_in>")
@score_decorator
def user_input(user_in):
    """Gets the user input"""
    try:
        return game.update_score(user_in)
    except NameError:
        guess_game()


if __name__ == '__main__':
    app.run(debug=True)
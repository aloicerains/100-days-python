from flask import Flask
app = Flask(__name__)

def make_bold(fn):
    def bolder():
        val = fn()
        return f'<b>{val}</b>'
    return bolder

def make_emphasis(fn):
    def emphasizer():
        val = fn()
        return f'<em>{val}</em>'
    return emphasizer
def make_underlined(fn):
    def under_line():
        val = fn()
        return f'<u>{val}</u>'
    return under_line

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"
@app.route('/<name>')
def hello_name(name):
    return f'Hello, {name + str(12)}'

if __name__ == "__main__":
    # runs the app in debug mode to allow auto reloading
    app.run(debug=True)
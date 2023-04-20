from flask import Flask, render_template
from post import Post


app = Flask(__name__)
new_post = Post()
@app.route('/')
def home():
    blogs = new_post.get_posts()
    return render_template("index.html", blogs=blogs)

@app.route('/post/<int:id>')
def read_post(id):
    the_post = new_post.get_posts()[id-1]
    return render_template("post.html", the_post=the_post)

if __name__ == "__main__":
    app.run(debug=True)

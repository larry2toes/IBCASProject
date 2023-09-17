import flask, os, db
from flask import Flask, render_template, request
from db import Post

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

p = Post("Name", "blah blah blah")
posts = [p]

@app.route("/")
def test():
    return render_template('index.html')

@app.route('/upvote/<post>', methods=['POST'])
def upvote(post):
    if(posts.count(post) < 1 ): return 404
    p = posts[posts.index(post)]
    id = request.form.get('id')
    
    p.upvote(id)
    print(f"{posts} | {p.upvotes}")
    return 200

if __name__ == '__main__':
   app.run('0.0.0.0', 54321)
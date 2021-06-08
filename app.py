from flask import Flask, render_template, request
# from flask_cors import CORS
from models import create_content, get_posts

# server object
app = Flask(__name__)

# CORS(app)

# routes/endpoints


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        content = request.form.get('content')
        create_content(name, content)

    posts = get_posts()

    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)

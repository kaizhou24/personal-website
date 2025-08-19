from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        'title': 'Personal Website',
        'description': 'A personal portfolio site built with Python and Flask to showcase my projects and interests.',
        'technologies': ['Python', 'Flask', 'HTML', 'CSS'],
        'github_link': '#'
    },
]

@app.route('/')
def index():
    return render_template('index.html', projects=projects)
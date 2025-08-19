from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        'title': 'Personal Website',
        'description': 'A personal portfolio site built with Python and Flask to showcase my projects and skills.',
        'technologies': ['Python', 'Flask', 'HTML', 'CSS'],
        'github_link': '#'
    },
    {
        'title': 'Financial Data Analyzer',
        'description': 'A tool for analyzing stock market data and generating performance reports.',
        'technologies': ['Python', 'Pandas', 'Matplotlib'],
        'github_link': '#'
    },
    {
        'title': 'Project Management App',
        'description': 'A concept for a SaaS tool to help teams manage tasks and deadlines.',
        'technologies': ['Python', 'Flask-SQLAlchemy', 'React'],
        'github_link': '#'
    }
]

@app.route('/')
def index():
    return render_template('index.html', projects=projects)
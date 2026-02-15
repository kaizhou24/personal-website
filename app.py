from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        'title': 'Portfolio Correlation and Mean-Variance Optimization',
        'description': 'A portfolio optimization tool uses a Monte Carlo simulation based on Modern Portfolio Theory to analyze historical data and visualize the Efficient Frontier, pinpointing portfolios with the highest risk-adjusted returns.',
        'technologies': ['Python', 'Pandas' , 'NumPy', 'Matplotlib', 'Seaborn'],
        'github_link': 'https://github.com/kaizhou24/portfolio-correlation-mvo',
    },
    {
        'title': "Conway's Game of Life",
        'description': 'An optimized implementation of Conway\'s Game of Life cellular automaton with interactive controls.',
        'technologies': ['JavaScript', 'HTML', 'CSS'],
        'github_link': 'https://kaizhou24.github.io/game-of-life/'
    },
    {
        'title': 'Personal Website',
        'description': 'A personal portfolio site built with Python and Flask to showcase my projects and interests.',
        'technologies': ['Python', 'Flask', 'HTML', 'CSS'],
        'github_link': '#'
    },
    {
        'title': "Conway's Game of Life",
        'description': 'An implementation of Conway\'s Game of Life cellular automaton with interactive controls.',
        'technologies': ['JavaScript', 'HTML', 'CSS'],
        'github_link': 'https://kaizhou24.github.io/game-of-life/'
    },
]

@app.route('/')
def index():
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
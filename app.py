# Imports
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs, pygmented_markdown
from renderer import custom_renderer


# App
app = Flask(__name__)
app.config.from_envvar('CONFIGURATION_FILE')
app.config.update({'FLATPAGES_HTML_RENDERER': custom_renderer})
pages = FlatPages(app)


# Route: Index
@app.route('/')
def index():
    return render_template('index.html', pages=pages)


# Route: Page
@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


# Route: Pygments style definition
@app.route('/pygments.css')
def pygments_css():
    pygments_style = app.config.get('FLATPAGES_PYGMENTS_STYLE', 'default')
    return pygments_style_defs(pygments_style), 200, {'Content-Type': 'text/css'}


if __name__ == '__main__':
    app.run()
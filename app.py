# Imports
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs, pygmented_markdown


# Config
config = {
    'DEBUG': True,
    'FLATPAGES_AUTO_RELOAD': True,
    'FLATPAGES_ROOT': 'content/',
    'FLATPAGES_CONTENT_URL': '',
    'FLATPAGES_MEDIA_URL': '/static/media',
    'FLATPAGES_EXTENSION': '.md',
    'FLATPAGES_MARKDOWN_EXTENSIONS': [
        'codehilite', 'fenced_code', 'footnotes', 
        'attr_list', 'tables', 'pymdownx.tilde'
    ],
}


# HTML renderer
def custom_renderer(body, fp_instance, page):
    body = body.replace('%CONTENT_URL%', config.get('FLATPAGES_CONTENT_URL'))
    body = body.replace('%MEDIA_URL%', config.get('FLATPAGES_MEDIA_URL'))
    return pygmented_markdown(body, flatpages=fp_instance)
config.update({'FLATPAGES_HTML_RENDERER': custom_renderer})


# App
app = Flask(__name__)
app.config.update(config)
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
    return pygments_style_defs('monokai'), 200, {'Content-Type': 'text/css'}
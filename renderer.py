# Imports
from flask_flatpages import pygmented_markdown


# HTML renderer
def custom_renderer(body, fp_instance, page):
    variables = {
        '%CONTENT_URL%': fp_instance.app.config.get('FLATPAGES_CONTENT_URL'),
        '%MEDIA_URL%': fp_instance.app.config.get('FLATPAGES_MEDIA_URL'),
    }

    for v, c in variables.items():
        body = body.replace(v, c)
    
    return pygmented_markdown(body, flatpages=fp_instance)
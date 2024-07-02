#!/usr/bin/env python3
"""Basic Babel Setup"""

from flask import Flask, render_template, request
from flask_babel import Babel
import os

app = Flask(__name__)


class Config:
    """babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# flask app configuration
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Return the best match language"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    """return html file"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)

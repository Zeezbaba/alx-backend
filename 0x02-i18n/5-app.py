#!/usr/bin/env python3
"""Basic Babel Setup"""

from flask import Flask, render_template, request, g
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """function that returns a user dictionary or None"""
    login_as = request.args.get('login_as')
    if login_as:
        user_id = int(login_as)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """use get_user to find a user if any"""
    g.user = get_user()


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
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)

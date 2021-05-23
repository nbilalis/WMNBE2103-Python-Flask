import locale
from datetime import datetime
from os import environ
from flask import Flask, render_template, request, redirect, url_for, session, flash
from jinja2 import filters

from products_service import get_products

app = Flask(__name__)

# import os; os.urandom(24).hex()
app.secret_key = environ.get('SECRET_KEY', '1234')


@app.route('/')
def home():
    if not session['timestamp']:
        session['timestamp'] = datetime.now()
    return render_template('index.html')


@app.get('/search')
def search_products():
    q = request.args.get('q')

    products = get_products(q) if q else []

    return render_template('search.html', products=products)


@app.get('/register')
def show_registration_form():
    return render_template('register.html')


@app.post('/register')  # @app.route('/register', methods=['POST'])
def register_user():
    username = request.form.get('username')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')

    app.logger.debug(username)
    app.logger.debug(firstname)
    app.logger.debug(lastname)

    errors = []

    if len(username) < 3:
        errors.append({'msg': 'Firstname should be at least 3 chars long', 'field': 'username'})
    if len(firstname) < 3:
        errors.append({'msg': 'Firstname should be at least 3 chars long', 'field': 'firstname'})
    if len(lastname) < 3:
        errors.append({'msg': 'Lastname should be at least 3 chars long', 'field': 'lastname'})

    if len(errors) == 0:
        flash('Registration was successful')
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return render_template('register.html', errors=errors)


def format_currency(value):
    locale.setlocale(locale.LC_ALL, 'el_GR')
    return locale.currency(value, symbol=True, grouping=True)


filters.FILTERS['format_currency'] = format_currency


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=environ.get('SERVER_PORT', 5000))

import locale

from os import environ

from flask import Flask, render_template, abort
from jinja2 import filters

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/products/')
def product_list():
    return render_template('products/list.html', products=get_products())


@app.route('/products/<sku>')
def product_details(sku):
    products = get_products()
    product = products.get(sku, None)

    if product is not None:
        return render_template('products/details.html', product=product)
    else:
        abort(404)


@app.route('/hello/')
@app.route('/hello/<username>')
def hello(username=None):
    return render_template('hello.html', username=username)


@app.errorhandler(404)
def page_not_found(e):
    app.logger.debug(e)
    # note that we set the 404 status explicitly
    return render_template('errors/404.html'), 404


def get_products():
    return {
        '0001': {'sku': '0001', 'title': 'Awesome Product #1', 'description': 'Blah blah. ' * 50, 'price': 2.34},
        '0002': {'sku': '0002', 'title': 'Awesome Product #2', 'description': 'Blah blah. ' * 50, 'price': 3.45},
        '0003': {'sku': '0003', 'title': 'Awesome Product #3', 'description': 'Blah blah. ' * 50, 'price': 4.56},
    }


def format_currency(value):
    locale.setlocale(locale.LC_ALL, 'el_GR')
    return locale.currency(value, symbol=True, grouping=True)


filters.FILTERS["format_currency"] = format_currency


app.logger.debug(__name__)


if __name__ == '__main__':
    port = environ.get('SERVER_PORT', 5000)
    app.run(host='localhost', port=port)

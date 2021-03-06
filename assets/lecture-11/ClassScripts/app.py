from datetime import datetime
from os import environ, path, listdir
from flask import Flask, g, render_template, request, make_response, abort
import sqlite3

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# python -c "import os; print(os.urandom(24).hex())"
app.secret_key = environ.get('SECRET_KEY', '1234')
toolbar = DebugToolbarExtension(app)

BASE_PATH = path.dirname(path.abspath(__file__))
DATABASE_PATH = path.join(BASE_PATH, 'data/flask-news.db')


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))


def get_con():
    con = getattr(g, 'con', None)   # con = g.con
    if con is None:
        con = sqlite3.connect(DATABASE_PATH)
        con.row_factory = sqlite3.Row
        # con.row_factory = make_dicts
        setattr(g, 'con', con)      # g.con = con
    return con


@app.teardown_appcontext
def close_connection(ctx):
    if con := g.pop('con', None):
        app.logger.debug(con)
        con.close()

    return None


@app.get('/')
def home():
    # return render_template('home.html'), {'Set-Cookie': 'foo=bar'}
    res = make_response(render_template('home.html'))
    if request.cookies.get('timestamp') is None:
        res.set_cookie('timestamp', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return res


@app.get('/articles')
def article_list():
    cur = get_con().cursor()
    articles = cur.execute(
        '''
        SELECT "id", "title"
        FROM "article"
        '''
    ).fetchall()

    app.logger.debug([dict(a) for a in articles])

    return render_template('/articles/list.html', articles=articles)


@app.get('/articles/<int:id>')
def article_details(id):
    cur = get_con().cursor()
    article = cur.execute(
        '''
        SELECT "id", "title", "body"
        FROM "article"
        WHERE "id" = :id
        ''',
        {'id': id}
    ).fetchone()

    if article is None:
        abort(404)

    app.logger.debug(dict(article))

    return render_template('articles/details.html', article=article)


@app.cli.command('create-db')
# @click.argument('name')
def init_db():
    migrations_path = path.join(BASE_PATH, '_migrations')
    for file in listdir(migrations_path):
        file_path = path.join(migrations_path, file)
        with app.app_context():
            with get_con() as con:
                with app.open_resource(file_path, mode='r') as f:
                    contents = f.read()
                    con.cursor().executescript(contents)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=int(environ.get('SERVER_PORT', 8081)))

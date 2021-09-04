from flask import current_app as app
from werkzeug.security import generate_password_hash

from . import db                # from app import db
from .models import User, Post  # from app.models import User, Post


from random import randint, choice, sample
from datetime import datetime, timedelta
from lorem import sentence, paragraph


@app.cli.command('init-db')
def init_db():
    db.drop_all()
    db.create_all()


@app.cli.command('add-data')
def add_data():
    User.query.delete()

    db.session.commit()

    users = []

    users.append(User(username='haris', email='haris@sae.edu', lastname='Argyropoulos', firstname='Zacharias-Christos', password=generate_password_hash('12121212')))
    users.append(User(username='ioanna', email='ioanna@sae.edu', lastname='Mitsani', firstname='Ioanna', password=generate_password_hash('12121212')))
    users.append(User(username='stavros', email='stavros@sae.edu', lastname='Tsiogkas', firstname='Stavros', password=generate_password_hash('12121212')))
    users.append(User(username='marios', email='marios@sae.edu', lastname='Tsioutsis', firstname='Marios', password=generate_password_hash('12121212')))

    users.append(User(username='george', email='george@sae.edu', lastname='Sisko', firstname='George', password=generate_password_hash('12121212')))
    users.append(User(username='lena', email='lena@sae.edu', lastname='Lekkou', firstname='Lena', password=generate_password_hash('12121212')))
    users.append(User(username='nikos.a', email='nikos.a@sae.edu', lastname='Apostolakis', firstname='Nikolaos', password=generate_password_hash('12121212')))
    users.append(User(username='nikos.b', email='nikos.b@sae.edu', lastname='Bilalis', firstname='Nikolaos', password=generate_password_hash('12121212')))

    for u in users:
        u.followers = [f for f in sample(users, randint(1, len(users))) if f != u]
        db.session.add(u)

    ts = datetime.now() - timedelta(weeks=6*4)    # .utcnow()

    while datetime.now() >= ts:
        p = Post(body=paragraph(), created_at=ts)
        u = choice(users)
        u.posts.append(p)
        ts += timedelta(microseconds=randint(1, 10**11))

    db.session.commit()

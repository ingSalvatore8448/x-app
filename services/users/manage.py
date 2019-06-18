# services/users/manage.py

import unittest

from flask.cli import FlaskGroup

from project import create_app, db  # nuevo
from project.api.models import User  # nuevo


app = create_app()  # nuevo
cli = FlaskGroup(create_app=create_app)  # nuevo


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """Ejecutando los test sin cobertura de código"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(User(username='salvatore', email="el_nene_8448@hotmail.com"))
    db.session.add(User(username='ingSalvatore8448', email="salvadorybarzola@upeu.edu.pe"))
    db.session.commit()


if __name__ == '__main__':
    cli()

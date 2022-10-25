import os
from flask_migrate import Migrate

from app import create_app, db
from app.models import ExampleModel


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
  return dict(db=db, ExampleModel=ExampleModel)


@app.cli.command()
def test():
  """Run the unit tests."""
  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)


@app.cli.command()
def lint():
  """Run the linter"""
  os.system('flake8')


@app.cli.command()
def seed():
  """Populate the database"""
  db.drop_all()
  db.create_all()

  characters = ['a', 'b', 'c']
  models = [ExampleModel(string_attribute=character)
            for character in characters]
  db.session.add_all(models)
  db.session.commit()

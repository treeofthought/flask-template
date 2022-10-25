# Flask Template
A very generic Flask API that can be copy-pasted to create new projects

## Usage
### `flask run` 
launch the application.

### `flask test`
run unit tests

### `flask shell`
launch interactive shell

### `flask seed`
Populate the database with some example objects.  
**Warning**, erases any pre-existing database.

### `flask lint`
run linting

## Initial Setup.
With a mind towards one day automating flask projects. This is not the way to get the app quickly duplicated.

### Create virtual env
`mkvenv`
`pip install flask`
`pip install flake8`
`pip install Flask-SQLAlchemy`
`pip freeze > requirements.txt`

### `.gitignore`
With some obvious known contents.

### Architectural boilerplate...
`touch .flaskenv` and populate with `FLASK_APP=tot-api.py` and `FLASK_ENV=development`
`mkdir app`  
`touch app/__init__.py` And this file needs contents.  
`touch app/models.py` And this file needs contents.  
`touch tot-api.py`. And this file needs contents
`mkdir tests`
`touch tests/__init__.py`
`touch tests/test_basics.py` And this file needs contents
`touch .flake8` And this file needs contents
`flask db init` To initialize database

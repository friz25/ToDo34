python -m venv venv
. venv/Scripts/activate

pip install Flask
pip install Flask-SQLAlchemy

set FLASK_APP=flask_ToDO.py
set FLASK_ENV=development
flask run
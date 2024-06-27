from flask import Flask
from flask import (
    render_template,
    redirect,
    url_for,
    request,
    flash,
    abort,
)
from dotenv import load_dotenv
import os


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.get('/')
def index():
    return render_template('index.html')

import os

from flask import Flask, session, redirect, render_template, request, flash, jsonify, abort
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(postgres://ypvuuadaexvgmf:4fcf02037d868398ac646f6d3cb05ca4b0ca1ccc4ff055b89fdc80fa5147d149@ec2-23-23-182-18.compute-1.amazonaws.com:5432/d2hg9oifn1sa61, pool_size=10, max_overflow=20)
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")

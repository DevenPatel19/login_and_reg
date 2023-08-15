from flask import Flask, flash, redirect, render_template, request, session

from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.secret_key = "9a97a7debecf8c3475d9ff326038fd14eb9ee9a7118bcaa3b210213703409c74"
bcrypt = Bcrypt(app)

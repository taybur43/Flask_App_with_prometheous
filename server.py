import logging
from flask import render_template
from flask import Flask
from flask import jsonify
from prometheus_flask_exporter import PrometheusMetrics

logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")


@app.route("/")
def hello():
    return jsonify(say_hello())
def say_hello():
    return {"message": "hello"}

@app.route('/index')
def index():
    return render_template('home.html')
@app.route('/about')
def about():
  return render_template('about.html')
@app.route('/live')
def live():
  return render_template('hello.html')
@app.route('/login')
def login():
  return render_template('login.html')


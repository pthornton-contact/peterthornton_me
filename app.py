from flask import Flask, render_template, redirect, url_for
application = Flask(__name__)

@application.route("/")
def index():
    return render_template('index.html')

@application.route("/appsy/")
def appsy():
    return render_template('appsy.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0')

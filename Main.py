from flask import Flask


main = Flask(__name__)


@main.route('/')
def root():
    return {"massage": "hello World"}


#! /usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    m = {1:'Hello', 2: 'Nix', 3: 'World' }
    return m[1] + ' ' + m[2] + ' ' + m[3]

def run():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    run()

